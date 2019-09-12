import scrapy

from cleaning import clean_price


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = [
        'https://www.autotrader.co.uk/car-search?advertising-location=at_cars&search-target=usedcars&is-quick-search=TRUE&postcode=WC2N+5DU&make=TESLA&price-search-type=total-price'
    ]

    def parse(self, response):
        for car_div in response.css('.search-listing'):
            link = car_div.css('.listing-title a.listing-fpa-link')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()

            raw_price = car_div.css('.vehicle-price::text').get()

            price = raw_price and clean_price(raw_price) or None

            img_urls = car_div.css('.listing-main-image img::attr(src)').getall()

            yield {
                'title': title,
                'href': response.urljoin(href),
                'price_eur': price,
                'imgs': [response.urljoin(img) for img in img_urls],
            }

            # TODO. Скачать данные со второй страницы выдачи, третьей и далее. Пагинация
