from scrapy.spider import Spider
from scrapy.http import FormRequest


class Search_PJ(Spider):
    name = "search_pj"
    allowed_domains = ["jurisprudencia.pj.gob.pe"]
    start_urls = [
        "http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-general.xhtml",
    ]

    def parse(self, response):
        return [FormRequest(url=self.start_urls[0],
            formdata={
                'formBusqueda:buNroExpediente': '000001-2013',
                'formBusqueda:j_idt30':'Buscar'},
            callback=self.after_search)]

    def after_search(self, response):
        if 'authentication failed' in response.body:
            self.log("Search failed", level=log.ERROR)
            print response
            return
        print response.body
