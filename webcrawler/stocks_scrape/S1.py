from bs4 import BeautifulSoup as soup
import requests


def get_url_soup(alink):
    open_url = requests.get(alink)
    read_url = open_url.text
    return soup(read_url, 'html.parser')

def main():
    main_page_html = get_url_soup('https://uk.finance.yahoo.com/quote/%5EFTSE?p=%5EFTSE')
    header_html = main_page_html.find('ul', {'class': 'Carousel-Slider Pos(r) Whs(nw)'})
    for li in header_html.find_all('li'):
        url_html = li.find('a', {'class': 'Fz(s) Ell Fw(b) C($actionBlue)'})
        actual_compnay_html = get_url_soup('https://uk.finance.yahoo.com%s' % url_html.get('href'))
        tree1 = actual_compnay_html.find('div', {'id': 'quote-summary'})
        tree2 = tree1.find_all('tr'), {'class': 'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($lightGray) H(36px) '}
        print tree2

main()
