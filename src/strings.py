"""
String utility functions for common text manipulation tasks.
"""


def capitalize_words(text):
    """Capitalizes the first letter of each word in a string."""
    return text.title()


def reverse_string(text):
    """Returns the reversed version of a string."""
    return text[::-1]


def truncate(text, max_length, suffix="..."):
    """Truncates text to max_length characters, appending suffix if cut."""
    if len(text) <= max_length:
        return text
    return text[: max_length - len(suffix)] + suffix


def slugify(text):
    """Converts a string to a URL-friendly slug (lowercase, hyphens)."""
    return text.strip().lower().replace(" ", "-")
