# -*- coding: utf-8 -*-
import requests
import scrapy
from bs4 import BeautifulSoup
from scrapy import FormRequest
from scrapy.utils.project import get_project_settings




class ProSpider(scrapy.Spider):
    name = 'pro'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']
    settings = get_project_settings()
    my_header = settings['HEADER']
    my_username = 'ljl'
    my_password = '123456'

    def start_requests(self):
        # url = 'https://login.sina.com.cn/signup/signin.php'
        url = 'http://127.0.0.1:8000/login/'
        # url = 'https://weibo.com/'
        html = requests.get(url, headers=self.my_header).text
        soup = BeautifulSoup(html, 'lxml')
        csrf = soup.find_all(class_='login-form')[0].input['value']
        postData = {
            'username': self.my_username,
            'password': self.my_password,
            'csrfmiddlewaretoken': csrf
        }
        return [FormRequest(
            url,
            method='POST',
            meta={'cookiejar': 1}, headers=self.my_header,
            formdata=postData,
            callback=self.parse
        )]



    def parse(self, response):
        print('parse', response.text)
        # pass
