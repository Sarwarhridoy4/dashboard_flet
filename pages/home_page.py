import flet as ft
from components.stat_card import create_stat_card

class HomePage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 30
        self.expand = True

        # Build initial content
        self._build_content()

        # Listen to external theme changes
        self.page.on_theme_changed = lambda e: self.update_theme()

    # ------------------------------------------------------------
    # Build content based on current theme
    # ------------------------------------------------------------
    def _build_content(self):
        theme = self.page.theme_mode

        # Colors based on theme
        if theme == ft.ThemeMode.DARK:
            bg_color = ft.Colors.BLACK87
            text_color = ft.Colors.WHITE
            card_bg_default = ft.Colors.BLACK
        else:
            bg_color = ft.Colors.WHITE
            text_color = ft.Colors.BLACK
            card_bg_default = ft.Colors.WHITE

        # Assign background to container
        self.bgcolor = bg_color

        self.content = ft.Column(
            controls=[
                ft.Text("Home Dashboard", size=28, weight=ft.FontWeight.BOLD, color=text_color),
                ft.Container(height=20),
                ft.Row(
                    controls=[
                        create_stat_card(self.page, "Total Users", "1,234", ft.Icons.PEOPLE, ft.Colors.BLUE_400),
                        create_stat_card(self.page, "Revenue", "$45.2K", ft.Icons.ATTACH_MONEY, ft.Colors.GREEN_400),
                        create_stat_card(self.page, "Orders", "892", ft.Icons.SHOPPING_CART, ft.Colors.ORANGE_400),
                    ],
                    wrap=True,
                    spacing=20,
                ),
                ft.Container(height=20),
                ft.Text("Recent Activity", size=20, weight=ft.FontWeight.BOLD, color=text_color),
                ft.Container(height=10),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.PERSON_ADD, color=text_color),
                                title=ft.Text("New user registered", color=text_color),
                                subtitle=ft.Text("2 minutes ago", color=text_color),
                            ),
                            ft.Divider(color=text_color),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.SHOPPING_BAG, color=text_color),
                                title=ft.Text("New order received", color=text_color),
                                subtitle=ft.Text("15 minutes ago", color=text_color),
                            ),
                            ft.Divider(color=text_color),
                            ft.ListTile(
                                leading=ft.Icon(ft.Icons.PAYMENT, color=text_color),
                                title=ft.Text("Payment processed", color=text_color),
                                subtitle=ft.Text("1 hour ago", color=text_color),
                            ),
                        ],
                    ),
                    bgcolor=card_bg_default,
                    border_radius=10,
                    padding=10,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )

    # ------------------------------------------------------------
    # Called externally when theme changes
    # ------------------------------------------------------------
    def update_theme(self):
        self._build_content()
        self.update()
