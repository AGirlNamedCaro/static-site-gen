import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_value_raises(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_no_tag_returns_value(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_multiple_props(self):
        node = LeafNode(
            "a", "Click here", props={"href": "http://example.com", "target": "_blank"}
        )
        expected_html = '<a href="http://example.com" target="_blank">Click here</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_leaf_repr(self):
        node = LeafNode("span", "Sample text", {"class": "highlight"})
        expected_repr = (
            "LeafNode(tag=span, value=Sample text, props={'class': 'highlight'})"
        )
        self.assertEqual(repr(node), expected_repr)

    def test_leaf_no_props(self):
        node = LeafNode("div", "Content")
        expected_html = "<div>Content</div>"
        self.assertEqual(node.to_html(), expected_html)
