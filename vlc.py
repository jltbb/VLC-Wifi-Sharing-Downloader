import requests

from multiprocessing import Pool

import urllib.parse            
def dl(url):
    r = requests.get(url)
    fn = urllib.parse.unquote(url.split('/')[-1])
    with open(f'{fn}', 'wb') as f:
        f.write(r.content)

a = []                                     
for x in req.split('<a href="'):

    if '<divstyle=' in x.split('"')[0].split('#')[0].replace(' ', '') or len(x.split('"')[0].split('#')[0].replace(' ', '')) == 0:
        continue
    fn = urllib.parse.unquote(x.split('"')[0].split('#')[0].replace(' ', '').split('/')[-1])
    a.append('http://10.9.20.108/' + x.split('"')[0].split('#')[0].replace(' ', ''))

if __name__ == '__main__':
    with Pool(6) as p:
        print(p.map(dl, a))