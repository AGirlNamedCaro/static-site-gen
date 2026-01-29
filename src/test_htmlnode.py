import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )


def test_to_html_no_tag_raises(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode(None, [child_node])
    with self.assertRaises(ValueError):
        parent_node.to_html()


def test_to_html_no_children_raises(self):
    parent_node = ParentNode("div", [])
    with self.assertRaises(ValueError):
        parent_node.to_html()


def test_to_html_when_child_is_string(self):
    parent_node = ParentNode("p", ["This is a text child"])
    self.assertEqual(parent_node.to_html(), "<p>This is a text child</p>")
