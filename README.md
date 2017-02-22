# 依赖
 - Python 3.5
 - requests
 - BeautifulSoup
 
# 功能
抓取
http://cn-proxy.com/
的国内代理信息（如需获取海外代理信息，请将 http://cn-proxy.com/ 替换为 http://cn-proxy.com/archives/218 ），函数返回一个列表，例如

```
['124.88.67.17:80',
 '124.88.67.21:83',
 '124.88.67.31:83',
 '124.88.67.21:843',
 '124.88.67.32:82',
 '124.88.67.32:80',
 '124.88.67.32:83',
 '124.88.67.18:80',
 '124.88.67.17:843',
 '124.88.67.18:82',
 '119.28.12.218:8888',
 '218.109.189.16:8888',
 '112.249.186.52:8888',
 '101.200.187.110:8090',
 '120.25.166.134:3128',
 '120.27.49.85:8090',
 '180.76.154.5:8888',
 '222.33.192.238:8118',
 '118.123.22.192:3128',
 '124.88.67.30:843',
 '101.4.136.34:81',
 '175.30.124.96:80',
 '125.88.74.122:81',
 '125.88.74.122:83',
 '125.88.74.122:85',
 '125.88.74.122:82',
 '58.221.38.170:8080',
 '123.57.225.102:8088',
 '14.152.93.79:8080',
 '120.27.113.72:8888',
 '183.95.80.165:8080',
 '112.249.41.57:8888',
 '203.90.144.145:82',
 '203.90.144.145:81',
 '101.53.101.172:9999',
 '203.90.144.145:83',
 '112.91.135.115:8080',
 '124.88.67.39:843',
 '124.88.67.16:80',
 '124.88.67.18:843',
 '124.88.67.16:843',
 '124.88.67.24:843',
 '124.88.67.31:82',
 '124.88.67.14:80',
 '124.88.67.16:81',
 '124.88.67.16:83',
 '124.88.67.14:843',
 '124.88.67.17:82',
 '124.88.67.24:83',
 '124.88.67.32:81',
 '124.88.67.24:80',
 '124.88.67.10:843',
 '124.88.67.23:843',
 '124.88.67.31:843',
 '124.88.67.32:843',
 '124.88.67.30:82',
 '124.88.67.14:83']
 ```



 # 使用方法
 
 由于该网站在墙外，如果运行的机器在墙内，需要自己配置一个代理，这里默认使用socks5代理，修改`"localhost", 60002`为你自己的代理信息即可。
 
 第二步，调用`proxies()`函数即可
 
 
 # 注意
 
 该网站的代理不稳定，过一段时间就失效，如果希望有长期稳定的代理，花钱才是王道。
