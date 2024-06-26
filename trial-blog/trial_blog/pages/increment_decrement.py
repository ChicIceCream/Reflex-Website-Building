import reflex as rx
from trial_blog.templates import ThemeState, template
from trial_blog.state import Up_Down_State

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
@template(route="/simple", title="Increment-Decrement")
def increment_decrement() -> rx.Component:
        return rx.container(
            rx.center(
                # rx.color_mode.button("Change"),
                rx.hstack(
                    rx.button(
                        "Decrement",
                        color_scheme="ruby",
                        on_click=Up_Down_State.decrement,
                    ),
                    rx.heading(Up_Down_State.count, font_size="2em"),
                    rx.button(
                        "Increment",
                        color_scheme="grass",
                        on_click=Up_Down_State.increment,
                    ),
                spacing="3",
            ),
            # cond_simple_example(),
        )
    )