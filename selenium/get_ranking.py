from selenium import webdriver
from PIL import Image

browser = webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/ranking/')

# 複数のClass名から要素を取得する
elem_rankingBox = browser.find_element_by_class_name('u_areaListRankingBox')
elem_title = elem_rankingBox.find_element_by_class_name('u_title')
elem_rank = elem_rankingBox.find_element_by_class_name('u_rankBox')
title = elem_title.text.split('\n')[1]
rank = elem_rank.text
print(title, rank)

# 全ての観光地を取得する
titles = []
elems_rankingBox = browser.find_elements_by_class_name('u_areaListRankingBox')
for elem in elems_rankingBox:
    title = elem.find_element_by_class_name('u_title').text.split('\n')[1]
    titles.append(title)
print(titles)

browser.quit()