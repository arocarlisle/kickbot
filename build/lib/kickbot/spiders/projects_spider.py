from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from kickbot.items import ProjectItem


class ProjectSpider(CrawlSpider):

    name = 'project'
    allowed_domains = ['kickstarter.com']
    start_urls = ['https://www.kickstarter.com/discover/advanced?category_id=16&woe_id=0&sort=newest&seed=2451077&page=1']
    rules = (
        Rule(
            SgmlLinkExtractor(allow=r'\page=\d+'),
            follow=True,
            callback='parse_listing'
        ),
        Rule(
            SgmlLinkExtractor(allow=r'\category_id=\d+'),
            follow=True,
            callback='parse_listing'
        ),
        Rule(
            SgmlLinkExtractor(allow=r'/categories/'),
            callback='parse_listing'
        )
        # Rule(
        #     SgmlLinkExtractor(allow=r'/projects/'),
        #     callback='parse_listing'
        # )
    )

    def parse_listing(self, response):
        for item in response.xpath('//div[@class="project-card-content"]'):
            pro = ProjectItem()
            pro['url'] = item.xpath('.//h6/a/text()').extract()
            pro['title'] = item.xpath('.//h6/a/text()').extract()
            pro['description'] = item.xpath(
                './/p[@class="project-blurb"]/text()'
            ).extract()
            pro['author'] = item.xpath(
                './/p[@class="project-byline"]/text()'
            ).extract()
            pro['url_img'] = item.xpath('.//img/@src').extract()

            yield pro
