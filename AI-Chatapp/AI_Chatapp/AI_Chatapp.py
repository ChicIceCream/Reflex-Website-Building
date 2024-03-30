from rxconfig import config
import reflex as rx
from AI_Chatapp import style
from AI_Chatapp.state import TutorialState

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            TutorialState.chat_history,
            lambda messages: qa(messages[0], messages[1])
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=TutorialState.question,
            placeholder="Ask a question",
            on_change=TutorialState.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask", 
            on_click=TutorialState.answer,
            style=style.button_style,
        ),
        # rx.button(
        #     "Clear Chat",
        #     on_click=TutorialState.clear_chat,
        #     style=style.button_style,
        # )
    )


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center",
        )
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
