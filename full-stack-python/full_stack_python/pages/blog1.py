import reflex as rx

from ..ui.base import base_page

def blog1_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("This is going to be my first blog!!!!!", size="9"),
            rx.text(
                "Gonna be epicc!!!",
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )
