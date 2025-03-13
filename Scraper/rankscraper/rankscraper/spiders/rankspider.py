import scrapy


class RankscraperSpider(scrapy.Spider):
    name = "rankscraper"
    allowed_domains = ["localhost:5500"]
    start_urls = ["http://localhost:5500/Offline_File/nsut-2024-cutoff.html"]

    # custom_settings = {
    #     'FEEDS': {
    #         'nsut-2024-cutoff.csv': {'format': 'csv', 'overwrite': True},
    #     }
    # }

    custom_settings = {
        'FEEDS': {
            'nsut-2024-cutoff.json': {'format': 'json', 'overwrite': True},
        }
    }


    def parse(self, response):
        tables = response.css("table.numeric-table.wm-table")
        region = None
        
        for table in tables:
            rows = table.css("tr")
            for row in rows:
                columns = row.css("td")
                
                if len(columns) == 1:  
                    region = columns[0].css("::text").get().strip()
                elif len(columns) == 2:
                    branch = columns[0].css("::text").get().strip()
                    rank = columns[1].css("::text").get().strip()
                    
                    if region and branch and rank:
                        yield {
                            "Region": region,
                            "Branch": branch,
                            "Jee Rank": rank,
                        }
