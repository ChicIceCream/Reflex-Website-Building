import reflex as rx
import asyncio


class State(rx.State):
    # The current question being asked.
    question: str

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]]

    async def answer(self):
        # Our chatbot is not very smart right now...
        answer = "I don't know!"
        self.chat_history.append((self.question, ""))
        self.question=''
        yield
        
        for i in range(len(answer)):
            # Pause to show the streaming effect
            await asyncio.sleep(0.1)
            # Adding one letter at a time
            self.chat_history[-1] = (
                self.chat_history[-1][0],
                answer[: i + 2],
            )
            yield
    
    def clear_chat(self):
        self.chat_history = []