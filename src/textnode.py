from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
        

    def __eq__(self, other):
        if self.url and other.url:
            if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
                return True
            else:
                return False
        elif self.text == other.text and self.text_type == other.text_type:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"