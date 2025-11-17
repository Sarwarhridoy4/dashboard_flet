import flet as ft

class AnalyticsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 30
        self.expand = True

        self._build_content()

    # ------------------------------------------------------------
    # Build content based on current theme
    # ------------------------------------------------------------
    def _build_content(self):
        theme = self.page.theme_mode

        if theme == ft.ThemeMode.DARK:
            text_color = ft.Colors.WHITE
            subtitle_color = ft.Colors.WHITE70
            container_bg = ft.Colors.BLACK
            icon_color = ft.Colors.BLUE_300
            bg_color = ft.Colors.BLACK87
        else:
            text_color = ft.Colors.BLACK
            subtitle_color = ft.Colors.BLACK54
            container_bg = ft.Colors.WHITE
            icon_color = ft.Colors.BLUE_700
            bg_color = ft.Colors.WHITE

        self.content = ft.Column(
            controls=[
                ft.Text("Analytics", size=28, weight=ft.FontWeight.BOLD, color=text_color),
                ft.Container(height=20),
                ft.Text(
                    "View your performance metrics and insights here.",
                    size=16,
                    color=text_color
                ),
                ft.Container(height=20),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Icon(ft.Icons.BAR_CHART, size=60, color=icon_color),
                            ft.Text(
                                "Chart placeholder",
                                size=18,
                                text_align=ft.TextAlign.CENTER,
                                color=text_color
                            ),
                            ft.Text(
                                "Add your charts and graphs here",
                                size=14,
                                color=subtitle_color,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    bgcolor=container_bg,
                    border_radius=10,
                    padding=50,
                    alignment=ft.alignment.center,
                    height=300,
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
            
            
        )
        self.bgcolor = bg_color

    # ------------------------------------------------------------
    # Called by DashboardView when theme changes
    # ------------------------------------------------------------
    def update_theme(self):
        self._build_content()
        self.update()
