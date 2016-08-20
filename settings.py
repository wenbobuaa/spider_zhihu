# -*- coding: utf-8 -*-
OUTPUT = 1
DBPUT = 0

MYAGENT = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')

MYCOOKIES = {
    'd_c0': '"ABDALIVoQAqPTo8EI1iRDcgGNd8mo3NdJ6g=|1468901058"',
    '_za': 'c22d3b22-d31d-4734-9c95-0011257e5cba',
    '_xsrf': '88c6e5cc84e7ca6e94a414eece7e3b25',
    '_zap': '8747fcca-bd6c-464a-8739-8448b79ee2c1',
    'oauth_from': '"/"',
    'o_act': 'login',
    'q_c1': 'a4ea01c9e34b440d92f2aeb56456389a|1469506641000|1469506641000',
    'l_cap_id': '"ZTU1MDNhZDRkZTI4NDlmMWIxN2Y5YTJlYjY5YmIwMDg=|1470107776|f87d06f79362f702055b46f42f5ddf3604342d11"',
    'cap_id': '"ZjczYzdiMDYyOGU5NDc4NGJhYzUwNWE0OWEzOGY2ODQ=|1470107776|71c8fd91aa39bd196c69f862c2fc105d560851b8"',
    'login': '"YTU0MGYxNTFiNzE5NDBiNGEyMDBlMmViNDg5ZGE5NmE=|1470107793|8945f9abc33a05ab8755a2243f717472ef10daf8"',
    'z_c0': ('Mi4wQUVBQVpxbFZTUW9BRU1Bc2hXaEFDaGNBQUFCaEFsVk5vWjNIVndBRllzaURROF9rNHR6b0NqN0lfbC0tb0hxcDRB'
             '|1470107809|4398a685f707fad40550bb853b14c06c22c61d91'),
    'n_c': '1',
    'a_t': ('"2.0AEAAZqlVSQoXAAAAoZ3HVwBAAGapVUkKABDALIVoQAoXAAAAYQJVTaGdx1cABWLIg'
            '0PP5OLc6Ao-yP5fvqB6qeDX5Mej6T85JiurRRbkHDKRyEbDSQ=="'),
    's-q': 'zhang\'jia\'wei',
    's-i': '2',
    'sid': 'laul6c68',
    's-t': 'autocomplete',
    '__utmt': '1',
    '__utma': '51854390.646409182.1468901059.1470129298.1470133148.11',
    '__utmb': '51854390.2.10.1470133148',
    '__utmc': '51854390',
    '__utmz': ('51854390.1470133148.11.9.utmcsr=zhihu.com|utmccn=(referral)|'
               'utmcmd=referral|utmcct=/people/lu-jian-yao-qing-60/followees'),
    '__utmv': '51854390.100--|2=registration_date=20160726=1^3=entry_date=20160726=1',
}

ZHIHU_NAME = "//a[@class='name']/text()"
ZHIHU_LOCATION = "//span[@class='location item']/@title"
ZHIHU_GENDER = "//span[@class='item gender']/i/@class"
ZHIHU_EMPLOYMENT = "//span[@class='employment item']/@title"
ZHIHU_EMPLOYMENT_EXTRA = "//span[@class='position item']/@title"
ZHIHU_EDUCATION = "//span[@class='education item']/@title"
ZHIHU_EDUCATION_EXTRA = "//span[@class='education-extra item']/@title"
ZHIHU_FOLLOW = "//div[@class='zu-main-sidebar']//strong"
ZHIHU_AGREED = "//span[@class='zm-profile-header-user-agree']/strong/text()"
ZHIHU_THANKED = "//span[@class='zm-profile-header-user-thanks']/strong/text()"
ZHIHU_USER_INFO = "//span[@class='bio']/@title"
ZHIHU_USER_INTRO = "//span[@class='content']/text()"
ZHIHU_FOLLOWEE_URL = "//h2[@class='zm-list-content-title']/span/a/@href"
