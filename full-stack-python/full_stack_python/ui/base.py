import reflex as rx

from .nav import navbar

def base_page(*args, **kwargs) -> rx.Component:

    return rx.fragment(
        navbar(),
        rx.box(
            args,
            padding="1em",
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
    )
