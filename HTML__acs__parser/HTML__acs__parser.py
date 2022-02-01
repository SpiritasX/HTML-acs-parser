from html.parser import HTMLParser
import urllib.request
import sys

tags = sys.argv[1].split(' ')

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        niz = data.split(']')
        for tag in tags:
            if niz[0].__contains__(tag):
                print(data)
                exit()

parser = MyHTMLParser()
fp = urllib.request.urlopen('http://www.acs.uns.ac.rs/sr/node?page=0')
data = fp.read()
string = data.decode('utf8')
fp.close()
parser.feed(string)
