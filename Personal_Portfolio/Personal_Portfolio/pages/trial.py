import reflex as rx
from Personal_Portfolio.templates import template

@template(route="/in_de", title="Increment-Decrement")
class up_down(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def in_de():
    return rx.hstack(
        rx.button(
            "Decrement",
            color_scheme="ruby",
            on_click=up_down.decrement,
        ),
        rx.heading(up_down.count, font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="grass",
            on_click=up_down.increment,
        ),
        spacing="4",
    )


app = rx.App()
app.add_page(in_de)
