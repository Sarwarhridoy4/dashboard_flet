def screen_size(page):
    w = page.width
    if w < 500:
        return "mobile"
    elif w < 900:
        return "tablet"
    return "desktop"
