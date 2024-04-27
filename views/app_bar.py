import flet as ft


def NavBar(page):


    NavBar = ft.AppBar(
            leading_width=20,
            title=ft.Text("Get Unfollow"),
            center_title=False,
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
                ft.IconButton(ft.icons.PERSON_ROUNDED, on_click=lambda _: page.go('/profile')),
                ft.IconButton(ft.icons.SETTINGS_ROUNDED, on_click=lambda _: page.go('/settings')),
                ft.IconButton(ft.icons.EXIT_TO_APP, on_click=lambda _: page.go('/settings'))
            ]
        )

    return NavBar