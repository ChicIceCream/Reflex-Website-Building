import reflex as rx

class Up_Down_State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1
