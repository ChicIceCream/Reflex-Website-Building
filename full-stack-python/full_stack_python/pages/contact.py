import reflex as rx

from ..ui.base import base_page

def contact_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Contact us easily", size="9"),
            rx.text(
                "(9301276854) ",
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )
