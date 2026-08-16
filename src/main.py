"""
main.py

This is the entry point of the AI Job Automation Assistant.
"""

from config import settings


def greet_user(name: str) -> str:
    """
    Build a welcome message for the user.
    """
    return f"Hello, {name}! Your development environment is ready."


def main() -> None:
    """
    Program entry point.
    """
    try:
        settings.validate()
    except ValueError as error:
        print(f"Configuration error: {error}")
        return

    message = greet_user("Future Software Engineer")
    print(message)
    print(f"Debug mode is: {settings.DEBUG_MODE}")
    print(f"Log level is: {settings.LOG_LEVEL}")
    print(f"Max retries is: {settings.MAX_RETRIES}")


if __name__ == "__main__":
    main()