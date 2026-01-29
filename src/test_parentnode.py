import unittest
from parentnode import ParentNode
from leafnode import LeafNode


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
