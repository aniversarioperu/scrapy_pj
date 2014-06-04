import json
import re
import sys

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import FormRequest
from scrapy.http import Request


class Search_PJ(Spider):
    name = "search_pj"
    allowed_domains = ["jurisprudencia.pj.gob.pe"]
    target_url = "http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-general.xhtml"

    def start_requests(self):
        yield Request(self.target_url,  callback=self.parse)

    def parse(self, response):
        return [FormRequest.from_response(
            response,
            formdata={
                'formBusqueda': 'formBusqueda',
                'formBusqueda:txtBusqueda': 'Ingrese el texto a buscar',
                'formBusqueda:cmbCorte': '',
                'formBusqueda:buNroExpediente': '000001-2013',
                'javax.faces.source': 'formBusqueda:j_idt30',
                'forward': 'buscar',
                'formBusqueda:j_idt32': '21',
                'formBusqueda:j_idt33': 'ASC',
                'org.richfaces.ajax.component': 'formBusqueda:j_idt30',
            },
            clickdata={'id': 'formBusqueda:j_idt30', },
            callback=self.after_search
        )]

    def after_search(self, response):
        sel = Selector(response)
        ls = sel.xpath('//input[starts-with(@value, "Ver Resolu")]').extract()
        patt = "(formBusqueda:repeat:[0-9]+:j_idt[0-9]+).+uuid\W+((\w+-)+\w+)"
        for l in ls:
            res = re.search(patt, l).groups()
            if res:
                idt = res[0]
                uuid = res[1]
                print idt, uuid, "<br>"
        #print "<br>response.body", response.body



# post request to download PDF file
"""
        formBusqueda=formBusqueda&formBusqueda%3AbuCorte=&formBusqueda%3Aj_idt25-value=j_idt26&formBusqueda%3AbuEspecialidad=0&formBusqueda%3AbuEspecialidadInput=--+Todos+--&formBusqueda%3AbuPretensionValue=&formBusqueda%3AbuPretensionInput=&formBusqueda%3AbuPalabraClaveValue=&formBusqueda%3AbuPalabraClaveInput=&formBusqueda%3AbuSala=0&formBusqueda%3AbuSalaInput=--+Todos+--&formBusqueda%3AbuTipoRecurso=0&formBusqueda%3AbuTipoRecursoInput=--+Todos+--&formBusqueda%3AbuTipoResolucion=0&formBusqueda%3AbuTipoResolucionInput=--+Todos+--&formBusqueda%3AbuAnio=&formBusqueda%3AbuAnioInput=--+Seleccione+--&formBusqueda%3AtxtBusqueda=&formBusqueda%3AbuOrden=21&formBusqueda%3AbuOrdenInput=Fecha+Resoluci%C3%B3n&formBusqueda%3AbuOrdenForma=ASC&formBusqueda%3AbuOrdenFormaInput=Ascendente&formBusqueda%3AbuPaginas=10&formBusqueda%3AbuPaginasInput=10+resultados&javax.faces.ViewState=-697870706530378361%3A6617078509790886010&formBusqueda%3Arepeat%3A0%3Aj_idt158=formBusqueda%3Arepeat%3A0%3Aj_idt158&uuid=47cd6b37-8c7b-4cd0-b46a-adb4755bb161
"""
