import re

import scrapy

from maoyan.items import MaoyanItem


class Top100Spider(scrapy.Spider):
    name = 'top_100'
    allowed_domains = ['maoyan.com']
    start_urls = [f'https://maoyan.com/board/4?offset={i}' for i in range(0, 91, 10)]

    def parse(self, response):
        for entry in response.xpath('//dl[@class="board-wrapper"]/dd'):
            try:
                item = MaoyanItem()
                item['rank'] = entry.xpath('./i[contains(@class, "board-index")]/text()').get().strip()
                item['url'] = response.urljoin(entry.xpath('./a/@href').get())
                item['name_cn'] = entry.xpath('./a/@title').get().strip()
                score = entry.xpath('.//p[@class="score"]')
                item['score'] = score.xpath('./i[@class="integer"]/text()').get().strip() + \
                                score.xpath('./i[@class="fraction"]/text()').get().strip()
                yield scrapy.Request(url=item['url'], callback=self.parse_detail, meta={"item": item})
            except:
                pass

    def parse_detail(self, response):
        item = response.meta.get("item")

        try:
            brief = response.xpath('//div[@class="movie-brief-container"]')
            try:
                item["name_alt"] = brief.xpath('./div[contains(@class, "ename")]/text()').get()
            except:
                pass
            try:
                item["tag"] = list(map(str.strip, brief.xpath('(./ul/li)[1]/a/text()').getall()))
            except:
                pass
            try:
                item["region"] = [s.strip() for s in re.split(',|，', brief.xpath('(./ul/li)[2]/text()').get().split('/')[0])]
            except:
                pass
            try:
                item["length"] = re.sub(r'[^\x00-\x7F]+', '', brief.xpath('(./ul/li)[2]/text()').get().split('/')[1].strip())
            except:
                pass
            try:
                item["date"] = re.sub(r'[^\x00-\x7F]+', '', brief.xpath('(./ul/li)[3]/text()').get().strip()[:10])
            except:
                pass
        except:
            pass

        try:
            celebrity = response.xpath('//div[contains(@class, "tab-celebrity")]/div[@class="celebrity-container"]/div[@class="celebrity-group"]')
            item["celebrity"] = dict()
            for cele_grp in celebrity:
                cele_type = cele_grp.xpath('./div[@class="celebrity-type"]/text()').get().strip()
                cele_list = list(map(str.strip, cele_grp.xpath('./ul/li/div[@class="info"]/a/text()').getall()))
                item["celebrity"][cele_type] = cele_list
        except:
            pass

        try:
            box = response.xpath('//div[@class="film-mbox"]/div[@class="film-mbox-item"]')
            try:
                item["box_first_week"] = re.sub(r'[^\x00-\x7F]+', '', box[0].xpath('(./div)[1]/text()').get().strip())
            except:
                pass
            try:
                item["box_sum"] = re.sub(r'[^\x00-\x7F]+', '', box[1].xpath('(./div)[1]/text()').get().strip())
            except:
                pass
        except:
            pass

        try:
            honor = response.xpath('//div[@class="film-honors"]/div[@class="film-honors-item"]')
            try:
                item["honor_count"] = re.sub(r'[^\x00-\x7F]+', '', honor[0].xpath('(./div)[1]/text()').get().strip())
            except:
                pass
            try:
                item["nomination_count"] = re.sub(r'[^\x00-\x7F]+', '', honor[1].xpath('(./div)[1]/text()').get().strip())
            except:
                pass
        except:
            pass

        try:
            item["poster"] = response.xpath('//img[@class="avatar"]/@src').get()
        except:
            pass

        yield item