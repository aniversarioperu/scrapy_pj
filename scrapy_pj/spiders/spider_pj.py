import json
import sys

from scrapy.spider import Spider
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.http.cookies import CookieJar


class Search_PJ(Spider):
    name = "search_pj"
    allowed_domains = ["jurisprudencia.pj.gob.pe"]
    target_url = "http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-resultado.xhtml"

    def start_requests(self):
        yield Request(self.target_url, cookies={'JSESSIONID': 'S99PW04VLX~AqMf5d1vHg+KP4rRCp0snqs5.a0c2e3f5-7bb5-3b43-be3f-aceabf94c2c1'
            }, callback=self.parse)

    def parse(self, response):
        print "<br>response.body", response.body
        return [FormRequest(url=self.target_url,
                formdata={
                  'formBusqueda:buEspecialidadInput': 'Civil',
                  'formBusqueda:buAnioInput':'2013',
                    },
                cookies=[{'name': 'JSESSIONID', 'value': 'S99PW04VLX~AqMf5d1vHg+KP4rRCp0snqs5.a0c2e3f5-7bb5-3b43-be3f-aceabf94c2c1'}],
                callback = self.after_search)]

    def after_search(self, response):
        print "<br>response.body", response.body

    def make_cookie(self, response):
        tmp = response.headers['Set-Cookie']
        cookies = {}
        cookies['name'] = 'JSESSIONID'
        tmp = tmp.split(";")
        cookies['value'] = tmp[0].split("=")[1]

        cookies = {}
        cookies['JSESSIONID'] = 'S99PW04VLX~zc+5l2lit5jlYB1zBNQvvYYy.86439558-da66-3a1b-af8b-0355e5d4e948'
        return cookies
