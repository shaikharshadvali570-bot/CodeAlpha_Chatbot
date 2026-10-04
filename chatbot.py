"""
PyChat — Basic Rule-Based Chatbot
A clean, beginner-friendly console assistant demonstrating core Python fundamentals:
functions, loops, string processing, and conditional logic.
"""


def clean_input(text):
    """Normalize input by trimming whitespace, lowercasing, and removing trailing punctuation."""
    cleaned = text.lower().strip()
    return cleaned.rstrip(".!?")


def display_welcome():
    """Print the initial banner and greeting."""
    print("=" * 50)
    print("             PyChat - Python Chatbot              ")
    print("=" * 50)
    print("\nHello! I'm PyChat, a simple rule-based chatbot.")
    print('Type "help" to see what I can do.')
    print('Type "bye" or "exit" to quit.\n')
    print("-" * 50)


def get_response(user_input):
    """
    Evaluate cleaned user input against predefined rules and return a tuple:
    (response_text, is_exit_flag)
    """
    if not user_input:
        return "Please type something so I can respond.", False

    # Exit rules
    if user_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!", True

    # Greeting rules
    elif user_input in ["hello", "hi", "hey", "good morning", "good afternoon"]:
        return "Hi! Nice to meet you.", False

    # Status rules
    elif user_input in ["how are you", "how are u", "how are you doing"]:
        return "I'm fine, thanks! How can I help you today?", False

    # Identity rules
    elif user_input in ["what is your name", "your name", "who are you"]:
        return "I'm PyChat, a simple Python rule-based chatbot.", False

    # Appreciation rules
    elif user_input in ["thank you", "thanks", "thx"]:
        return "You're welcome!", False

    # Help and commands rules
    elif user_input == "help":
        return (
            "I can respond to greetings, introduce myself, and answer a few basic questions.\n"
            'Type "commands" to view a list of recognized topics.',
            False,
        )

    elif user_input == "commands":
        return (
            "Available inputs you can try:\n"
            "  - hello / hi / hey\n"
            "  - how are you\n"
            "  - what is your name / who are you\n"
            "  - thank you / thanks\n"
            "  - help\n"
            "  - bye / exit / quit",
            False,
        )

    # Fallback rule for unknown inputs
    else:
        return "I'm not sure how to respond to that. Try typing \"help\" to see what I can do.", False


def chatbot():
    """Run the main conversation loop until an exit command is provided."""
    display_welcome()

    while True:
        try:
            raw_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\n\nSession interrupted.")
            break

        processed_input = clean_input(raw_input)
        response, should_exit = get_response(processed_input)

        print(f"\nPyChat: {response}")

        if should_exit:
            break

    print("\n" + "=" * 50)
    print("              Chat session ended                 ")
    print("=" * 50)


def main():
    """Application entry point."""
    chatbot()


if __name__ == "__main__":
    main()