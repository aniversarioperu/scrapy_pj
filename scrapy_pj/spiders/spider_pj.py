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
formBusqueda=formBusqueda
formBusqueda:buCorte=
formBusqueda:j_idt25-value=j_idt26
formBusqueda:buEspecialidad=0
formBusqueda:buEspecialidadInput=-- Todos --
formBusqueda:buPretensionValue=
formBusqueda:buPretensionInput=
formBusqueda:buPalabraClaveValue=
formBusqueda:buPalabraClaveInput=
formBusqueda:buSala=0
formBusqueda:buSalaInput=-- Todos --
formBusqueda:buTipoRecurso=0
formBusqueda:buTipoRecursoInput=-- Todos --
formBusqueda:buTipoResolucion=0
formBusqueda:buTipoResolucionInput=-- Todos --
formBusqueda:buAnio=
formBusqueda:buAnioInput=-- Seleccione --
formBusqueda:txtBusqueda=
formBusqueda:buOrden=21
formBusqueda:buOrdenInput=Fecha Resolución
formBusqueda:buOrdenForma=ASC
formBusqueda:buOrdenFormaInput=Ascendente
formBusqueda:buPaginas=10
formBusqueda:buPaginasInput=10 resultados
javax.faces.ViewState=-697870706530378361:6617078509790886010
formBusqueda:repeat:0:j_idt158=formBusqueda:repeat:0:j_idt158
uuid=47cd6b37-8c7b-4cd0-b46a-adb4755bb161
"""
