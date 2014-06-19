# About
The Justice Department in Peru (*Poder Judicial*, PJ) has released
thousands of veredicts from the Supreme Court. All are in PDF
format (images, not text). The only way to download is by using their website
and download one by one, which is far from efficient. They don't offer
downloads of documents in batches of more than 5.

This project aims to be an efficient way to download the documents from the PJ
website by scrapping their website using **scrapy**.

This software executes the steps 1 to 5:

1. Go here <http://jurisprudencia.pj.gob.pe/jurisprudenciaweb/faces/page/resolucion-busqueda-general.xhtml>
2. POST to No Expediente: '000001-2013'
3. GET results. Get **idt** and **uuid** values for each result (from button 
  "Ver Resolución").
4. For each result, replace the **idt** and **uuid** in **their** javascript
  function to get the PDF:
5. ``mojarra.jsfcljs(document.getElementById('formBusqueda'),{'formBusqueda:repeat:0:j_idt158':'formBusqueda:repeat:0:j_idt158','uuid':'47cd6b37-8c7b-4cd0-b46a-adb4755bb161'},'');``
6. OCR PDF
7. add to database


# Install Scrapy
Assuming that you have Python 2.7+ isntalled in your computer:
```bash
pip install scrapy
```

# Usage of Scrapy
* Cookie handler.
* Proxy middleware.
* User agent middleware.

# Clone this repository
```bash
git clone https://github.com/aniversarioperu/scrapy_pj.git
```

# Run the software
Replace the "expediente" number for the one(s) that your wish to download:
```bash
scrapy crawl search_pj -a expediente=00001-2013 -t json -o output.json
```
Expected output is a bunch of PDF files downloaded to current folder:

```
Resolucion_000001-2013-1390676516593.pdf
Resolucion_000001-2013-1390773912770.pdf
Resolucion_000001-2013-20140225102936000838852.pdf
Resolucion_000001-2013-20140227102906000571555.pdf
Resolucion_000001-2013-20140228170931000865573.pdf
Resolucion_000001-2013-20140304171117000584898.pdf
Resolucion_000001-2013-20140310115239000895619.pdf
Resolucion_000001-2013-20140311151759000566176.pdf
```

# Set up Tor
[Optional] If using Ubuntu, add this line to ``/etc/apt/sources.list``:

```bash
deb http://deb.torproject.org/torproject.org saucy main
```

Then do:

```bash
gpg --keyserver keys.gnupg.net --recv 886DDD89
gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | sudo apt-key add -
apt-get update
apt-get install deb.torproject.org-keyring
apt-get install tor
```
More info here <https://www.torproject.org/docs/tor-doc-unix.html.en#using>

Install polipo, more info [here](http://pkmishra.github.io/blog/2013/03/18/how-to-run-scrapy-with-TOR-and-multiple-browser-agents-part-1-mac/).
