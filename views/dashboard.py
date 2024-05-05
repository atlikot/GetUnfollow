import click

from core.style import *
from core.client import *
from time import sleep
from core import fake
from controls.toggle_bg import ToggleBackground
from controls.toggle_border import ToggleBorder


class Dashboard(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.current_user = ''

        # print(cl.username)
        # print('Getting following list...')
        #
        # followers = fake.get_followers() if cl.username == 'fake' else cl.user_followers(str(cl.user_id))
        # following = fake.get_following() if cl.username == 'fake' else cl.user_following(str(cl.user_id))
        #
        # print('-------------')
        # print(followers)
        # print('-------------')
        # print(following)
        # print('-------------')
        #
        # string = ''
        # unfollow = {k: v for k, v in following.items() if k not in followers}
        # print(unfollow)
        # print('-------------')
        #
        # for k in unfollow:
        #     string += following.get(k).username + ', '
        # string = string.rstrip(', ')
        # print('-------------')
        #
        # print('Unfollows:', string)
        # print('Done')

        def get_content():
            if cl.username:
                return ft.Stack(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    f"UserName: ",
                                    width=form_width,
                                    size=25,
                                    weight='w400',
                                    text_align='center'
                                )
                            ]
                        )

                    ]
                )
            else:
                return ft.Stack(
                    [
                        ft.Column(
                            [
                                ft.Text(
                                    f"Please login first!",
                                    size=25,
                                    weight='w400',
                                    text_align='center'
                                )
                            ]
                        )

                    ]
                )

    def load(self):

        if not cl.username:
            self.content = ft.Column(
                [
                    ft.Text(
                        "Please login first",
                        width=form_width,
                        size=25,
                        weight='w400',
                        text_align='center'
                    )
                ])
            self.page.update()
            return

        if self.current_user == cl.username:
            return

        self.current_user = cl.username
        self.content = ft.Column([
            ft.Row(
                [ft.ProgressRing()],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ], alignment=ft.MainAxisAlignment.CENTER, height=board_height)
        self.page.update()

        followers = fake.get_followers() if cl.username == 'fake' else cl.user_followers(str(cl.user_id))
        following = fake.get_following() if cl.username == 'fake' else cl.user_following(str(cl.user_id))

        print('Loading complete!')
        self.content = ft.Column(
            [
                ft.Text(
                    "UserName: " + cl.username,
                    width=form_width,
                    size=25,
                    weight='w400',
                    text_align='center'
                )
            ])
        self.page.update()
