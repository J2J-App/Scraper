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
        
        #To shorten the data
        adapter["Region"] = adapter["Region"].replace("B) Outside Delhi Region", "OD")
        adapter["Region"] = adapter["Region"].replace("A) Delhi Region", "D")
        
        adapter["Round"] = adapter["Round"].replace("Round 1", "1")
        adapter["Round"] = adapter["Round"].replace("Round 2", "2")
        adapter["Round"] = adapter["Round"].replace("Round 3", "3")
        adapter["Round"] = adapter["Round"].replace("Round 4", "4")
        adapter["Round"] = adapter["Round"].replace("Round 5", "5")
        adapter["Round"] = adapter["Round"].replace("Upgradation Round", "U1")
        adapter["Round"] = adapter["Round"].replace("Upgradation Round 2", "U2")
        adapter["Round"] = adapter["Round"].replace("Upgradation 1", "U1")
        adapter["Round"] = adapter["Round"].replace("Upgradation 2", "U2")
        adapter["Round"] = adapter["Round"].replace("Spot Round", "S")
        
        adapter["Category"] = adapter["Category"].replace("General","GEN")
        adapter["Category"] = adapter["Category"].replace("Defence","-DEF")
        adapter["Category"] = adapter["Category"].replace(" ","")
        adapter["Category"] = adapter["Category"].replace("GENPWD","GEN-PWD")
        adapter["Category"] = adapter["Category"].replace("EWSPWD","EWS-PWD")
        adapter["Category"] = adapter["Category"].replace("OBCPWD","OBC-PWD")
        adapter["Category"] = adapter["Category"].replace("SCPWD","SC-PWD")
        adapter["Category"] = adapter["Category"].replace("STPWD","ST-PWD")
        
        # To replace "something bad happened" with "s2"
        adapter["Round"] = adapter["Round"].replace("something bad happened", "s2")
        
        return item
