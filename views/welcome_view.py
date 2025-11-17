# views/welcome_view.py
import flet as ft


class WelcomeView(ft.Container):
    def __init__(self, on_sign_in):
        super().__init__()
        self.on_sign_in = on_sign_in
        
        self.expand = True
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Icon(
                        ft.Icons.DASHBOARD_ROUNDED,
                        size=100,
                        color=ft.Colors.BLUE_400,
                    ),
                    padding=ft.padding.only(bottom=20),
                ),
                ft.Text(
                    "Welcome to Dashboard",
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Your all-in-one management solution",
                    size=16,
                    color=ft.Colors.GREY_400,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=40),
                ft.ElevatedButton(
                    "Sign In",
                    icon=ft.Icons.LOGIN,
                    on_click=lambda _: self.on_sign_in(),
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=ft.padding.symmetric(horizontal=50, vertical=20),
                    ),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        )