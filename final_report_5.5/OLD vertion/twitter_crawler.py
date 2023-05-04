import time
import datetime
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
limit_language = 'en'

def connent_url(UrlPath):
    Data_List = []
    df = pd.read_csv(UrlPath)

    i = 1
    for url in df:
        driver.get(url=UrlPath)
        driver.implicitly_wait(200)
        page =0
        try:
            old_scroll_height = 0  # 表明页面在最上端
            js1 = 'return document.body.scrollHeight'  # 获取页面高度的javascript语句
            js2 = 'window.scrollTo(0, document.body.scrollHeight)'  # 将页面下拉的Javascript语句
            while (driver.execute_script(js1) > old_scroll_height):  # 将当前页面高度与上一次的页面高度进行对比
                old_scroll_height = driver.execute_script(js1)  # 获取到当前页面高度
                driver.execute_script(js2)  # 操控浏览器进行下拉
                time.sleep(3)  # 空出加载的时间
                html = driver.page_source
                old_scroll_height = 0  # 表明页面在最上端
                js1 = 'return document.body.scrollHeight'  # 获取页面高度的javascript语句
                js2 = 'window.scrollTo(0, document.body.scrollHeight)'  # 将页面下拉的Javascript语句
                soup = BeautifulSoup(html, 'html.parser')
                divs = soup.find_all(
                    'div', {'class': 'css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu'})
                print(divs)
                page += 1
                print('Fetching data on page {}！！！'.format(page))

                for div in divs:
                    data_list = []
                    name = div.find_all(
                        'div', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'}).get_text()
                    data_list.append(name)
                    user_name = div.find(
                        'div', {'class': 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'}).get_text()
                    data_list.append(user_name)
                    date = div.find('time')
                    data_list.append(date['datetime'])
                    content = div.find_all('div', {
                        'class="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"'}).get_text()
                    data_list.append(str(content).strip().replace('\n', ''))
                    Data_List.append(data_list)
                    language = content.get('lang')
                    '''like class="css-901oao r-1awozwy r-14j79pv r-6koalj r-37j5jr r-a023e6 r-16dba41 r-1h0z5md r-rjixqe r-bcqeeo r-o7ynqc r-clp7b1 r-3s2u2q r-qvutc0"
                       view class="css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1777fci r-bt1l66 r-1ny4l3l r-bztko3 r-lrvibr"
                       review class="css-18t94o4 css-1dbjc4n r-1777fci r-bt1l66 r-1ny4l3l r-bztko3 r-lrvibr"
                       retweet class="css-901oao r-1awozwy r-14j79pv r-6koalj r-37j5jr r-a023e6 r-16dba41 r-1h0z5md r-rjixqe r-bcqeeo r-o7ynqc r-clp7b1 r-3s2u2q r-qvutc0"'''
                    if ((language == limit_language)):
                        data_list.append(name)  # 名字
                        data_list.append(user_name)  # 用户名
                        data_list.append(date)
                        data_list.append(str(content).strip().replace('\n', ''))  # 内容
                    else:
                        continue
                    Data_List.append(data_list)
        except Exception as e:
            print(e)
        print('finish crawling'.format(i))
        i = i + 1

    driver.close()

    Data_List_New = []
    for data in Data_List:
        if data not in Data_List_New:
            Data_List_New.append(data)
    return Data_List_New


def Save_Data(UrlPath):
    """
    get data and store in csv
    """
    Data_List_New = connent_url(UrlPath=UrlPath)
    print('crawl '.format(len(Data_List_New)))
    df_Sheet = pd.DataFrame(Data_List_New, columns=[
                            'name', 'user_name', 'date', 'content'])
    print('Get data successfully!!!')

    TIMEFORMAT = '%Y-%m-%d_%H_%M_%S'
    now = datetime.datetime.now().strftime(TIMEFORMAT)
    csv_path = 'TwitterData/Twitter_Data(' + now + ').txt'
    df_Sheet.to_csv(csv_path)
    now = datetime.datetime.now().strftime(TIMEFORMAT)
    csv_path = 'TwitterData/Twitter_Data(' + now + ').csv'
    df_Sheet.to_csv(csv_path)

    excel_path = 'TwitterData/Twitter_Data(' + now + ').xlsx'
    writer = pd.ExcelWriter(excel_path)
    df_Sheet.to_excel(excel_writer=writer, sheet_name='twitter', index=True)
    writer.save()
    print('Save - successfully!!!')
    writer.close()
    print('Close - successfully!!!')


def Run():
    Save_Data(UrlPath='twitter_url.txt')


if __name__ == '__main__':
    Run()
