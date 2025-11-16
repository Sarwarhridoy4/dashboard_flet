import flet as ft
from styles import PRIMARY_COLOR, BUTTON_RADIUS, PADDING

def signin_view(page, on_signin):
    email = ft.TextField(label="Email", width=300)
    password = ft.TextField(label="Password", password=True, width=300)

    button_style = ft.ButtonStyle(
        bgcolor=PRIMARY_COLOR,
        color=ft.Colors.WHITE,
        shape=ft.RoundedRectangleBorder(radius=BUTTON_RADIUS),
        padding=ft.padding.symmetric(vertical=12, horizontal=50),
    )

    btn = ft.ElevatedButton("Sign In", on_click=lambda e: on_signin(email.value, password.value), style=button_style)
    back = ft.TextButton("Back", on_click=lambda e: page.go("/"))

    return ft.View(
        "/signin",
        [
            ft.Container(
                content=ft.Column(
                    [email, password, btn, back],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                ),
                padding=PADDING,
                expand=True,
                alignment=ft.alignment.center,
            )
        ]
    )
