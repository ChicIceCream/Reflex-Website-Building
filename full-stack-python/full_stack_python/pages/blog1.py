import reflex as rx

from ..ui.base import base_page

def blog1_page() -> rx.Component:
    return base_page(
        rx.box(
            rx.vstack(
                rx.heading(
                    "Introduction to Supervised Learning:",
                    size="7",
                    # font_family="Cambria",
                ),
                rx.heading(
                    "A Beginner's Guide",
                    size="7",
                    # font_family="Cambria",
                ),
                rx.text(
                    """
                    Hey there, future data science wizards! 🌟 Ever wondered how Netflix seems to know \n
                    exactly what you want to watch next, or how your email filters out spam? The magic behind \n
                    these tech wonders is machine learning! Today, we're going to dive into one of its \n
                    coolest aspects: Supervised Learning. Get ready for a fun ride!
                    """,
                    align="left",
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
                ),
                rx.text(
                    """
                    We will build a simple classification model using the \n
                    famous Iris dataset later.
                    """,
                ),
                rx.heading(
                    """
                    So. What is Machine Learning?
                    """,
                    size="5",
                    weight="medium",
                ),
                rx.text(
                    '''
                    Machine learning is like teaching computers to learn from experience,\n
                    just like we humans do! Instead of programming specific instructions like a bunch of \n
                    if statements, we feed the machine a ton of data, and it figures out patterns and\n
                    makes decisions itself! In simple terms, machine learning is teaching your computer to \n
                    make decisions without being explicitly programmed to do so. Now thats how to \n
                    make your computer smart! 🧠
                    ''',
                    align="left",
                ),
                rx.heading(
                    """
                    What are some major types of Machine learning?
                    """,
                    size="5",
                    weight="medium",
                ),
                rx.text(
                    '''
                    Machine learning isn't a one-size-fits-all deal. There are three main types:

                    Supervised Learning: Learning from labeled data.
                    Unsupervised Learning: Finding patterns in unlabeled data.
                    Reinforcement Learning: Learning by trial and error.

                    ''',
                    align="left",
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
            max_width="600px",
        ),
    )
