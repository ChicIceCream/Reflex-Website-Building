
from rxconfig import config
import reflex as rx

def qa(question:str, answer:str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="centre", font_size="3em"),
        rx.box(answer, text_align="centre", font_size="3em"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )


def index() -> rx.Component:
    return rx.container(chat())



# def index() -> rx.Component:
#     return rx.container(
#         rx.box(
#             "Who is my friend?",
#             # put it on the right.
#             text_align="right",
#             font_size="5em"
#         ),
#         rx.box(
#             "It is Dhananjay Sharma!",
#             # lets put this on the left
#             text_align="left",
#             font_size="5em"
#         )
#     )

app = rx.App()
app.add_page(index)
