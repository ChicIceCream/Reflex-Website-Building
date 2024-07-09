import reflex as rx

from ..ui.base import base_page

def blog1_page() -> rx.Component:
    return base_page(
        rx.box(
            rx.vstack(
                rx.heading(
                    "Introduction to Supervised Learning:",
                    size="7",
                    font_family="Cambria",
                ),
                rx.heading(
                    "A Beginner's Guide",
                    size="7",
                    font_family="Cambria",
                ),
                rx.text(
                    """
                    Hey there, future data science wizards! 🌟 Ever wondered how \n
                    Netflix knows what you might want to watch next or how your email\n
                    filters out spam? The magic behind these and many other tech wonders\n
                    is machine learning. Today, we're diving into one of its most \n
                    fascinating realms: supervised learning. Buckle up, because this\n
                    is going to be fun!
                    """,
                    align="left",
                    font_family="Cambria",
                ),
                rx.code(
                    """
                    import sklearn as sk\n 
                    """,
                    lang="python",
                    variant="outline",
                ),
                rx.text(
                    """
                    This is one of the most important line of code in machine learning!
                    """,
                    font_family="Cambria",
                ),
                rx.text(
                    """
                    We will build a simple classification model using the \n
                    famous Iris dataset later on.
                    """,
                    font_family="Cambria",
                ),
                rx.heading(
                    """
                    What is Machine Learning?
                    """,
                    size="5",
                    weight="medium",
                    font_family="Cambria",
                ),
                rx.text(
                    '''
                    Machine learning is like teaching computers to learn from experience,\n
                    just like humans do. Instead of programming specific instructions,\n
                    we feed the machine a ton of data, and it figures out patterns and\n
                    makes decisions. From recommending your next favorite show to \n
                    spotting a fraudulent transaction, machine learning is the secret \n
                    sauce.
                    ''',
                    align="left",
                    font_family="Cambria",
                ),
                spacing="5",
                align="center",
                justify="start",
                min_height="85vh",
            ),
            # overflow="fixed",/
            # width="80%",
            # max_width="80%",
            align="center",
            margin="0 auto",
            max_width="550px",
        ),
    )
