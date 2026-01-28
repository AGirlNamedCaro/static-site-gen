import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Hello", TextType.PLAIN)
        node2 = TextNode("Hello", TextType.PLAIN)
        node3 = TextNode("World", TextType.PLAIN)
        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)

    def test_repr(self):
        node = TextNode("Click here", TextType.LINK, url="http://example.com")
        expected_repr = "TextNode(Click here, link, http://example.com)"
        self.assertEqual(repr(node), expected_repr)

    def test_url_none(self):
        node = TextNode("Just text", TextType.PLAIN)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
