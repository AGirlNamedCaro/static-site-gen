import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.TEXT)
        node3 = TextNode("World", TextType.TEXT)
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

    def test_repr(self):
        node = TextNode("Click here", TextType.LINK, url="http://example.com")
        expected_repr = "TextNode(Click here, link, http://example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_url_none(self):
        node = TextNode("Just text", TextType.TEXT)
        self.assertIsNone(node.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")

    def test_bold_empty(self):
        node = TextNode("", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "")

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")

    def test_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")

    def test_link(self):
        node = TextNode("Link text", TextType.LINK, url="http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertEqual(html_node.props, {"href": "http://example.com"})

    def test_image(self):
        node = TextNode(
            "Image alt text", TextType.IMAGE, url="http://example.com/image.png"
        )
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "http://example.com/image.png", "alt": "Image alt text"},
        )

    def test_link_empty_url(self):
        node = TextNode("Link text", TextType.LINK, url="")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertEqual(html_node.props, {"href": ""})

    def test_link_empty_text(self):
        node = TextNode("", TextType.LINK, url="http://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"href": "http://example.com"})

    def test_unsupported_text_type_raises(self):
        node = TextNode("Some text", "unsupported_type")
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(node)
        self.assertIn("Unsupported text type", str(context.exception))

    def test_image_empty_url(self):
        node = TextNode("Image alt text", TextType.IMAGE, url="")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "", "alt": "Image alt text"},
        )


if __name__ == "__main__":
    unittest.main()
