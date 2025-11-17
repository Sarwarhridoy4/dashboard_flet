# pages/settings_page.py
import flet as ft

class SettingsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.padding = 30
        self.expand = True

        # Theme switch
        self.theme_switch = ft.Switch(
            value=self.page.theme_mode == ft.ThemeMode.DARK,
            on_change=self.toggle_theme
        )

        # Build initial content
        self._build_content()

        # Listen for theme changes
        self.page.on_theme_changed = lambda e: self._on_theme_change()

    # ------------------------------------------------------------
    # Build content based on current theme
    # ------------------------------------------------------------
    def _build_content(self):
        theme = self.page.theme_mode

        if theme == ft.ThemeMode.DARK:
            text_color = ft.Colors.WHITE
            subtitle_color = ft.Colors.WHITE70
            container_bg = ft.Colors.BLACK
        else:
            text_color = ft.Colors.BLACK
            subtitle_color = ft.Colors.BLACK54
            container_bg = ft.Colors.WHITE

        self.content = ft.Column(
            controls=[
                ft.Text("Settings", size=28, weight=ft.FontWeight.BOLD, color=text_color),
                ft.Container(height=20),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.NOTIFICATIONS, color=text_color),
                    title=ft.Text("Notifications", color=text_color),
                    subtitle=ft.Text("Manage notification preferences", color=subtitle_color),
                    trailing=ft.Switch(value=True),
                ),
                ft.Divider(color=text_color),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.DARK_MODE, color=text_color),
                    title=ft.Text("Dark Mode", color=text_color),
                    subtitle=ft.Text("Toggle dark/light theme", color=subtitle_color),
                    trailing=self.theme_switch,
                ),
                ft.Divider(color=text_color),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.LANGUAGE, color=text_color),
                    title=ft.Text("Language", color=text_color),
                    subtitle=ft.Text("English", color=subtitle_color),
                    trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT, color=text_color),
                ),
                ft.Divider(color=text_color),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.SECURITY, color=text_color),
                    title=ft.Text("Privacy & Security", color=text_color),
                    subtitle=ft.Text("Manage your account security", color=subtitle_color),
                    trailing=ft.Icon(ft.Icons.CHEVRON_RIGHT, color=text_color),
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )

        # Set the container background dynamically
        self.bgcolor = container_bg

    # ------------------------------------------------------------
    # Toggle dark/light theme
    # ------------------------------------------------------------
    def toggle_theme(self, e):
        # Switch theme
        self.page.theme_mode = (
            ft.ThemeMode.LIGHT
            if self.page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )

        # Update the switch UI
        self.theme_switch.value = self.page.theme_mode == ft.ThemeMode.DARK

        # Notify other components to rebuild
        if callable(getattr(self.page, "on_theme_changed", None)):
            self.page.on_theme_changed(None)

        # Rebuild current page
        self._build_content()
        self.update()

    # ------------------------------------------------------------
    # Called when theme changes externally
    # ------------------------------------------------------------
    def _on_theme_change(self):
        # Update switch value
        self.theme_switch.value = self.page.theme_mode == ft.ThemeMode.DARK
        # Rebuild page content with new theme
        self._build_content()
        self.update()
