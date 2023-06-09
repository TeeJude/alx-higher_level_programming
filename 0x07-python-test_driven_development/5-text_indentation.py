#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text indentation function."""


def text_indentation(text):
    """Print texts with two new lines after these characters '.', '?', and ':'.

    Args:
        text (string): Text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    t = 0
    while t < len(text) and text[t] == ' ':
        t += 1

    while t < len(text):
        print(text[t], end="")
        if text[t] == "\n" or text[t] in ".?:":
            if text[t] in ".?:":
                print("\n")
            t += 1
            while t < len(text) and text[t] == ' ':
                t += 1
            continue
        t += 1
