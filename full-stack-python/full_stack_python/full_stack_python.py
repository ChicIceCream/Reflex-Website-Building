"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from .ui.base import base_page

from . import pages, navigation

class State(rx.State):
    """The app state."""
    label = "Welcome to Chic's Den!"
    
    def handle_title_inpput_change(self, value: str):
        """Handle title input change."""
        self.label = value

def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.input(
                on_change=State.handle_title_inpput_change, 
                placeholder="Enter a title...",
                size="3",
                ),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="3",
            ),
            rx.link(
                rx.button("About Us!"),
                href='/about',
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
app.add_page(pages.about_us, 
            route=navigation.routes.ABOUT_US_ROUTE
            )