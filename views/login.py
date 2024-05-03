from core.style import *
from controls.toggle_image import ToggleImage
from controls.toggle_border import ToggleBorder
from core.client import *



class Login(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        # def snack_bar(status):
        #     if status == 'error':
        #         snack_message = 'Incorrect login or password'
        #         snack_color = '#ff0000'
        #     elif status == 'success':
        #         snack_message = 'Incorrect login or password'
        #         snack_color = '00ff00'
        #     else:
        #         snack_message = ''
        #         snack_color = 'ff0000'
        #
        #     bar = ft.SnackBar(ft.Text(snack_message, color=snack_color),
        #                       bgcolor='#1e1c20')
        #
        #     bar.open = True
        #     bar.update()
        #
        #     return bar


        def login_auth(e):
            login = self.login.value
            password = self.password.value

            print(login)
            print(password)

            if login == 'test' and password == 'test':
                self.snack_bar.open = True
                self.snack_bar.update()
                cl.username = 'fake'
                self.page.go(
                    '/dashboard'
                )
                return
            elif not login or not password:
                return

            try:
                cl.login(login, password)
                self.snack_bar.open = True
                self.snack_bar.update()
                self.page.go(
                    '/dashboard'
                )
            except:
                self.snack_bar.open = True
                self.snack_bar.update()

        self.snack_bar = ft.SnackBar(
            ft.Text(f"Неверный логин или пароль", color='#ff0000'),
            bgcolor=snack_bg
        )

        self.login = ft.TextField(
            width=input_width,
            height=input_height,
            hint_text='Username',
            border='underline',
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
            border='underline',
            prefix_icon=ft.icons.LOCK,
        )

        self.login_button = ft.ElevatedButton(
            content=ft.Text(
                'SIGN IN',
                # color='white',
                weight='w500',
            ), width=200,
            on_click=lambda e: login_auth(e)
        )

        self.content = ft.Container(
            ft.Stack(
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
                                weight='w900',
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
                            self.snack_bar,

                        ]
                        ), border_radius=form_radius,
                        width=form_width,
                        height=form_height,
                        margin=form_margin,
                        padding=ft.padding.all(50)
                    )
                ]
            ),
            width=windows_width,
            height=board_height,
            gradient=form_gradient
        )
