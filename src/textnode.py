from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"

class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = TextType(text_type)
        if url and url.startswith('https://'):    
            self.url = url
        else: self.url = None

    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"