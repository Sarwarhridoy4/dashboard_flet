import flet as ft
from styles import PRIMARY_COLOR, BUTTON_RADIUS, PADDING, responsive_text_size, button_width

def welcome_view(page):

    return ft.View(
        "/",
        controls=[
            ft.Container(
                expand=True,
                alignment=ft.alignment.center,
                padding=PADDING,
                content=ft.Column(
                    [
                        ft.Text(
                            "Welcome to MyApp",
                            size=responsive_text_size(page),
                            weight=ft.FontWeight.BOLD,
                            text_align="center",
                        ),
                        ft.ElevatedButton(
                            "Sign Up",
                            width=button_width(page),
                            style=ft.ButtonStyle(
                                bgcolor=PRIMARY_COLOR,
                                color=ft.Colors.WHITE,
                                shape=ft.RoundedRectangleBorder(radius=BUTTON_RADIUS),
                            ),
                            on_click=lambda e: page.go("/signup"),
                        ),
                        ft.ElevatedButton(
                            "Sign In",
                            width=button_width(page),
                            style=ft.ButtonStyle(
                                bgcolor=PRIMARY_COLOR,
                                color=ft.Colors.WHITE,
                                shape=ft.RoundedRectangleBorder(radius=BUTTON_RADIUS),
                            ),
                            on_click=lambda e: page.go("/signin"),
                        ),
                    ],
                    spacing=25,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
            )
        ],
    )
