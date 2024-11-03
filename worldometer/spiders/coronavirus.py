import scrapy


class CoronavirusSpider(scrapy.Spider):
    name = "coronavirus"
    allowed_domains = ["www.worldometers.info"]
    #start_urls = ["https://www.worldometers.info/coronavirus/"]
    start_link = 'https://www.worldometers.info/coronavirus/'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.3'}
    
    def start_requests(self):
        yield scrapy.Request(url=self.start_link,callback=self.parse,headers=self.header)

    def parse(self, response):
        for country in response.xpath("//td/a"):
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            #absolute_url = f"https://www.worldometers.info/coronavirus/{link}"
            absolute_url = response.urljoin(link)
            if link:
                yield response.follow(url=absolute_url, callback=self.pageparser,meta={'country_name':name})
            
            
           # yield{
                #"Country_name":name,
                #"Country_link":absolute_url
            #}
    def pageparser(self, response):
        coutry_name = response.request.meta['country_name']
        active_cases = response.xpath("(//div[@class='maincounter-number'])[1]/span/text()").get()
        death = response.xpath("(//div[@class='maincounter-number'])[2]/span/text()").get()
        recovered = response.xpath("(//div[@class='maincounter-number'])[3]/span/text()").get()
        
        yield{
            'country_name':coutry_name,
            'active_cases':active_cases,
            'death':death,
            'recovered':recovered
        }
        
