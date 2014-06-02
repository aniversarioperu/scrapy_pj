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
        yield Request(self.target_url,  callback=self.parse)

    def parse(self, response):
        print "<br>response.headers", response.headers
        return [FormRequest.from_response(response,
                formdata={
                  'formBusqueda:buEspecialidadInput': 'Civil',
                  'formBusqueda:buAnioInput':'2013',
                    },
                dont_click=True,
                #cookies=[self.make_cookie(response)],
                callback = self.after_search)]

    def after_search(self, response):
        print "<br>response.headers", response.headers
        print "<br>response.body", response.body

    def make_cookie(self, response):
        tmp = response.headers['Set-Cookie']
        tmp = tmp.split(";")[0]
        tmp = tmp.split("=")[1]
        mycookies = []
        cookies = {}
        cookies['name'] = 'JSESSIONID'
        cookies['value'] = tmp
        cookies['domain'] = "jurisprudencia.pj.gob.pe"
        cookies['path'] = "/jurisprudenciaweb"
        """
        mycookies.append(cookies)
        tmp = {'name': '__utma',
                'value':'224540507.1467503965.1401198857.1401198857.1401222458.2',
                'domain': '.pj.gob.pe',
                'path': '/'}
        mycookies.append(tmp)
        tmp = {'name': '__utmz',
                'value':'224540507.1401222458.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=http://www.pj.gob.pe/',
                'domain': '.pj.gob.pe',
                'path': '/'}
        mycookies.append(tmp)

        cookies = {}
        cookies['name'] = 'JSESSIONID'
        tmp = tmp.split(";")
        cookies['value'] = tmp[0].split("=")[1]
        cookies['domain'] = "jurisprudencia.pj.gob.pe"
        cookies['path'] = "/jurisprudenciaweb"
        """
        print "cookies:->", cookies
        return cookies
        #return mycookies
