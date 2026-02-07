class HTMLNode:
    '''
        - tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        - value - A string representing the value of the HTML tag (e.g. the text 
            inside a paragraph)
        - children - A list of HTMLNode objects representing the children of this node
        - props - A dictionary of key-value pairs representing the attributes of the HTML 
            tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    '''
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        ret_str = ""
        if self.props is None:
            return ret_str
        
        for prop in self.props:
            ret_str += f' {prop}="{self.props[prop]}"'
        return ret_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value not found.")
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        
        children_str = ""
        for child in self.children:
            children_str += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_str}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
