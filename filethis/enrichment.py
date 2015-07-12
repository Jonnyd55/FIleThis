from embedly import Embedly
from filethis.settings import EMBEDLY_KEY
from filethis.html import SmartHTMLDocument
from filethis.text import Summarizer

def enrich(url, title):
    client = Embedly(EMBEDLY_KEY)
    data = client.extract(url)
    data['text'] = SmartHTMLDocument("<html><body>%s</body></html>" % data['content']).getText().strip()
    data['summary'] = Summarizer(data['text'], title).summary()
    return data
