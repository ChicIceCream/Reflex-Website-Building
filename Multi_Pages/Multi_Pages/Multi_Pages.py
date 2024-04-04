"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


def index() -> rx.Component:
    return rx.center(
        rx.vstack(  
            rx.heading("Welcome to Task Master!", size="9"),
            rx.text("This is a simple form"),
            rx.hstack(
                rx.form.root(
                    rx.form.field(
                        rx.form.label("Task"),
                        rx.form.control(
                            rx.input.input(
                                placeholder="Enter your task!",
                                type="email",
                            ),
                            as_child=True,
                        ),
                        rx.form.submit(
                            rx.button(
                                "Add task!",
                                rx.icon(tag="plus"),
                                radius="full",
                                size="2",
                                on_click=rx.window_alert("Task added"),
                        ),
                            as_child=True,
                    ),
                ),
                    reset_on_submit=True,
            ),
            ),
            rx.checkbox(
                "Check me!",
                default_checked=False,
                spacing="2",
                color_scheme="bronze",
                size="3",
                variant="soft",
                # on_change=State.allow
            ),
            align="center",
            spacing="7",
            font_size="2em",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
