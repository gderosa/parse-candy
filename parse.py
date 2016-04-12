import re
import lxml.html
import urllib

IS_EPISODE = re.compile('Episodio (\d{1,3})')

parser = lxml.html.parse('input.html')

all_links = parser.findall('//a')  # list of lxml.html.HtmlElement objects

for idx, a in enumerate(all_links):
    matches = IS_EPISODE.findall(a.text)
    if matches:
        epn = matches[0]
        filename = re.sub(IS_EPISODE, 'Episodio ' + epn.zfill(3), a.text) + '.avi'
        filename = re.sub(r'[\\?]', '', filename)
        url = a.get('href')
        print(idx, filename, url, '...')
        urllib.urlretrieve(url, 'downloads/' + filename)
