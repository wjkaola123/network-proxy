import requests
from lxml import etree

url = "http://www.xicidaili.com/nn"

headers = {
    'Host':
    'www.xicidaili.com',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language':
    'zh-CN,zh;q=0.9',
    'Accept-Encoding':
    'gzip, deflate',
    'Connection':
    'keep-alive',
    'Cache-Control':
    'max-age=0',
    'If-None-Match':
    'W/"e77aca8f99adbdc0fc2b9111c5e2ed71"',
    'Upgrade-Insecure-Requests':
    '1',
    'Cookie':
    '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWZjYTE1N2Y0ZTUzNDFmNWRmNWRlOGE3NWJmMDMzNGZiBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVVOeEhiVnNvZjNkWnJzOXpSZ2tNcnZvWnd5WjA3K056citxN2MxSmg1U0E9BjsARg%3D%3D--33ad2d676a4513567fda2b352a42458d96900ef9; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1514655698; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1514655698'
}

resp = requests.get(url, headers=headers)
selector = etree.HTML(resp.text)
ip_lst = list()
for i in range(2, 102):
    ip = selector.xpath(f'//*[@id="ip_list"]/tr[{i}]/td[2]/text()')
    port = selector.xpath(f'//*[@id="ip_list"]/tr[{i}]/td[3]/text()')
    print(ip, port)
    ip_lst.append((ip, port))
    print(len(ip_lst))




