# main.py
import flet as ft
from views.welcome_view import WelcomeView
from views.dashboard_view import DashboardView


def main(page: ft.Page):
    page.title = "Dashboard App"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    
    # Theme configuration
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.BLUE,
        use_material3=True,
    )
    
    def show_dashboard():
        page.controls.clear()
        page.add(DashboardView(page))
        page.update()
    
    def show_welcome():
        page.controls.clear()
        page.add(WelcomeView(on_sign_in=show_dashboard))
        page.update()
    
    # Start with welcome screen
    show_welcome()


if __name__ == "__main__":
    ft.app(target=main)