import scrapy
import numpy as np
import pandas as pd

tabla=pd.read_csv(r'D:\Hacker Civics\Proyecto Migrador\Importacion - Productos\Tablas creadas\codigo_nc_scrapeo.csv',sep=',',dtype={'Product':str},engine="python", encoding="latin_1")

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = []
    for nrow in range(0,(tabla.shape[0])):
        start_urls.append('https://www.tariffnumber.com/2017/' + tabla.ix[nrow,0])

    def parse(self, response):
	
        if response.css("h1 span::text").extract_first() is None :
            if response.css("tr th.col-sm-10::text").extract_first() is not None :
                yield scrapy.Request(response.url[:-10]+response.css("td a.light::attr(href)").extract_first())
            else:
                yield scrapy.Request(response.url[0:-4])
        else:
            aux = response.css("section div.col-lg-12").extract()
            for n in range(0,len(aux)):
                if aux[n][56:57] == "C":
                    if aux[n][83] == "<":
                        yield { "0"+aux[n][82]: aux[n][125:-70] }
                    else:
                        yield { aux[n][83:85]: aux[n][127:-70] }
                #elif aux[n][56:57] == "P":
                #    yield { aux[n][86:90]: aux[n][132:-71] }
                #elif aux[n][56:57] == "S":
                #    yield { aux[n][82:88]: aux[n][139:-71] }
            #yield { response.css("h1 span::text").extract_first()[0:8]: response.css("h1 span::text").extract_first()[11:-26] } 					