import flet as ft
from styles import PRIMARY_COLOR, BUTTON_RADIUS, PADDING

def dashboard_view(page, user):
    welcome = ft.Text(f"Hello, {user['name']}!", size=24, weight=ft.FontWeight.BOLD)

    button_style = ft.ButtonStyle(
        bgcolor=PRIMARY_COLOR,
        color=ft.Colors.WHITE,
        shape=ft.RoundedRectangleBorder(radius=BUTTON_RADIUS),
        padding=ft.padding.symmetric(vertical=12, horizontal=50),
    )

    logout = ft.ElevatedButton("Log out", on_click=lambda e: page.go("/"), style=button_style)

    return ft.View(
        "/dashboard",
        [
            ft.Container(
                content=ft.Column(
                    [welcome, logout],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=PADDING,
                expand=True,
                alignment=ft.alignment.center,
            )
        ]
    )
