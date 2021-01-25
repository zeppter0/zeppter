from bs4 import BeautifulSoup

from admin_dashboard.models import Book

class Html(object):
    def __init__(self,html):
        self.html = html
    def content(self):
        parsed_html = BeautifulSoup(self.html)
        s = ""
        frame = parsed_html.body.find('div', attrs={'class': 'col-md-9 col-md-push-3'})

        for f in frame.select('img'):
            f.extract()
        for f in frame.select('h3'):
            f.extract()

        for f in frame.select('h1'):
            f.extract()

        for f in frame.select('div', ):
            f.extract()
        return frame.text

    def title(self):
        parsed_html = BeautifulSoup(self.html)
        s = ""
        frame = parsed_html.body.find('div', attrs={'class': 'col-md-9 col-md-push-3'})
        for f in frame.select('p'):
            f.extract()

        for f in frame.select('img'):
            f.extract()
        for f in frame.select('h3'):
            f.extract()



        for f in frame.select('div', ):
            f.extract()
        print(frame.text)
        return frame.text

    def description(self):
        parsed_html = BeautifulSoup(self.html)
        s = ""
        frame = parsed_html.body.find('div', attrs={'class': 'col-md-9 col-md-push-3'})
        for f in frame.select('h1'):
            f.extract()


        for f in frame.select('img'):
            f.extract()
        for f in frame.select('h3'):
            f.extract()

        for f in frame.select('div', ):
            f.extract()
        data = frame.text

        data = data[:400]
        return data
    def image(self):
        parsed_html = BeautifulSoup(self.html)
        s = ""
        frame = parsed_html.body.find('div', attrs={'class': 'col-md-9 col-md-push-3'})
        for f in frame.select('h1'):
            f.extract()
        for f in frame.select('p'):
            f.extract()


        for f in frame.select('h3'):
            f.extract()

        for f in frame.select('div', ):
            f.extract()


        return frame.img['src']
    def is_image(self):
        parsed_html = BeautifulSoup(self.html)
        s = ""
        frame = parsed_html.body.find('div', attrs={'class': 'col-md-9 col-md-push-3'})
        for f in frame.select('h1'):
            f.extract()
        for f in frame.select('p'):
            f.extract()

        for f in frame.select('h3'):
            f.extract()

        for f in frame.select('div', ):
            f.extract()



        return frame.img.name

