from core.style import *

def Dashboard(router):
    content = Column(
        [
            Container(
                Container(
                    Stack(
                        [

                        ]),
                    padding=50,
                    width=form_width,
                    height=form_height,
                ),
                width=windows_width,
                height=windows_height,
                gradient=form_gradient,
            )
        ]
    )
    return content