import json
import sys

from scrapy.spider import Spider
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.http.cookies import CookieJar


class Search_PJ(Spider):
    def __init__(self):
        self.mycookies = ''

    name = "search_pj"
    allowed_domains = ["jurisprudencia.pj.gob.pe"]
    start_urls = [
        "http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-resultado.xhtml",
    ]

    def parse(self, response):
        self.mycookies = self.make_cookie(response)
        print self.mycookies
        return [FormRequest(url=self.start_urls[0],
                callback = self.after_search,
                formdata={
                    'formBusqueda:buNoExpediente': '000001-2013',
                    },
                meta={'dont_merge_cookies': True},
                cookies=self.mycookies,
        )]
        print response.headers
        cookieJar = response.meta.setdefault('cookie_jar', CookieJar())
        cookieJar.extract_cookies(response, response.request)
        request = FormRequest(url=self.start_urls[0],
            formdata={
                 'formBusqueda:buEspecialidadInput': 'Civil',
                 'formBusqueda:buAnioInput':'2013',
                },
            cookies=[{'name':'JSESSIONID', 'value': 'S99PW04VLX~zc+5l2lit5jlYB1zBNQvvYYy.86439558-da66-3a1b-af8b-0355e5d4e948'}],
            callback=self.after_search)]

    def after_search(self, response):
        print "<br>response.body", response.body
        cookieJar = response.meta.setdefault('cookie_jar', CookieJar())
        cookieJar.extract_cookies(response, response.request)
        request = FormRequest(url=self.start_urls[0],
                callback = self.after_search2,
                formdata={
                    'formBusqueda:buNoExpediente': '000001-2013',
                    },
                meta={'dont_merge_cookies': True},
                cookies=self.make_cookie(response),
        )
        print self.mycookies
        cookieJar.add_cookie_header(request)
        print "<br>request.header", request.headers
        yield request

    def after_search2(self, response):
        print "<br>response.body", response.body

    def make_cookie(self, response):
        tmp = response.headers['Set-Cookie']
        cookies = {}
        cookies['name'] = 'JSESSIONID'
        tmp = tmp.split(";")
        cookies['value'] = tmp[0].split("=")[1]

        cookies = {}
        cookies['JSESSIONID'] = 'S99PW04VLX~UYf3XwHQxMpDxXlX7E5U0LhI.a0c2e3f5-7bb5-3b43-be3f-aceabf94c2c1'
        return cookies
