from typing import Optional

from flet_core.gradients import Gradient

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
            gradient=login_gradient
        )

    def before_update(self):
        super().before_update()
        if self.page.route == '/dashboard':
            self.board.gradient = dashboard_gradient if self.page.theme_mode == ft.ThemeMode.DARK else dashboard_gradient_light
        else:
            self.board.gradient = login_gradient if self.page.theme_mode == ft.ThemeMode.DARK else login_gradient_light
