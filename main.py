"""
main.py

This is the entry point of the AI Job Automation Assistant.
"""


def greet_user(name: str) -> str:
    """
    Build a welcome message for the user.

    Args:
        name: The name of the person using the program.

    Returns:
        A formatted greeting string.
    """
    return f"Hello, {name}! Your development environment is ready."


def main() -> None:
    """
    Program entry point.
    """
    message = greet_user("Future Software Engineer")
    print(message)


if __name__ == "__main__":
    main()