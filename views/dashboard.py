import flet as ft
from styles import (
    PRIMARY_COLOR,
    BUTTON_RADIUS,
    PADDING,
    button_width,
    responsive_text_size
)

def dashboard_view(page):

    title = ft.Text(
        "Dashboard",
        size=responsive_text_size(page),
        weight=ft.FontWeight.BOLD,
        text_align="center",
    )

    def button(label, color, action):
        return ft.ElevatedButton(
            label,
            width=button_width(page),
            style=ft.ButtonStyle(
                bgcolor=color,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=BUTTON_RADIUS),
            ),
            on_click=action,
        )

    return ft.View(
        "/dashboard",
        controls=[
            ft.Container(
                expand=True,
                padding=PADDING,
                alignment=ft.alignment.center,
                content=ft.Column(
                    [
                        title,
                        button("Profile", ft.Colors.BLUE_700, lambda e: None),
                        button("Settings", ft.Colors.ORANGE_700, lambda e: None),
                        button("Reports", ft.Colors.GREEN_700, lambda e: None),
                        button("Logout", ft.Colors.RED_600, lambda e: page.go("/")),
                    ],
                    spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            )
        ],
    )
