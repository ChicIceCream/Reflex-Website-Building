import reflex as rx

from ..ui.base import base_page

def blog1_page() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.heading("Introduction to Supervised Learning: A Beginner's Guide", size="8"),
            rx.text(
                """
                Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!
                """,
                align="center",
            ),
            rx.text(
                """
                Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!Hey there, future data science wizards! 🌟 Ever wondered how \n
                Netflix knows what you might want to watch next or how your email\n
                filters out spam? The magic behind these and many other tech wonders\n
                is machine learning. Today, we're diving into one of its most \n
                fascinating realms: supervised learning. Buckle up, because this\n
                is going to be fun!
                """,
                align="center",
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
