import reflex as rx

from ..ui.base import base_page

def about_us() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("This page is about us", size="9"),
            rx.text(
                "Something about us ",
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )
