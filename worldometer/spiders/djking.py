import scrapy
from w3lib.url import add_or_replace_parameters

class DjkingSpider(scrapy.Spider):
    name = "djking"
    allowed_domains = ["https://widerdjs.in"]
    #start_urls = "https://soundcloud.com/search/list"
    
    url = "https://widerdjs.in/search/list"
    search = input("Enter the song Name: ")
    #https://widerdjs.in/search/list?q=ye+dil+h+muskil&search=all
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3'}
    params = {
        'q':search,
        'search': 'all'
    }
    
    url_s = add_or_replace_parameters(url,params)
    #print(url_s)
    
    def start_requests(self):
        yield scrapy.Request(url=self.url_s, callback=self.parse,headers=self.header)

    def parse(self, response):
        i = 1
        for song in response.xpath("//div[@class='vfx_video_details']"):
            name = song.xpath(".//h4/text()").get()
            print(f'{i}.{name}')
            i = i+1
        #print(response.body)
