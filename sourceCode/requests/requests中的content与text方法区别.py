"""
    resp.text返回的是Unicode型的数据。
    resp.content返回的是bytes型也就是二进制的数据。
    也就是说，如果你想取文本，可以通过r.text。
    如果想取图片，文件，则可以通过r.content。
  （resp.json()返回的是json格式数据）
"""
#  下载并保存一张图片
import requests

jpg_url = 'http://img2.niutuku.com/1312/0804/0804-niutuku.com-27840.jpg'
content = requests.get(jpg_url).content
with open('demo.jpg', 'wb') as fp:
    fp.write(content)
