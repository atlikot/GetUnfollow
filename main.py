import flet as ft
from views.routes import *
from views.app_bar import navBar
from core.style import *


def main(page: ft.Page):
    routes = Routes(page)
    page.theme_mode = ft.ThemeMode.DARK
    page.window_center()
    page.window_width = windows_width
    page.window_height = windows_height
    page.window_resizable = False
    page.window_maximizable = False
    page.appbar = navBar(page)
    page.on_route_change = routes.on_route_change
    page.go('/')


ft.app(target=main, assets_dir="assets")