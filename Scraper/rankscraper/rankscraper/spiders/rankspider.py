import scrapy
from rankscraper.items import RankscraperItem

class RankscraperSpider(scrapy.Spider):
    name = "rankscraper"
    allowed_domains = ["localhost:5500"]
    start_urls = ["http://localhost:5500/Offline_File/igdtuw-2023-cutoff.html"]

    custom_settings = {
        'FEEDS': {
            'igdtuw-2023-cutoff.csv': {'format': 'csv', 'overwrite': True},
        }
    }
    
    # custom_settings = {
    #     'FEEDS': {
    #         'igdtuw-2023-cutoff.json': {'format': 'json', 'overwrite': True},
    #     }
    # }

    def parse(self, response):
        sections = response.css("div.box-card.crs-box") # Get all the sections in the page
        for section in sections:
            main_heading = section.css("p.cp-clg-h::text").get() # Get the main heading of the section ( category of students )
            rounds = section.css("ul.tabs-nav li::text").getall() # Get the round names (round 1, round 2, etc.)
            tables = section.css("table.numeric-table.wm-table") # Get all the tables in the section

            for round_index, table in enumerate(tables):
                
                if round_index < len(rounds):
                    round_name = rounds[round_index]
                else:
                    round_name = "something bad happened" # If the number of rounds is less than the number of tables, detected spotround-2 
                
                rows = table.css("tr")
                region = None  # To store Delhi/Outside Delhi region

                for row in rows:
                    columns = row.css("td")

                    if len(columns) == 1:  # Check for region headers
                        region_text = columns[0].css("::text").get(default="").strip()
                        if "delhi" in region_text.lower():
                            region = region_text

                    elif len(columns) == 2:  # Check for branch & rank rows
                        branch = columns[0].css("::text").get(default="").strip()
                        rank = columns[1].css("::text").get(default="").strip()

                        if region and branch and rank:
                            rank_item = RankscraperItem()
                            rank_item["Category"] = main_heading
                            rank_item["Round"] = round_name
                            rank_item["Region"] = region
                            rank_item["Branch"] = branch
                            rank_item["Jee_Rank"] = rank

                            yield rank_item
