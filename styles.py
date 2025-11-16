import flet as ft

PRIMARY_COLOR = ft.Colors.BLUE_600
BUTTON_RADIUS = 12
PADDING = 20

def responsive_text_size(page):
    w = page.width
    if w < 400:
        return 24
    elif w < 800:
        return 28
    return 32

def button_width(page):
    w = page.width
    if w < 400:
        return 250
    elif w < 800:
        return 300
    return 350
