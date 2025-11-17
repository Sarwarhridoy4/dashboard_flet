# models/menu_item.py
class MenuItem:
    """Menu item data structure"""
    
    def __init__(self, icon: str, label: str, page_class):
        self.icon = icon
        self.label = label
        self.page_class = page_class