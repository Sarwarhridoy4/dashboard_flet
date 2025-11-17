# views/dashboard_view.py
import flet as ft
from components.sidebar import Sidebar
from pages.home_page import HomePage
from pages.analytics_page import AnalyticsPage
from pages.settings_page import SettingsPage
from models.menu_item import MenuItem


class DashboardView(ft.Row):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.spacing = 0
        self.expand = True

        # Define menu items
        self.menu_items = [
            MenuItem(ft.Icons.HOME_ROUNDED, "Home", HomePage),
            MenuItem(ft.Icons.ANALYTICS_ROUNDED, "Analytics", AnalyticsPage),
            MenuItem(ft.Icons.SETTINGS_ROUNDED, "Settings", SettingsPage),
            # Add more menu items here
        ]

        # Create sidebar (pass page as first argument)
        self.sidebar = Sidebar(
            page=self.page,
            menu_items=self.menu_items,
            on_menu_change=self.on_menu_change,
        )

        # Create content area
        self.content_area = ft.Container(
            content=self.menu_items[0].page_class(self.page),
            expand=True,
        )

        self.controls = [
            self.sidebar,
            self.content_area,
        ]

        # Listen for theme changes to update sidebar and content
        self.page.on_theme_changed = lambda e: self.update_theme()

    # ------------------------------------------------------------
    # Handle menu selection
    # ------------------------------------------------------------
    def on_menu_change(self, index: int):
        # Update content area with selected page
        self.content_area.content = self.menu_items[index].page_class(self.page)
        self.content_area.update()

    # ------------------------------------------------------------
    # Update theme-aware components
    # ------------------------------------------------------------
    def update_theme(self):
        # Update sidebar colors
        self.sidebar.update_theme()

        # Update current content page (calls its update_theme if exists)
        if hasattr(self.content_area.content, "update_theme"):
            self.content_area.content.update_theme()
