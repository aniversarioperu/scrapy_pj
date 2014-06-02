import json

from scrapy.spider import Spider
from scrapy.http import FormRequest
from scrapy.http import Request
from scrapy.http.cookies import CookieJar


class Search_PJ(Spider):
    name = "search_pj"
    allowed_domains = ["jurisprudencia.pj.gob.pe"]
    target_url = "http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-resultado.xhtml"

    def start_requests(self):
        #cookieJar = response.meta.setdefault('cookie_jar', CookieJar())
        #cookieJar.extract_cookies(response, response.request)
        #mycookie = cookieJar._cookies['jurisprudencia.pj.gob.pe']['/jurisprudenciaweb']['JSESSIONID']
        #print "my cookie:\t", mycookie
        yield Request(self.target_url, cookies={'JSESSIONID': 'S99PW04VLX~zc+5l2lit5jlYB1zBNQvvYYy.86439558-da66-3a1b-af8b-0355e5d4e948'},
            callback=self.parse)

        """
        cookieJar.add_cookie_header(request)
        print "<br><br>---<br>"
        print "request.url,", request.url, "<br>"
        print "request.callback,", request.callback, "<br>"
        print "request.method,", request.method, "<br>"
        print "request.meta,", request.meta, "<br>"
        print "request.body,", request.body, "<br>"
        print "request.headers,", request.headers, "<br>"
        print "request.cookies,", request.cookies, "<br>"
        print "request.encoding,", request.encoding, "<br>"
        print "request.priority,", request.priority, "<br>"
        print "request.dont_filter,", request.dont_filter, "<br>"
        print "request.errback,", request.errback, "<br>"
        """

    def parse(self, response):
        if 'authentication failed' in response.body:
            self.log("Search failed", level=log.ERROR)
            print response
            return

        print response.headers, "<br><br>"
        print response.meta, "<br><br>"
        print response.body, "<br><br>"

        return [FormRequest(url=self.start_urls[0],
            formdata={
                 'formBusqueda:buEspecialidadInput': 'Civil',
                 'formBusqueda:buAnioInput':'2013',
                },
            cookies=[{'name':'JSESSIONID', 'value': 'S99PW04VLX~zc+5l2lit5jlYB1zBNQvvYYy.86439558-da66-3a1b-af8b-0355e5d4e948'}],
            callback=self.after_search)]

    def after_search(self, response):
        if 'authentication failed' in response.body:
            self.log("Search failed", level=log.ERROR)
            print response
            return

        print response.headers, "<br><br>"
        print response.meta, "<br><br>"
        print response.body, "<br><br>"
