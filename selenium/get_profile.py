from selenium import webdriver
from PIL import Image
import pandas as pd

# browser = webdriver.Firefox()
browser = webdriver.Chrome()

browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

# 場所の指定(id指定)
elem_username = browser.find_element_by_id('username')
elem_password = browser.find_element_by_id('password')
elem_login_btn = browser.find_element_by_id('login-btn')
# 入力
elem_username.send_keys('imanishi')
elem_password.send_keys('kohei')
elem_login_btn.click()


# elementだと最初のth1つだけ取得し、elementsだと全部取得する。
elems_th = browser.find_elements_by_tag_name('th')
elems_td = browser.find_elements_by_tag_name('td')

# 複数取得されたthはリストとして格納されている。
for th in elems_th:
    print(th.text)

keys = []
for th in elems_th:
    keys.append(th.text)
print(keys)

values = []
for td in elems_td:
    values.append(td.text)
print(values)

# pandasでcsv出力する
df = pd.DataFrame()
df['項目'] = keys
df['値'] = values
print(df)

df.to_csv('講師情報.csv', index=False)

# 作業が終了したら閉じるようにする。
browser.quit()