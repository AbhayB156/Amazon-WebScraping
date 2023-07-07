import os
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from msedge.selenium_tools import Edge, EdgeOptions

# os.environ['PATH'] += r"C:/SeleniumDriver"
# webdriver.Edge(executable_path=r"C:/SeleniumDriver")
# browser = webdriver.Edge('F:\\za\\python\\Assistant\\msedgedriver.exe')
os.environ['PATH'] += r"C:/SeleniumDriver"
# driver = webdriver.Chrome()

def get_url(search_term):
    template = "https://www.amazon.in/s?k=ipad&ref=nb_sb_noss"
    search_term = search_term.replace(' ','*')
    url = template.format(search_term)
    url += '&page'
    return url

def extract_record(item):
   atag = item.h2.a
   description = atag.text.strip()
   url = 'https://www.amazon.com' + atag.get('href')
   try:
    price_parent = item.find('span','a-price')
    price = price_parent.find('span','a-offscreen').text
   except:
      return 
   try: 
    rating = item.i.text
    review_count = item.find('span',{'class':'a-size-base','dir':'auto'}).text 
   except AttributeError:
     rating = ''
     review_count = ''
     
   

   result = {description, price, rating, review_count, url}

   return result

def main(search_term):
  options = EdgeOptions()
  options.use_chronium = True
  driver = Edge(options=options)

  records = []
  url = get_url(search_term)

  for page in range(1,21):
    driver.get(url.format(page))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    result = soup.find_all('div',{'data-component-type': 's-search-result'})

    for item in result:
      record = extract_record(item)
      if record:
        records.append(record)
  driver.close()

  with open('results.csv','w',newline='',encoding='utf-8')  as f:
    writer = csv.writer(f)
    writer.writerow(['Description','Price','rating','ReviewCount','URL'])
    writer.writerows(records)

main('ipad')
# driver = webdriver.Chrome()

# options = EdgeOptions()
# # options.use_chromium = True
# driver = Edge(options=options)

# url = "http://www.amazon.com"
# driver.get(url)

# def get_url(search_term):
#     template = "https://www.amazon.in/s?k=ipad&ref=nb_sb_noss"
#     search_term = search_term.replace(' ','*')
#     return template.format(search_term)

# url = get_url('ipad')
# print(url)

# driver.get(url)

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# result = soup.find_all('div',{'data-component-type': 's-search-result'})
# len(result)

# item = result[0]
# atag = item.h2.a
# description = atag.text.strip()
# url = 'https://www.amazon.com' + atag.get('href')
# price_parent = item.find('span','a-price')
# price = price_parent.find('span','a-offscreen').text
# rating = item.i.text
# review_count = item.find('span',{'class':'a-size-base','dir':'auto'}).text

# # def extract_record(item):
# #    atag = item.h2.a
# #    description = atag.text.strip()
# #    url = 'https://www.amazon.com' + atag.get('href')
# #    try:
# #     price_parent = item.find('span','a-price')
# #     price = price_parent.find('span','a-offscreen').text
# #    except:
# #       return 
# #    try: 
# #     rating = item.i.text
# #     review_count = item.find('span',{'class':'a-size-base','dir':'auto'}).text 
# #    except AttributeError:
# #      rating = ''
# #      review_count = ''
     
   

# #    result = {description, price, rating, review_count, url}

# #    return result
# records = []
# results = soup.find_all('div', {'data-component': 's-search-result'})
# for item in results:
#   record = extract_record(item)
#   if record:
#     record.append(record)

# records[0]

# for row in records:
#   print(row[1])

# # def get_url(search_term):
# #     template = "https://www.amazon.in/s?k=ipad&ref=nb_sb_noss"
# #     search_term = search_term.replace(' ','*')
# #     url = template.format(search_term)
# #     url += '&page'
# #     return url