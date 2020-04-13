import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class LinkChecker():

    def get_page_info(self, url):
        page_info = requests.get(url)
        return page_info

    def get_list_url(self, base_url, html):
        soup = BeautifulSoup(html, "html.parser")
        list_a_tag = soup.find_all('a')
        list_url = []
        for a in list_a_tag:
            url = a.get('href')
            if url == None :
                continue
            ab_url = urljoin(base_url, url)
            if ab_url not in list_url:
                list_url.append(ab_url)
        return list_url

    def check_url_status(self, list_url):
        list_error_url = []
        for url in list_url:
            dict_url = {}
            page_info = requests.get(url)
            if page_info.status_code >= 400:
                dict_url['status'] = page_info.status_code
                dict_url['url'] = url
                list_error_url.append(dict_url)
            print(str(page_info.status_code) + " : " + url)
        return list_error_url

    