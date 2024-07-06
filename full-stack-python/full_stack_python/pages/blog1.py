import reflex as rx

from ..ui.base import base_page

def blog1_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("What is Supervised Learning?", size="9"),
            rx.text(
                """
                Supervised learning is a type of machine learning 
                where the model is trained on a labeled dataset. 
                """,
            ),
            rx.code(
                """
                import sklearn as sk\n 
                import the world!\n
                """,
                lang="python",
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )
