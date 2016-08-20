# -*- coding: utf-8 -*-
from lxml import html
import requests
import redis

import settings


class Spider_zhihu():

    def __init__(self, url, option=settings.OUTPUT):
        self.url = url
        self.header = {}
        self.option = option
        self.cookies = settings.MYCOOKIES
        self.header['User-Agent'] = settings.MYAGENT

    def get_user_data(self):
        # 获取用户信息
        # 核心部分
        followee_url = self.url.decode('utf-8') + '/followees'
        try:
            request = requests.get(
                followee_url,
                cookies=self.cookies,
                headers=self.header,
                verify=False
            )
        except:
            print('request error!')
            return

        if request.status_code == 200:
            content = request.text
            self.analy_profile(content)
            return

    def analy_profile(self, html_file):
        # 解析抓取的网页
        tree = html.fromstring(html_file)
        self.user_name = self.get_xpath_source(tree.xpath(settings.ZHIHU_NAME))
        self.user_location = self.get_xpath_source(tree.xpath(settings.ZHIHU_LOCATION))
        self.user_gender = self.get_xpath_source(tree.xpath(settings.ZHIHU_GENDER))
        if self.user_gender and u'female' in self.user_gender:
            self.user_gender = u'female'
        else:
            self.user_gender = u'male'
        self.user_employment = self.get_xpath_source(tree.xpath(settings.ZHIHU_EMPLOYMENT))
        self.user_employment_extra = self.get_xpath_source(tree.xpath(settings.ZHIHU_EMPLOYMENT_EXTRA))
        self.user_education_school = self.get_xpath_source(tree.xpath(settings.ZHIHU_EDUCATION))
        self.user_education_subject = self.get_xpath_source(tree.xpath(settings.ZHIHU_EDUCATION_EXTRA))

        try:
            self.user_followees = tree.xpath(settings.ZHIHU_FOLLOW)[0]
            self.user_followers = tree.xpath(settings.ZHIHU_FOLLOW)[1]
        except:
            return
        self.user_be_agreed = self.get_xpath_source(tree.xpath(settings.ZHIHU_AGREED))
        self.user_be_thanked = self.get_xpath_source(tree.xpath(settings.ZHIHU_THANKED))
        self.user_info = self.get_xpath_source(tree.xpath(settings.ZHIHU_USER_INFO))
        self.user_intro = self.get_xpath_source(tree.xpath(settings.ZHIHU_USER_INTRO))

        if self.option == settings.OUTPUT:
            # self.decode('utf-8')
            self.print_data_out()
        else:
            self.store_data_to_mongod()

        global red

        # 提取出被关注者的url
        url_list = tree.xpath(settings.ZHIHU_FOLLOWEE_URL)
        for target_url in url_list:
            if red.sadd('had_spidered', target_url):
                red.lpush('to_spider', target_url)

    def get_xpath_source(self, source):
        if source:
            return source[0]
        else:
            return ''

    def print_data_out(self):
        print(u'用户名：{user_name}'.format(user_name=self.user_name))
        print(u'用户性别：{user_gender}'.format(user_gender=self.user_gender))
        print(u'被感谢：{thanked}'.format(thanked=self.user_be_thanked))
        print(u'被赞同：{agreed}'.format(agreed=self.user_be_agreed))
        print(u'工作地：{location}'.format(location=self.user_location))
        print(u'行业：{employment}'.format(employment=self.user_employment))
        print(u'工作信息：{employment_extra}'.format(employment_extra=self.user_employment_extra))
        print(u'教育信息：{school}/{subject}'.format(
            school=self.user_education_school,
            subject=self.user_education_subject)
        )
        print(u'个人简介：{info}'.format(info=self.user_info))

    def store_data_to_mongod(self):
        pass


def bfs_search(option):
    global red
    time = 10

    while time > 0:
        url = red.rpop('to_spider')
        if url:
            red.sadd('had_spidered', url)
            spider = Spider_zhihu(url, option)
            spider.get_user_data()
            time -= 1
        else:
            break

    print(u'完成。')
    return

if __name__ == '__main__':
    output_option = settings.OUTPUT
    source_url = 'https://www.zhihu.com/people/lu-jian-yao-qing-60'

    red = redis.Redis(host='localhost', port=6379, db='1')
    red.lpush('to_spider', source_url)

    bfs_search(output_option)
