import pandas as pd
import requests
import re

def getMessage(url):
    heasers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}
    response = requests.get(url, headers=heasers)
    if response.status_code == 200:
        return response.text
    return None

def parseMessage(html):
    pattern1 = re.compile('<li.*?data-info=.*?i*?class="icon.*?title="(.*?)"', re.S | re.M)
    pattern2 = re.compile('li.*?data-info=.*?i*?class="icon.*?title=".*?<b>(.*?)</b>', re.S | re.M)
    pattern3 = re.compile(
        '<li.*?data-info=.*?i*?class="icon.*?title=".*?<div.*?class="job-info".*?<h3.*?title="(.*?)">', re.S | re.M)
    pattern4 = re.compile(
        '<li.*?data-info=.*?i*?class="icon.*?title=".*?<div.*?class="job-info".*?<h3.*?<p.*?class="condition clearfix".*?title="(.*?)">',
        re.S | re.M)
    pattern5 = re.compile(
        '<li.*?data-info=.*?i*?class="icon.*?title=".*?<div.*?class="job-info".*?<h3.*?<p.*?class="condition clearfix".*?<p.*?class="time-info clearfix".*?<div.*?class="company-info nohover".*?<p.*?<a.*?title="(.*?)"',
        re.S | re.M)
    title1 = re.findall(pattern1, html)
    title2 = re.findall(pattern2, html)
    title3 = re.findall(pattern3, html)
    title4 = re.findall(pattern4, html)
    title5 = re.findall(pattern5, html)

    Dict = {
        'Fankui': title1,
        'Status': title2,
        'Position': title3,
        'Work': title4,
        'Companyname': title5
    }
    return Dict

def main():
    url = 'https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90'
    html = getMessage(url)
    Data = parseMessage(html)
    pd.DataFrame(Data, columns=['Fankui', 'Status', 'Position', 'Work', 'Companyname']).to_csv("E://数据分析数据集.csv", encoding="utf_8_sig")
main()