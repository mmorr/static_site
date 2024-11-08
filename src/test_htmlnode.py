import unittest
from htmlnode import HTMLNode

class testHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode(tag="h1", value="This is an HTML header", props={"class": "header"})
        self.assertEqual(node.__repr__(), "HTMLNode(h1, This is an HTML header, None, {'class': 'header'})")

    def test_props(self):
        node = HTMLNode("h1", "This is an HTML header", None, {"class": "header"})
        self.assertEqual(node.props_to_html(), 'class="header"')

    def test_toprops2(self):
        node = HTMLNode("p", "This is a HTML paragraph", None, {"class": "paragraph"})
        self.assertEqual(node.props_to_html(), 'class="paragraph"')
