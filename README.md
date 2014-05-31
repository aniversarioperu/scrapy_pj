PJ has released thousands for veredicts from the Supreme Court. All are in PDF
format (images, not text).

Scrape (scrapy? beautifulSoup?) to download documents from the Peruvian
Judicial System:

* POST to No Expediente: '000001-2013'
  <http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-general.xhtml>
* GET results. Get **idt** and **uuid** values for each result (from button
  "Ver Resolución").
* use **their** javascript function to get the PDF:

    * ``mojarra.jsfcljs(document.getElementById('formBusqueda'),{'formBusqueda:repeat:0:j_idt158':'formBusqueda:repeat:0:j_idt158','uuid':'47cd6b37-8c7b-4cd0-b46a-adb4755bb161'},'');``

* OCR PDF
* profit
