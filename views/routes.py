from views.login import Login
from views.about import About
from views.dashboard import Dashboard
import flet as ft


class Routes:
    def __init__(self, page: ft.Page):
        self.routes = {
            "/": Login,
            "/about": About,
            "/dashboard": Dashboard,
        }

        self.body = ft.Container()
        self.page = page
        self.page.add(
            self.body
        )

    def on_route_change(self, route):
        print('Route: ', self.page.route)
        self.body.content = self.routes[self.page.route](self.page)
        self.page.update()
