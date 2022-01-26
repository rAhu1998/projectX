import scrapy 

class CarMaxSpider(scrapy.Spider):

	name = "carmax"
	start_urls = ['https://www.carmax.com/cars/bmw/330']
	

	def parse(self,response):
		for cars in	response.css('div.car-tile--content'):
			yield {
				'carName': cars.css('span.year-make::text').get(),
				'carModel': cars.css('span.model-trim::text').get(),
				'carPrice': cars.css('span.price::text').get().replace('$',''),
				'carMiles': cars.css('span.miles::text').get(),
				}