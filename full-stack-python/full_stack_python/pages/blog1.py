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
                """,
                lang="python",
            ),
            rx.text(
                """
                This is one of the most important line of code in machine learning!
                
                """,
            ),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )
