from flask import Flask, request, render_template
import re
import requests
from lxml import html
app = Flask(__name__)


def getRealUrl(url):
    url='https://www.douyin.com/share/video/6515017468493171975'
    pattern = re.compile(r'http.*')
    urls = pattern.findall(url)
    response=requests.get(urls[0]).content
    selector = html.fromstring(response)
    hrefs=selector.xpath('/html/body/div/script[2]')
    data= hrefs[0].text
    pattern = re.compile(r'(?<=uri":")\w{32}')
    urls = pattern.findall(data)
    print urls[0]
    url='https://aweme.snssdk.com/aweme/v1/play/?video_id=%s'%urls[0]
    print url

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def jiexi():
    baseUrl = request.form['baseUrl']
    print(baseUrl)
    realUrl= getRealUrl(baseUrl)
    if realUrl:
        return render_template('index.html')
    return render_template('ok.html')


if __name__ == '__main__':
    app.run()