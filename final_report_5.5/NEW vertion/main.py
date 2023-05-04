from functions import *
from selenium import webdriver
import os

if __name__ == '__main__':

    driver = webdriver.Chrome()
    print('------------------------------------------------------------------------')
    # --------------------------------------------------------------------------------
    # parameters
    URL_Path = 'URL.csv'
    Stop_num = 10  # this is the number of the items you want to crawl
    kw_start_point = 0  # this parameter decides the start keyword of the crawler.its default value is 0
    save_path = 'data'  # this is the path where you want to save the crawled data
    start_date = '2023-01-29'  # this parameter decides the start date of the crawler.its default value is 2021-01-01
    end_date = '2023-05-01'  # this parameter decides the end date of the crawler.its default value is 2020-01-01
    limit_language = 'en'  # this parameter decides the language of the crawler.its default value is en
    # ----------------------------------------------------------------------------------
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    Twitter_Crawler(driver, URL_Path, Stop_num, kw_start_point, save_path, start_date, end_date, limit_language)
    print('------------------------------------------------------------------------')
    driver.close()
