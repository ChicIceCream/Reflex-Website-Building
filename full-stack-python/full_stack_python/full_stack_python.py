"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page

from . import pages, navigation

class State(rx.State):
    """The app state."""
    label = "Welcome to Chic's Den!"
    
    def handle_title_input_change(self, value: str):
        """Handle title input change."""
        self.label = value

def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.input(
                on_change=State.handle_title_input_change, 
                placeholder="Try typing!",
                size="3",
                ),
            rx.link(
                rx.button("Click here to Sign Up!!"),
                href='https://avuy0vjlte4.typeform.com/to/eJ27V0qL',
            ),
            rx.link(
                rx.button("Link to my first blog when I make it!!"),
                href=navigation.routes.BLOG1_ROUTE,
            ), 
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )

style = {
    "font_family": "source-serif-pro, Georgia, Cambria, 'Times New Roman', Times, serif",
}

app = rx.App(
    style = {
    "font_family": "source-serif-pro, Georgia, Cambria, 'Times New Roman', Times, serif",
    }
)

app.add_page(index)

# app.add_page(pages.about_page, 
#             route=navigation.routes.ABOUT_US_ROUTE
#             )
# app.add_page(pages.contact_page, 
#             route=navigation.routes.CONTACT_US_ROUTE
#             )
# app.add_page(pages.pricing_page, 
#             route=navigation.routes.PRICING_ROUTE
#             )
app.add_page(pages.blog1_page,
            route=navigation.routes.BLOG1_ROUTE
            )