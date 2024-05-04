from core.style import *


class ToggleBackground(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.board = self.create_board()
        self.content = self.board

    @staticmethod
    def create_board() -> ft.Container:
        return ft.Container(
            width=windows_width,
            height=board_height,
            gradient=form_gradient
        )

    def before_update(self):
        super().before_update()
        self.board.gradient = form_gradient if self.page.theme_mode == ft.ThemeMode.DARK else form_gradient_light
