import scrapy
from ..items import Lstractor1Item


class Lstscrape1Spider(scrapy.Spider):
    name = 'lstscrape1'
    # allowed_domains = ['lstractorusa.com']
    # start_urls = ['http://lstractorusa.com/']

    def start_requests(self):
        url = r'https://lstractorusa.com/wp-admin/admin-ajax.php?lang=en&action=store_search&lat=40.73883&lng=-73.98153&max_results=25&search_radius=500'
        yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        items = Lstractor1Item()
        json_response = response.json()
        for i in json_response:
            items = {
                'StoreID':i.get('id', ''), 
                'StoreName':i.get('store', ''), 
                'Street':i.get('address', ''), 
                'City':i.get('city', ''), 
                'State':i.get('state', ''), 
                # 'StoreTiminings':''
                'Phone':i.get('phone',''),
                'Fax':i.get('fax',''),
                'Latitude':i.get('lat', ''),
                'Longitude':i.get('lng', ''),
                'ZipCode': i.get('zip',''),
                'URL': i.get('url',''),
                }
            yield items

