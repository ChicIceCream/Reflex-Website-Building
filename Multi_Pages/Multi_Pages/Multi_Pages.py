"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from rxconfig import config

import reflex as rx

filename = f"{config.app_name}/{config.app_name}.py"


def index() -> rx.Component:
    return rx.center(
        rx.vstack(  
            rx.heading("Welcome to Task Master!", size="9"),
            rx.text("This is a simple task master"),
            rx.hstack(
                rx.form.root(
                    rx.form.field(
                        rx.form.label("Task"),
                        rx.form.control(
                            rx.input.input(
                                placeholder="Enter your task",
                                type="email",
                            ),
                            as_child=True,
                        ),
                        rx.form.submit(
                            rx.button(
                                "Add task",
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

def about():
    return rx.text("About Page")

def todo():
    return rx.center(
        rx.vstack(
            rx.heading(
                "TODO APP",
                size="9"
            ),
        rx.hstack(
            rx.heading(
                "Task",
                size="4",
            ),
            rx.heading(
                "Checked",
                size="4"
            ),
        spacing="9",
        ),
        ),
    )

app = rx.App()
app.add_page(index)
app.add_page(todo)
app.add_page(about)