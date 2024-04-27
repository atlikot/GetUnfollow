from core.style import *

def Login(router):
    content = Column(
        [
            Container(
                Container(
                    Stack(
                        [
                            Container(
                                border_radius=11,
                                rotate=Rotate(0.98 * 3.14),  # degree
                                width=form_width,
                                height=form_height,
                                bgcolor=form_bgcolor,
                                border=form_border,
                            ),
                            Container(
                                Container(
                                    Column([
                                        Container(
                                            Image(
                                                src='assets/rat.png',
                                                width=130,
                                            ), padding=padding.only(100, 50),

                                        ),
                                        Text(
                                            "Get Unfollow",
                                            width=form_width,
                                            size=35,
                                            weight='w900',
                                            text_align='center',
                                        ),
                                        Text(
                                            "Please login via Instagram Account:",
                                            width=form_width,
                                            text_align='center',
                                        ),
                                        Container(
                                            TextField(
                                                width=input_width,
                                                height=input_height,
                                                hint_text='Username',
                                                border='underline',
                                                color=input_text_color,
                                                prefix_icon=icons.EMAIL,
                                            ), padding.only(25, 10)
                                        ),
                                        Container(
                                            TextField(
                                                width=input_width,
                                                height=input_height,
                                                hint_text='Password',
                                                border='underline',
                                                color=input_text_color,
                                                prefix_icon=icons.LOCK,
                                            ), padding.only(25, 10),
                                        ),
                                        Container
                                            (
                                            Text(
                                                "* use test/test to enter testing view",
                                                width=form_width,
                                                text_align='center',
                                            )
                                        ),
                                        Container(
                                            ElevatedButton(
                                                content=Text(
                                                    'SIGN IN',
                                                    color='white',
                                                    weight='w500',
                                                ), width=200, bgcolor='black',
                                            ), padding.only(70, 10)
                                        )],
                                    ),
                                    border_radius=11,
                                    width=form_width,
                                    height=form_height,
                                    bgcolor=form_bgcolor,
                                    border=form_border,
                                ),
                            )
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