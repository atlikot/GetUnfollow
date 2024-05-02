from core.style import *
from flet import *


class Dashboard(Container):
    def __init__(self):
        super().__init__()
        self.content = Container(
            Text(value='Панель управления')
        )
