import reflex as rx


class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

# class CondSimpleState(rx.State):
#     show: bool = True

#     def change(self):
#         self.show = not (self.show)


# def cond_simple_example():
#     return rx.vstack(
#         rx.button(
#             "Toggle", on_click=CondSimpleState.change
#         ),
#         rx.cond(
#             CondSimpleState.show,
#             rx.text("Text 1", color="blue"),
#             rx.text("Text 2", color="red"),
#         ),
#     )

def index() -> rx.Component:
        return rx.container(
            rx.center(
                # rx.color_mode.button("Change"),
                rx.hstack(
                    rx.button(
                        "Decrement",
                        color_scheme="ruby",
                        on_click=State.decrement,
                    ),
                    rx.heading(State.count, font_size="2em"),
                    rx.button(
                        "Increment",
                        color_scheme="grass",
                        on_click=State.increment,
                    ),
                spacing="3",
            ),
            # cond_simple_example(),
        )
    )
app = rx.App()
app.add_page(index)
