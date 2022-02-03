from html.parser import HTMLParser
import urllib.request
import sys

tags = sys.argv[1].split(' ')

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        niz = data.split(']')
        for tag in tags:
            if niz[0].__contains__(tag):
                with open('C:\\Users\\pompeii\\Source\\Repos\\SpiritasX\\HTML__acs__parser\\HTML__acs__parser\\last.txt', 'r') as fp:
                    line = fp.readline()
                
                if line != data:
                    with open('C:\\Users\\pompeii\\Source\\Repos\\SpiritasX\\HTML__acs__parser\\HTML__acs__parser\\last.txt', 'w') as fp:
                        fp.write(data)

                    print(data)
                exit()

with urllib.request.urlopen('http://www.acs.uns.ac.rs/sr/node?page=0') as fp:
    data = fp.read()
    string = data.decode('utf8')

    parser = MyHTMLParser()
    parser.feed(string)
