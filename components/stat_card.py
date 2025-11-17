# components/stat_card.py
import flet as ft

def create_stat_card(page: ft.Page, title: str, value: str, icon: str, icon_color: str = None):
    """
    Returns a theme-aware stat card.
    - page: current Flet page
    - title: card subtitle
    - value: main value text
    - icon: icon name from ft.Icons
    - icon_color: optional, overrides default color
    """
    # Determine colors based on theme
    if page.theme_mode == ft.ThemeMode.DARK:
        card_bg = ft.Colors.BLACK
        text_color = ft.Colors.WHITE
        subtitle_color = ft.Colors.WHITE70
        icon_color = icon_color or ft.Colors.BLUE_300
    else:
        card_bg = ft.Colors.WHITE
        text_color = ft.Colors.BLACK
        subtitle_color = ft.Colors.BLACK54
        icon_color = icon_color or ft.Colors.BLUE_700

    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Icon(icon, size=40, color=icon_color),
                        ft.Column(
                            controls=[
                                ft.Text(
                                    value,
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color=text_color,
                                ),
                                ft.Text(
                                    title,
                                    size=14,
                                    color=subtitle_color,
                                ),
                            ],
                            spacing=0,
                        ),
                    ],
                    spacing=15,
                ),
            ],
        ),
        bgcolor=card_bg,
        border_radius=10,
        padding=20,
        width=250,
    )
