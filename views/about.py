import flet as ft


class About(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Author:", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Image(src=f"/cat.jpg", width=100, border_radius=100)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Text("Name: Vladimir Semyonov")
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("Contact: https://t.me/atlikot")
                    ]
                ),
                ft.Row(
                    [
                        ft.Text("Github: https://github.com/atlikot")
                    ]
                ),
            ]

        )
