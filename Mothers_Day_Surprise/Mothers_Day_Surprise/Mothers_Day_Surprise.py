"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

# class State(rx.State):
#     love: int = 0
    
#     def increment(self):
#         self.love += 1

#     def decrement(self):
#         self.love -= 1


class NestedState(rx.State):
    love: int = 5

    def increment(self):
        self.love += 1

    def decrement(self):
        self.love -= 1


def cond_complex_example():
    return rx.container(
        rx.center(
            rx.vstack(
            rx.hstack(
                rx.button(
                            "Decrease love ☹",
                            color_scheme="ruby",
                            on_click=NestedState.decrement,
                            size="4"
                        ),
                rx.cond(
                    (NestedState.love >= 10),
                    rx.chakra.circular_progress(
                        rx.chakra.circular_progress_label(
                            "∞  ♡", color="rgb(255,105,180)"
                        ),
                        color="rgb(255,20,147)",
                        size="70",
                        is_indeterminate=True,
                    ),
                ),
                rx.cond(
                    (NestedState.love <= 0),
                    rx.chakra.circular_progress(
                        rx.chakra.circular_progress_label(
                            "ERROR", color="rgb(128,0,0)"
                        ),
                        color="rgb(255,0,0)",
                        size="70",
                        is_indeterminate=True,
                    ),
                ),
                rx.cond(
                    (NestedState.love >= 1)
                    & (NestedState.love <= 9),
                    rx.chakra.circular_progress(
                            rx.chakra.circular_progress_label(
                                (NestedState.love*10), color="green"
                            ),
                            value=(NestedState.love*10),
                            color="rgb(255,20,147)",
                            size="70",
                        ),
                ),
                rx.button(
                            "Increase Love 😘",
                            color_scheme="grass",
                            on_click=NestedState.increment,
                            size="4"
                        ),
                spacing="7",
            ),
        ),
    ),
)

def index() -> rx.Component:
    return rx.container(
        rx.center(
            rx.vstack(
                rx.vstack(
                    rx.heading("Happy Mothers Day Mumma!", size="9", color="rgb(255,105,180)"),
                    rx.text("I just want to say that you are the best mom ever!"),
                    rx.text("Let's test something!"),
                    cond_complex_example(),
                    rx.text("By Abhivyakt Bhati :)", size="3"),
                    align="center",
                    spacing="9",
                    font_size="2em",
                ),
            ),
        ),
        rx.center(
        #     rx.hstack(
        #         rx.button(
        #             "Decrement",
        #             color_scheme="ruby",
        #             on_click=State.decrement,
        #         ),
        #         rx.chakra.circular_progress(
        #             rx.chakra.circular_progress_label(
        #                 (State.love*10), color="green"
        #             ),
        #             value=(State.love*10),
        #         ),
        #         rx.button(
        #             "Increment",
        #             color_scheme="grass",
        #             on_click=State.increment,
        #         ),
        #     spacing="5",
        # ),
    ),
)


app = rx.App()
app.add_page(index)
