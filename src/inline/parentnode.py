from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None):
        if not tag:
            raise ValueError("Parent nodes must have a tag.")

        if not children:
            raise ValueError("Parent nodes must have at least one child node.")
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("parent nodes must have a tag.")
        
        if not self.children:
            raise ValueError("parent nodes must have at least one child node.")

        res = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            res += child.to_html()
        res += f"</{self.tag}>"

        return res
    
    def __repr__(self):
        return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"