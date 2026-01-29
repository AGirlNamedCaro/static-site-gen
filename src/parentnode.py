from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag to convert to HTML")
        if not self.children:
            raise ValueError("ParentNode must have children to convert to HTML")
        props_str = self.props_to_html()
        children_html = "".join(
            child.to_html() if isinstance(child, HTMLNode) else str(child)
            for child in self.children
        )
        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
