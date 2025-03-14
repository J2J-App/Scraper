# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class RankscraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)

        #To remove /n from data
        adapter["Region"] = adapter["Region"].replace("\n", "")
        adapter["Branch"] = adapter["Branch"].replace("\n", "")
        adapter["Jee_Rank"] = adapter["Jee_Rank"].replace("\n", "")
        
        #To remove extra spaces from data
        adapter["Region"] = adapter["Region"].strip()
        adapter["Branch"] = adapter["Branch"].strip()
        adapter["Jee_Rank"] = adapter["Jee_Rank"].strip()
        adapter["Round"] = adapter["Round"].strip()
        adapter["Category"] = adapter["Category"].strip()
        
        #To remove extra spaces from in between of data
        adapter["Region"] = adapter["Region"].replace("                                                                                        ", " ")
        adapter["Branch"] = adapter["Branch"].replace("                                                                                    ", " ")
        adapter["Jee_Rank"] = adapter["Jee_Rank"].replace("                                                                                    ", " ")
        
        return item
