import requests 
from bs4 import BeautifulSoup
import json

instagram_url='https://www.instagram.com'
#profile_url='cati.puiu'
def get_followers_count(profile_url: str):
	response = requests.get(f"{instagram_url}/{profile_url}")
	print(response.status_code)
	if response.ok:
		html= response.text
		bs_html= BeautifulSoup(html)
		#print(response.text)
		#not server rendered
		#followers_a=bs_html('#react-root > section > main > div > ul > li:nth-child(2) > a')
		#print(followers_a)
		scripts=bs_html.select('script[type="application/ld+json"]')
		scripts_content=json.loads(scripts[0].text.strip())
		#print(json.dumps(scripts_content, indent=4, sort_keys=True))
		#print(scripts[0].text.strip())
		#print(bs_html)#script/JSON
		#print(len(scripts))
		#STRIP=he strip() method returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).
		main_entity_of_page= scripts_content['mainEntityofPage']
		interaction_statistic=main_entity_of_page['interactionStatistic']
		followers_count=interaction_statistic['userInteractionCount']
		#print(followers_count)
		return followers_count


profiles=['cati.puiu','2dorpetre']
for profile in profiles:
	count=get_followers_count(profile)
	print(f"{profile} has {count} followers_count")