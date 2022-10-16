from unittest import result
from autoscraper import AutoScraper

amazon_url = "https://www.amazon.in/s?k=headphones"

wanted_list = ["₹799", "boAt Rockerz 370 On Ear Bluetooth Headphones with Upto 12 Hours Playtime, Cozy Padded Earcups and Bluetooth v5.0(Buoyant Black)", "30,149"]

scraper = AutoScraper()
result=scraper.build(amazon_url, wanted_list)
print(result)

scraper.get_result_similar(amazon_url,grouped=True)

scraper.set_rule_aliases({'rule_keg5':'Title', 'rule_ms55':'Price'})
scraper.keep_rules(['rule_keg5','rule_ms55'])
scraper.save('amazon-search')

results=scraper.get_result_similar('https://www.amazon.in/s?k=mi+phone+under+10000',group_by_alias=True)

results['Title']
results['Price']