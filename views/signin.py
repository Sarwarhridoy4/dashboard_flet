import flet as ft
from styles import PRIMARY_COLOR, BUTTON_RADIUS, PADDING, button_width

def signin_view(page):

    email = ft.TextField(label="Email", width=button_width(page))
    password = ft.TextField(label="Password", width=button_width(page), password=True)

    return ft.View(
        "/signin",
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                padding=PADDING,
                content=ft.Column(
                    [
                        ft.Text("Sign In", size=26, weight=ft.FontWeight.BOLD),
                        email,
                        password,
                        ft.ElevatedButton(
                            "Sign In",
                            width=button_width(page),
                            on_click=lambda e: page.go("/dashboard"),   # ✔ Go to dashboard
                            style=ft.ButtonStyle(
                                bgcolor=PRIMARY_COLOR,
                                color=ft.Colors.WHITE,  # ✔ fixed case
                                shape=ft.RoundedRectangleBorder(radius=BUTTON_RADIUS),
                            ),
                        ),
                        ft.TextButton(
                            "Don't have an account? Sign Up",
                            on_click=lambda e: page.go("/signup")
                        )
                    ],
                    spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        ],
    )
