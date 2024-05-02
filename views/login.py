#         self.image_active = Image(src='assets/bg_windows_active.png')
#         self.image_noactive = Image(src='assets/bg_windows.png',
#                                     animate_opacity=300,
#                                     opacity=1)

#         def animate_eyes(e):
#             if self.image_noactive.opacity == 1:
#                 self.image_noactive.opacity = 0
#                 self.image_noactive.update()
#
#
#
#         self.login_button = ElevatedButton(
#             text=dic_login_button,
#             width=button_width,
#             height=button_height,
#             style=ButtonStyle(
#                 bgcolor=button_bgcolor,
#                 color=button_font_color,
#                 side=button_border,
#                 overlay_color=button_overlay,
#             ),
#             on_click=lambda e: login_auth(e)
#
##
#         #Контент
#         self.content = Container(
#             Stack([
#                 self.login_error,
#                 self.image_active,
#                 self.image_noactive,
#                 Container(
#                     Text(
#                         value=dic_login_name,
#                         size=18,
#                         color=login_title_color
#                     ),
#                     margin=login_title_margin
#                 ),
#                 Container(
#                     Container(
#                         Column([
#                             self.login_username,
#                             self.login_password,
#                             Row([self.login_button], alignment=button_align)],
#                             spacing=20),
#                         padding=20,
#                         width=form_width,
#                         height=form_height,
#                         bgcolor=form_bgcolor,
#                         border_radius=10,
#                         border=form_border,
#                         margin=form_margin
#                     ),
#                     alignment=alignment.center
#                 )
#             ])
#         )

from core.style import *


class Login(ft.Container):
    def __init__(self):
        super().__init__()

        self.image_white = ft.Image(src='assets/ratw.png')
        self.image_black = ft.Image(src='assets/rat.png',
                                    animate_opacity=300,
                                    opacity=0)

        def login_auth(e):
            login = self.login.value
            password = self.password.value

            print(login)
            print(password)

            if (login == 'Login' and password == 'test'):
                self.page.go(
                    '/dashboard'
                )
            else:
                self.login_error.open = True
                self.login_error.update()

        self.login_error = ft.SnackBar(
            ft.Text(f"Неверный логин или пароль", color='#ff0000'),
            bgcolor=alert_error_bg
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
        ),

        self.content = ft.Container(
            ft.Stack(
                [
                    ft.Container(
                        border_radius=form_radius,
                        rotate=ft.Rotate(0.98 * 3.14),  # degree
                        width=form_width,
                        height=form_height,
                        margin=form_margin,
                        border=form_border,
                    ),
                    ft.Container(
                        ft.Column([
                            ft.Row(
                                [
                                    ft.Container(
                                        ft.Stack(
                                            [
                                                self.image_white,
                                                self.image_black
                                            ]
                                        )
                                        , height=logo_size)
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
                                [ft.ElevatedButton(
                                    content=ft.Text(
                                        'SIGN IN',
                                        # color='white',
                                        weight='w500',
                                    ), width=200,
                                )],alignment=center
                            ),
                            self.login_error,

                        ]
                        ), border_radius=form_radius,
                        width=form_width,
                        height=form_height,
                        border=form_border,
                        margin=form_margin,
                        padding=ft.padding.all(50)
                    )
                ]
            ),
            width=windows_width,
            height=board_height,
            gradient=form_gradient
        )
