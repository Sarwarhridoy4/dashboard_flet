import flet as ft

class Sidebar(ft.Container):
    def __init__(self, page: ft.Page, menu_items, on_menu_change):
        super().__init__()
        self.page = page
        self.menu_items = menu_items
        self.on_menu_change = on_menu_change

        self.expanded = True
        self.selected_index = 0
        self.width = 250
        self.animate = ft.Animation(300, ft.AnimationCurve.EASE_OUT)

        # Placeholder content until mounted
        self.content = ft.Container()

        # Listen for theme changes
        self.page.on_theme_changed = lambda e: self.update_theme()

        # Build initially
        self._build_sidebar()

    # ------------------------------------------------------------
    # Apply colors based on current theme
    # ------------------------------------------------------------
    def _apply_theme_colors(self):
        if self.page.theme_mode == ft.ThemeMode.DARK:
            self.bgcolor = ft.Colors.BLACK
            self.text_color = ft.Colors.WHITE
            self.icon_color = ft.Colors.WHITE
            self.selected_bg = ft.Colors.BLUE_700
            self.divider_color = ft.Colors.WHITE12
        else:
            self.bgcolor = ft.Colors.WHITE
            self.text_color = ft.Colors.BLACK
            self.icon_color = ft.Colors.BLACK
            self.selected_bg = ft.Colors.BLUE_200
            self.divider_color = ft.Colors.BLACK12

    # ------------------------------------------------------------
    # Build sidebar layout
    # ------------------------------------------------------------
    def _build_sidebar(self):
        self._apply_theme_colors()

        # Menu buttons
        self.menu_buttons = []
        for i, item in enumerate(self.menu_items):
            btn = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Icon(item.icon, size=24, color=self.icon_color),
                        ft.Text(item.label, size=14, visible=self.expanded, color=self.text_color),
                    ],
                    spacing=15,
                ),
                padding=15,
                border_radius=10,
                ink=True,
                on_click=lambda e, idx=i: self.select_menu(idx),
                bgcolor=self.selected_bg if i == self.selected_index else None,
            )
            self.menu_buttons.append(btn)

        # Header
        self.header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.DASHBOARD_ROUNDED, size=28, color=self.icon_color),
                    ft.Text(
                        "Dashboard",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        visible=self.expanded,
                        color=self.text_color,
                    ),
                ],
                spacing=10,
            ),
            padding=20,
        )

        # Toggle button
        self.toggle_btn = ft.IconButton(
            icon=ft.Icons.MENU_OPEN if self.expanded else ft.Icons.MENU,
            icon_color=self.icon_color,
            on_click=self.toggle_sidebar,
        )

        # Build sidebar content
        self.content = ft.Column(
            controls=[
                self.header,
                ft.Divider(height=1, color=self.divider_color),
                ft.Container(
                    content=ft.Column(controls=self.menu_buttons, spacing=5),
                    padding=10,
                    expand=True,
                ),
                ft.Divider(height=1, color=self.divider_color),
                ft.Container(content=self.toggle_btn, padding=10),
            ],
            spacing=0,
        )

        # Set overall background
        self.bgcolor = self.bgcolor

    # ------------------------------------------------------------
    # Collapse / expand toggle
    # ------------------------------------------------------------
    def toggle_sidebar(self, e):
        self.expanded = not self.expanded
        self.width = 250 if self.expanded else 70

        for b in self.menu_buttons:
            b.content.controls[1].visible = self.expanded

        self.header.content.controls[1].visible = self.expanded
        self.toggle_btn.icon = ft.Icons.MENU_OPEN if self.expanded else ft.Icons.MENU

        self.update()

    # ------------------------------------------------------------
    # Select a menu item
    # ------------------------------------------------------------
    def select_menu(self, index):
        self.selected_index = index

        for i, b in enumerate(self.menu_buttons):
            b.bgcolor = self.selected_bg if i == index else None

        self.on_menu_change(index)
        self.update()

    # ------------------------------------------------------------
    # Update theme externally
    # ------------------------------------------------------------
    def update_theme(self):
        self._build_sidebar()
        self.update()
