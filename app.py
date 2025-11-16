import flet as ft
from views.welcome import welcome_view
from views.signup import signup_view
from views.signin import signin_view
from views.dashboard import dashboard_view


def main(page: ft.Page):
    page.title = "My Flet App"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Toggle Dark / Light mode
    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    # Build the AppBar
    def build_appbar(show_back=False):
        return ft.AppBar(
            leading=(
                ft.IconButton(ft.Icons.ARROW_BACK, on_click=lambda e: page.go("/"))
                if show_back else None
            ),
            title=ft.Text("My Flet App"),
            actions=[
                ft.IconButton(
                    ft.Icons.DARK_MODE if page.theme_mode == ft.ThemeMode.LIGHT else ft.Icons.LIGHT_MODE,
                    on_click=toggle_theme
                )
            ],
            center_title=False,
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,
        )

    def on_route_change(e):
        route = page.route
        page.views.clear()

        if route == "/":
            page.appbar = build_appbar(show_back=False)
            page.views.append(welcome_view(page))
        elif route == "/signup":
            page.appbar = build_appbar(show_back=True)
            page.views.append(signup_view(page))
        elif route == "/signin":
            page.appbar = build_appbar(show_back=True)
            page.views.append(signin_view(page))
        elif route == "/dashboard":
            page.appbar = build_appbar(show_back=True)
            page.views.append(dashboard_view(page))
        else:
            page.go("/")
            return

        page.update()

    page.on_route_change = on_route_change
    page.on_resize = lambda e: page.update()
    page.go(page.route)


ft.app(target=main)
