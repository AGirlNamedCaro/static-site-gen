import unittest
from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="div", props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected_html = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="div")
        expected_html = ""
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="div", props={})
        expected_html = ""
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_special_characters(self):
        node = HTMLNode(
            tag="img", props={"alt": 'A "special" image', "src": "image&photo.jpg"}
        )
        expected_html = ' alt="A "special" image" src="image&photo.jpg"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="input", props={"type": "text"})
        expected_html = ' type="text"'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_props_to_html_empty_value_prop(self):
        node = HTMLNode(tag="div", props={"data-id": ""})
        expected_html = ' data-id=""'
        self.assertEqual(node.props_to_html(), expected_html)

    def test_repr(self):
        node = HTMLNode(
            tag="a",
            value="Click here",
            children=[],
            props={"href": "https://www.example.com"},
        )
        expected_repr = "HTMLNode(tag=a, value=Click here, children=[], props={'href': 'https://www.example.com'})"
        self.assertEqual(repr(node), expected_repr)

    def test_repr_no_attributes(self):
        node = HTMLNode()
        expected_repr = "HTMLNode(tag=None, value=None, children=None, props=None)"
        self.assertEqual(repr(node), expected_repr)
