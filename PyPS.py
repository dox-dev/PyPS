#!/bin/bash

import sys

class print():
    """
        === Python Pretty Strings | Print Function ===

        Args:
            string: This is the string that will be printed out.
            text: This is a text color param.
            background: This is a bacground color param.
            style: This is a text style param.
            end: This is a end-line param.

        Text Colors:
            white, black, red, green, blue, yellow, magenta, cyan

        Background Colors:
            none, white, black, red, green, blue, yellow, magenta, cyan

        Text Styles:
            none, bold, italic, underline, inverted
    """
    def __init__(self, string, text="white", background="none", style="none", end="\n"):
        if (text != "white" and background == "none"):
            background = "black"
        self.string = string
        self.text = text
        self.background = background
        self.style = style
        self.end = end
        self.pretty_string()
    def pretty_string(self):
        styles = {
            "none": "0;",
            "bold": "1;",
            "italic": "3;",
            "underline": "4;",
            "inverted": "5;"
        }

        text_colors = {
            "black": "30;",
            "red": "31;",
            "green": "32;",
            "yellow": "33;",
            "blue": "34;",
            "magenta": "35;",
            "cyan": "36;",
            "white": "37;"
        }

        background_colors = {
            "none": "0m",
            "black": "40m",
            "red": "41m",
            "green": "42m",
            "yellow": "43m",
            "blue": "44m",
            "magenta": "45m",
            "cyan": "46m",
            "white": "47m"
        }

        try:
            sys.stdout.write('\x1b[' + styles[self.style] + text_colors[self.text] + background_colors[self.background] + str(self.string) + self.end + '\x1b[0m')
        except:
            sys.stdout.write("  Usage: print(\'String\' text=\'Text Color\' background=\'Background Color\' style=\'Text Style\' end=\'Break-Line\'")

if __name__ == "__main__":
    print()