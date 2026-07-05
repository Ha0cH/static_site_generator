class HTMLNode():
    def __init__(self,tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str, str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method must be implemented in child classes")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        res = ""
        for attr, val in self.props.items():
            res += f' {attr}="{val}"'
        return res
    
    def __repr__(self):
        return f'HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})'
    
    
