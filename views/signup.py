import flet as ft
from styles import PRIMARY_COLOR, BUTTON_RADIUS, PADDING, button_width

def signup_view(page):

    name = ft.TextField(label="Name", width=button_width(page))
    email = ft.TextField(label="Email", width=button_width(page))
    password = ft.TextField(label="Password", width=button_width(page), password=True)

    return ft.View(
        "/signup",
        controls=[
            ft.Container(
                alignment=ft.alignment.center,
                expand=True,
                padding=PADDING,
                content=ft.Column(
                    [
                        ft.Text("Create Account", size=26, weight=ft.FontWeight.BOLD),
                        name,
                        email,
                        password,
                        ft.ElevatedButton(
                            "Sign Up",
                            width=button_width(page),
                            style=ft.ButtonStyle(
                                bgcolor=PRIMARY_COLOR,
                                color=ft.Colors.WHITE,
                                shape=ft.RoundedRectangleBorder(radius=BUTTON_RADIUS),
                            ),
                        ),
                        ft.TextButton(
                            "Already have an account? Sign In",
                            on_click=lambda e: page.go("/signin")
                        )
                    ],
                    spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        ],
    )
