import os
from rich.console import Console
from rich.theme import Theme

def clear_screen():
    os.system('cls' if os == 'nt' else 'clear')

neon_genesis_theme = Theme(
    {
    "header": "bold black on bright_cyan",
    "option": "bright_green",
    "info": "bold cyan",
    "warning": "bold black on bright_yellow",
    "error": "bold black on bright_red",
    "success": "bold black on bright_green",
    "prompt": "bold magenta1",
    }
)
console = Console(theme=neon_genesis_theme)


def print_header(text):
    console.print(f"[header]{text}[/header]")

def print_option(text):
    console.print(f"[option]{text}[/option]")

def print_info(text):
    console.print(f"[info]{text}[/info]")

def print_warning(text):
    console.print(f"[warning]{text}[/warning]")

def print_error(text):
    console.print(f"[error]{text}[/error]")

def print_success(text):
    console.print(f"[success]{text}[/success]")

def input_prompt(text):
    return console.input(f"[prompt]{text}[/prompt]")

