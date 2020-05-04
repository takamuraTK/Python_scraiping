import requests

from bs4 import BeautifulSoup

# encodingを設定して、HTMLを取得する。
res = requests.get('http://quotes.toscrape.com/')
res.encoding = 'UTF-8'

# bsのオブジェクトを作成する。
soup = BeautifulSoup(res.text, 'html.parser')

# title名の取得
title_text = soup.find('title').get_text()
# print(title_text)

# CSSセレクターで取得し、forループを実行する。
author_names = [n.get_text() for n in soup.select('div.quote small.author')]
# print(author_names)

# 要素を取得する際は、find系のメソッドを使う方法もあるが、要素が存在しないケースのハンドリングや
# 見た目がわかりやすいので、CSSセレクタを使うのが無難
# 以下のような分岐ケースを書く際も楽
def get_text():
    t = soup.select_one('div.hoge div.fuga div.piyo')
    if not t:
        return None
    return t.get_text()

# CSSセレクタの使い方として、
# :contains()を使うことで指定した文字列を含む要素を取得できる。
# ~を使うことで同じ階層の隣接ノードにアクセスできる。
tag_items = soup.select('h2:contains("Top Ten tags") ~ span')
# print(tag_items)

# get_text()はHTMLからテキストを摘出する。
# そのままだと改行コードを含めるのでそうしたくない場合はstrip=Trueとする。
html = '<div>\n   aaa\n  </div>'
soup_text = BeautifulSoup(html, 'html.parser')
text = soup_text.find('div').get_text()
# print(text)
text = soup_text.find('div').get_text(strip=True)
print(text)