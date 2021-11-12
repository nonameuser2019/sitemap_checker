from bs4 import BeautifulSoup as bs
import requests


def get_html(url):
    response  = requests.get(url)
    assert response.status_code == 200
    return response


def get_url_count(html):
    soup = bs(html.text, 'html.parser')
    map_url_list = soup.find_all('loc')
    return len(map_url_list)


def parser(html):
    soup = bs(html.text, 'html.parser')
    map_url_list = soup.find_all('loc')
    count = 0
    for url in map_url_list:
        count += get_url_count(get_html(url.text))
    return count


def main():
    MAIN_URL = 'https://master.shop/sitemap.xml'
    count = parser(get_html(MAIN_URL))
    print(count)


if __name__ == '__main__':
    main()