import flet as ft


def toggle_dark_mode(e):
    page = e.page
    if page.theme_mode == "light":
        page.theme_mode = "dark"
        page.update()
    else:
        page.theme_mode = "light"
        page.update()


def exit_app(e):
    page = e.page
    page.window_destroy()


def navBar(page):
    navbar = ft.AppBar(
        leading_width=5,
        title=ft.Text("Get Unfollow"),
        center_title=False,
        actions=[
            ft.IconButton(ft.icons.LOGIN_ROUNDED, tooltip='Login', on_click=lambda _: page.go('/')),
            ft.IconButton(ft.icons.HOME_ROUNDED, tooltip='Dashboard', on_click=lambda _: page.go('/dashboard')),
            ft.IconButton(ft.icons.PERSON_ROUNDED, tooltip='Author', on_click=lambda _: page.go('/about')),
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, tooltip='Light/Dark Mode', on_click=toggle_dark_mode),
            ft.IconButton(ft.icons.EXIT_TO_APP, tooltip='Exit application', on_click=exit_app)
        ]
    )

    return navbar
