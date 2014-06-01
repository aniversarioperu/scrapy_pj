# Scrapy settings for scrapy_pj project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_pj'

SPIDER_MODULES = ['scrapy_pj.spiders']
NEWSPIDER_MODULE = 'scrapy_pj.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_pj (+http://www.yourdomain.com)'

# More comprehensive list can be found at 
# http://techpatterns.com/forums/about304.html
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]

HTTP_PROXY = "http://127.0.0.1:8123"

DOWNLOADER_MIDDLEWARES = {
         'scrapy_pj.middlewares.RandomUserAgentMiddleware': 400,
         'scrapy_pj.middlewares.ProxyMiddleware': 410,
         'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
         'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 'COOKIES_ENABLED',
    # Disable compression middleware, so the actual HTML pages are cached
}
