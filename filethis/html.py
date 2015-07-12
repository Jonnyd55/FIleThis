from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag, Comment


class SmartHTMLDocument:
    def __init__(self, html):
        self.bs = BeautifulSoup(html)
        # cache chunks
        self.chunks = None

    @property
    def body(self):
        return self.bs.html.body

    def find_all(self, *args, **kwargs):
        return self.bs.find_all(*args, attrs=kwargs)


    def delete(self, *args, **kwargs):
        for elem in self.bs.find_all(*args, attrs=kwargs):
            elem.extract()


    def getElementValue(self, _name, attr=None, **attrs):
        for elem in self.find_all(_name, **attrs):
            if attr is None:
                txt = elem.get_text().strip()
                if txt != "":
                    return txt
            elif elem[attr] is not None and len(elem[attr].strip()) > 0:
                return elem[attr].strip()
        return None


    def getText(self, node=None):
        text = ""
        node = node or self.bs.html
        if type(node) is not Tag:
            return text
        for child in node.descendants:
            if self.isTextNode(child):
                text += " " + child.string
        return text


    def getTextNodes(self):
        """
        Return all non-empty, non-js, non-css, non-comment text nodes
        """
        if self.bs.html is None:
            return []
        return [c for c in self.bs.html.descendants if self.isTextNode(c) and len(unicode(c).strip()) > 0]


    def isTextNode(self, node):
        istnode = type(node) is NavigableString
        istnode = istnode and (node.parent is None or node.parent.name not in [ 'script', 'style' ])
        return istnode and type(node) is not Comment


    def textChunks(self):
        if self.chunks is not None:
            return self.chunks

        self.chunks = []
        for child in self.bs.html.descendants:
            txt = self.getText(child).strip()
            if txt != "":
                self.chunks.append(txt)
        return self.chunks


    def __str__(self):
        if self.bs.html is None or self.bs.html.body is None:
            return ""
        return "".join([str(c) for c in self.bs.html.body.children])
