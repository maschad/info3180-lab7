import requests
import BeautifulSoup
import urlparse
import os
from urllib2 import urlopen
from urllib import urlretrieve

url = "http://www.amazon.com/gp/product/1783551623"
result = requests.get(url)
soup = BeautifulSoup.BeautifulSoup(result.text)
og_image = (soup.find('meta', property='og:image') or
                    soup.find('meta', attrs={'name': 'og:image'}))
if og_image and og_image['content']:
    print og_image['content']

thumbnail_spec = soup.find('link', rel='image_src')
if thumbnail_spec and thumbnail_spec['href']:
    print thumbnail_spec['href']

def image_dem():
    image = """<img src="%s"><br />"""
    for img in soup.findAll("img", src=True):
       if "sprite" not in img["src"]:
           image_url = urlparse.urljoin(url, img["src"])
           filename = img["src"].split("/")[-1]
           outpath = os.path.join('test/', filename)
           urlretrieve(image_url, outpath)

image_dem()
