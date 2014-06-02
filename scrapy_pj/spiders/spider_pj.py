import json

from scrapy.spider import Spider
from scrapy.http import FormRequest
from scrapy.http.cookies import CookieJar


class Search_PJ(Spider):
    name = "search_pj"
    allowed_domains = ["jurisprudencia.pj.gob.pe"]
    start_urls = [
        "http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-resultado.xhtml",
    ]

    def parse(self, response):
        cookieJar = response.meta.setdefault('cookie_jar', CookieJar())
        cookieJar.extract_cookies(response, response.request)
        mycookie = cookieJar._cookies['jurisprudencia.pj.gob.pe']['/jurisprudenciaweb']['JSESSIONID']
        return [FormRequest(url=self.start_urls[0],
            formdata={
                'formBusqueda:buEspecialidadInput': 'Civil',
                'formBusqueda:buAnioInput':'2013',
                },
            callback=self.after_search)
            ]

    def after_search(self, response):
        if 'authentication failed' in response.body:
            self.log("Search failed", level=log.ERROR)
            print response
            return

        print response.body

