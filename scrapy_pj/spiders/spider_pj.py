import json

from scrapy.spider import Spider
from scrapy.http import FormRequest
from scrapy.http.cookies import CookieJar


class Search_PJ(Spider):
    name = "search_pj"
    allowed_domains = ["jurisprudencia.pj.gob.pe"]
    start_urls = [
        "http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-general.xhtml",
    ]

    def parse(self, response):
        print response.headers
        cookieJar = response.meta.setdefault('cookie_jar', CookieJar())
        cookieJar.extract_cookies(response, response.request)
        request = FormRequest(url=self.start_urls[0],
            formdata={
                'formBusqueda:buNoExpediente': '000001-2013',
                },
            #cookies={'JSESSIONID': str(mycookie.value)},
            meta={'dont_merge_cookies': True, 'cookie_jar': cookieJar},
            callback=self.after_search)
        print "<br><br>---<br>"
        print request.url, "<br>"
        print request.callback, "<br>"
        print request.method, "<br>"
        print request.meta, "<br>"
        print request.body, "<br>"
        print request.headers, "<br>"
        print request.cookies, "<br>"
        print request.encoding, "<br>"
        print request.priority, "<br>"
        print request.dont_filter, "<br>"
        print request.errback, "<br>"
        cookieJar.add_cookie_header(request)
        yield request
            

    def after_search(self, response):
        if 'authentication failed' in response.body:
            self.log("Search failed", level=log.ERROR)
            print response
            return

        print response.body

