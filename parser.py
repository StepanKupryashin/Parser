from bs4 import BeautifulSoup as bs
import bs4
import requests



class Parser:
    
    def __init__(self, url: str) -> None:
        self.url = url
        html = requests.get(self.url)
        self.html = html.text
        self.soup = bs(self.html, 'html.parser')

    
    def get_text(self, container, c_class: str, content: str = 'p') -> str:
        text = self.soup.find_all(container, {'class': c_class})
        if content == 'p':
            text = self.soup.find('p')
            return text.get_text()

        elif content == 'a':
            text = self.soup.find('a')
            return text.get_text()

    def get_texts(self, container = None, c_class = None, elements = 1, dot_container = None) -> list:
        if not dot_container:
            text = self.soup.find_all(container, {'class' : c_class})
            texts = []
            for i in text:
                if len(texts) < elements:
                    texts.append(i.getText())
            return texts
        else:
            text = self.soup.select(f'.{c_class} {dot_container}')
            texts = []
            for i in text:
                if len(texts) < elements:
                    texts.append(i.getText())
            return texts

        
    def get_all(self) -> str:
        return self.soup.find_all('div')
    
        
p = Parser('https://sinoptik.com.ru/погода-москва')

weather = p.get_texts(container = 'div', c_class='table__temp', elements=8)

weather = p.get_texts(container='div', c_class='weather__content_tab-temperature', elements=14, dot_container='b')

print(f'{weather[2]}, {weather[3]}')