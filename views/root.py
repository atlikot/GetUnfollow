from controls.toggle_bg import ToggleBackground
from core.style import snack_bg
from views.login import Login
from views.about import About
from views.dashboard import Dashboard
import flet as ft


class Root:
    def __init__(self, page: ft.Page):
        self.routes = {
            "/": Login(page),
            "/about": About(page),
            "/dashboard": Dashboard(page),
        }
        self.body = ft.Container()
        self.page = page
        self.page.add(
            ft.Stack(
                [
                    ToggleBackground(page),
                    self.body,
                ]
            )
        )

    def on_route_change(self, route):
        print('Route: ', self.page.route)
        self.body.content = self.routes[self.page.route]
        self.page.update()
        if self.page.route == '/dashboard':
            self.body.content.load()