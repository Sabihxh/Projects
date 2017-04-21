from lxml import html
import requests

import urllib

def something():
    page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.content)


    buyers = tree.xpath('//div[@title = "buyer-name"]/text()')
    price = tree.xpath('//span[@class="item-price"]/text()')


    print 'buyers: ', buyers
    print 'price: ', price
































# file = open('test.txt', 'w')

# for x in range(1, 11):
#     square = x*x
#     file.write('%s\n'% square)

# file.close()

# file = open('test.txt', 'r')

# a_list = file.read().split('\n')[:-1]

# print a_list

# file.close()