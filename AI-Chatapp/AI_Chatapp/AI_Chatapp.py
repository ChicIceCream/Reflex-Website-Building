from rxconfig import config
import reflex as rx
from AI_Chatapp import style

def qa(question:str, answer:str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="centre", style=style.question_style),
        rx.box(answer, text_align="centre", style=style.answer_style),
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

def question_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Ask me a question : "),
        rx.button("ASK"),
    )


def index() -> rx.Component:
    return rx.container(
        chat(),
        question_bar(),
        )



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
