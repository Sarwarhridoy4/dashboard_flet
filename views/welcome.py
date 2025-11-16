import flet as ft
from styles import PRIMARY_COLOR, BUTTON_RADIUS, PADDING

def welcome_view(page):
    button_style = ft.ButtonStyle(
        bgcolor=PRIMARY_COLOR,
        color=ft.Colors.WHITE,
        shape=ft.RoundedRectangleBorder(radius=BUTTON_RADIUS),
        padding=ft.padding.symmetric(vertical=12, horizontal=50),
    )

    return ft.View(
        "/",
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Welcome to MyApp", size=32, weight=ft.FontWeight.BOLD),
                        ft.ElevatedButton("Sign Up", on_click=lambda e: page.go("/signup"), style=button_style),
                        ft.ElevatedButton("Sign In", on_click=lambda e: page.go("/signin"), style=button_style),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=PADDING,
                alignment=ft.alignment.center,
                expand=True,
            )
        ]
    )
