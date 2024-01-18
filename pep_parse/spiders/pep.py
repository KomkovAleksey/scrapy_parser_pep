import scrapy

from ..items import PepParseItem
from ..constants import START_URLS, PEP_SPIDER_NAME, ALLOWED_DOMAINS


class PepSpider(scrapy.Spider):
    """Паук для парсинга данных из документации PEP."""

    name = PEP_SPIDER_NAME
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def parse(self, response):
        """Парсинг ссылок документаций PEP."""
        for pep_link in response.css('tbody tr a[href^="pep-"]'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Парсинг данных из ссылок документаций PEP."""
        data = {
            'number': response.css('h1.page-title::text').get().split()[1],
            'name': response.css('h1.page-title::text').get().split(' – ')[1],
            'status': response.css('abbr::text').get(),
        }
        yield PepParseItem(data)
