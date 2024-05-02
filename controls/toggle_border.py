from core.style import *


class ToggleBorder(ft.Container):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.border1 = self.create_border(form_rotate)
        self.border2 = self.create_border(0)

        self.content = ft.Stack(
            [
                self.border1,
                self.border2
            ]
        )

    @staticmethod
    def create_border(rotate) -> ft.Container:
        return ft.Container(
            border_radius=form_radius,
            rotate=ft.Rotate(rotate),  # degree
            width=form_width,
            height=form_height,
            margin=form_margin,
            border=form_border,
        )

    def before_update(self):
        super().before_update()
        self.border1.border = form_border if self.page.theme_mode == ft.ThemeMode.LIGHT else form_border_light
        self.border2.border = form_border if self.page.theme_mode == ft.ThemeMode.LIGHT else form_border_light
