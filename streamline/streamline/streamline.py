"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    def analyze_code():
        code = rx.get_state("user_code")
        # Placeholder for embedding conversion and AI analysis
        rx.set_state("ai_suggestion", f"AI suggests refactoring this code: {code[:100]}...")


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("AI-Powered Code Improvement"),
            rx.text_area(
                placeholder="Paste your code here...", 
                rows='10',
                cols='50',
                id="user_code"
                ),
            align='center'
    ),
    )


app = rx.App()
app.add_page(index)
