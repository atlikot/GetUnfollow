from core.style import *
from controls.toggle_image import ToggleImage
from controls.toggle_border import ToggleBorder
from controls.toggle_bg import ToggleBackground
from core.client import *


class Login(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()

        self.loading_container = ft.Container(width=windows_width,
                                              height=board_height,
                                              bgcolor='#20ffffff',
                                              visible=False)

        self.snack_bar_container = ft.Container()

        self.login = ft.TextField(
            width=input_width,
            height=input_height,
            hint_text='Username',
            border=ft.InputBorder.UNDERLINE,
            prefix_icon=ft.icons.EMAIL,
            content_padding=15
        )

        self.password = ft.TextField(
            width=input_width,
            height=input_height,
            hint_text='Password',
            content_padding=15,
            password=True,
            can_reveal_password=True,
            border=ft.InputBorder.UNDERLINE,
            prefix_icon=ft.icons.LOCK,
        )

        self.login_button = ft.ElevatedButton(
            content=ft.Text(
                'SIGN IN',
                # color='white',
                weight=ft.FontWeight.W_500,
            ), width=200,
            on_click=lambda e: self.login_auth(e)
        )

        self.content = ft.Stack(
            [
                ToggleBorder(page),
                ft.Container(
                    ft.Column([
                        ft.Row(
                            [
                                ft.Container(
                                    ToggleImage(page), height=logo_size)
                            ], alignment=center
                        ),
                        ft.Text(
                            "Get Unfollow",
                            width=form_width,
                            size=35,
                            weight=ft.FontWeight.W_900,
                            text_align='center'
                        ),
                        ft.Text(
                            "Please login via Instagram Account:",
                            width=form_width,
                            text_align='center',
                        ),
                        self.login,
                        self.password,
                        ft.Text(
                            "hint: use test/test to enter test view",
                            width=form_width,
                            text_align='center',
                        ),
                        ft.Row(
                            [self.login_button], alignment=center
                        ),

                    ]
                    ), border_radius=form_radius,
                    width=form_width,
                    height=form_height,
                    margin=form_margin,
                    padding=ft.padding.all(50)
                ),
                self.loading_container,
                self.snack_bar_container,
            ]
        )

    def appbar_on(self):
        self.page.appbar.disabled = False
        self.page.appbar.update()
        self.loading_container.clean()
        self.loading_container.visible = False
        self.loading_container.update()

    def appbar_off(self):
        self.page.appbar.disabled = True
        self.page.appbar.update()
        self.loading_container.content = ft.Column([
            ft.Row(
                [ft.ProgressRing()],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ], alignment=ft.MainAxisAlignment.CENTER, height=board_height)
        self.loading_container.visible = True
        self.loading_container.update()

    def login_auth(self, e):
        self.appbar_off()
        login = self.login.value
        password = self.password.value

        if login == 'test' and password == 'test':
            self.show_snack_bar('Logging in...', '#00ff00')
            cl.logout()
            cl.username = 'fake'
            self.page.go(
                '/dashboard'
            )
            self.appbar_on()
            return
        elif not login or not password:
            self.show_snack_bar('Please fill the login and password')
            self.appbar_on()
            return

        try:
            self.show_snack_bar('Logging in...', '#00ff00')
            cl.logout()
            cl.login(login, password)
            self.page.go(
                '/dashboard'
            )
        except:
            self.show_snack_bar('Incorrect login or password.')

        self.appbar_on()

    def show_snack_bar(self, title: str, color: str = '#ff0000'):

        self.snack_bar_container.content = ft.SnackBar(
            ft.Text(title, color=color),
            bgcolor=snack_bg,
            open=True
        )
        self.snack_bar_container.update()
