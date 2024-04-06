import reflex as rx

class State(rx.State):
    """The app state."""
    
    # The current items that are in the list
    items = ["Writes code", "Sleep", "Go out"]
    
    def add_item(self, form_data: dict[str, str]):
        """Add a new item to the todo list."""
        
        new_item = form_data.get("new_item")
        if new_item:
            self.items.append(new_item)

    
    def clear_item(self, item: str):
        """Clears an item from the list

        Args:
            item (str): the todo list item
        """
        
        self.items.pop(self.items.index(item))

def todo_items(item : rx.Var[str]) -> rx.Component:
    """Render an item in the todo list
    
    Keyword arguments:
    item -- the todo list item
    Return: a single rendered todo list item
    """
    return rx.list_item(
        # Button to clear an item
        rx.icon_button(
            rx.icon(tag="check"),
            on_click=lambda : State.clear_item(item),
            margin="0 1em 1em 0",
        ),
        # Text of the item
        rx.text(item, as_="span"),
    )    

def todo_list() -> rx.Component:
    """ Renders the whole todo list """
    
    return rx.ordered_list(
        rx.foreach(State.items, lambda item: todo_items(item)),
    )

def new_item() -> rx.Component:
    """Render a new form

    Returns:
        A form to add a new itme ot the todo list
    """
    return rx.form(
        rx.hstack(
            rx.input.root(
                rx.input(
                    name="new_item",
                    placeholder="Add an item to the list",
                    bg="white",
                ),
                width="100%",
            ),
            rx.button("Add"),
        ),
        on_submit=State.add_item,
        reset_on_submit=True,
        width="100%",
    )

def index() -> rx.Component:
    """This will give us a view of the entire todo list

    Returns:
        Index of the todo app
    """
    rx.color_mode.button("Change"),
    return rx.container(
        rx.vstack(
            rx.heading("Todos"),
            new_item(),
            rx.divider(),
            todo_list(),
            bg=rx.color("gray", 7),
            margin_top="5em",
            margin_x="25vw",
            padding="1em",
            border_radius="0.5em",
            box_shadow=f"{rx.color('gray', 3, alpha=True)} 0px 1px 4px",
        ),
    )

app = rx.App()

app.add_page(index, title="Todo App")