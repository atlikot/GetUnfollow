import flet as ft


class ToggleImage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.image_white = ft.Image(src='assets/ratw.png',
                                    opacity=0,
                                    animate_opacity=300,
                                    )
        self.image_black = ft.Image(src='assets/rat.png',
                                    animate_opacity=300,
                                    opacity=1)

        self.content = ft.Stack(
            [
                self.image_white,
                self.image_black
            ]
        )

    def before_update(self):
        super().before_update()
        self.image_white.opacity = 0 if self.page.theme_mode == ft.ThemeMode.LIGHT else 1
        self.image_black.opacity = 0 if self.page.theme_mode == ft.ThemeMode.DARK else 1
