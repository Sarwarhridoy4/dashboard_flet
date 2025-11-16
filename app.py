import flet as ft
from views.welcome import welcome_view
from views.signup import signup_view
from views.signin import signin_view
from views.dashboard import dashboard_view

USERS = {}

def main(page: ft.Page):
    page.title = "My Flet App"
    
    def on_route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        route = page.route
        if route == "/":
            page.views.append(welcome_view(page))
        elif route == "/signup":
            page.views.append(signup_view(page, on_signup))
        elif route == "/signin":
            page.views.append(signin_view(page, on_signin))
        elif route == "/dashboard":
            if "current_user" in page.session:
                page.views.append(dashboard_view(page, page.session["current_user"]))
            else:
                page.go("/signin")
                return
        else:
            page.go("/")
        page.update()

    def on_signup(name, email, password):
        if email in USERS:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("User already exists"),
                actions=[ft.TextButton("OK", on_click=lambda e: setattr(page.dialog, "open", False))]
            )
            page.dialog.open = True
            page.update()
            return
        USERS[email] = {"name": name, "email": email, "password": password}
        page.session["current_user"] = USERS[email]
        page.go("/dashboard")
        page.update()

    def on_signin(email, password):
        user = USERS.get(email)
        if user and user["password"] == password:
            page.session["current_user"] = user
            page.go("/dashboard")
        else:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Error"),
                content=ft.Text("Invalid credentials"),
                actions=[ft.TextButton("OK", on_click=lambda e: setattr(page.dialog, "open", False))]
            )
            page.dialog.open = True
        page.update()

    page.on_route_change = on_route_change
    page.go(page.route)
    page.update()

ft.app(target=main)
