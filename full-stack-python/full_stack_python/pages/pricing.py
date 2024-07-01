import reflex as rx

from ..ui.base import base_page

def pricing_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Here is our pricing", size="9"),
            rx.text(
                "Click here to know our pricing",
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )
