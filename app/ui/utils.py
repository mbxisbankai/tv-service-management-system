import os
from rich.console import Console
from rich.theme import Theme
from rich.table import Table

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

#Table functions

def display_subscriptions(subscriptions):
    sub_table = Table(title="Subscriptions List")

    sub_table.add_column("ID", style="cyan", no_wrap=True)
    sub_table.add_column("Provider Name", style="magenta")
    sub_table.add_column("Price", justify="right", style="bright_cyan")
    sub_table.add_column("Subscription Date", style="magenta")
    sub_table.add_column("Expiry Date", style="magenta")
    sub_table.add_column("Customer ID", style="bright_green")

    for sub in subscriptions:
        sub_table.add_row(
            str(sub.id),
            sub.provider_name,
            f"${sub.price:.2f}",
            sub.sub_date.strftime("%Y-%m-%d"),
            sub.exp_date.strftime("%Y-%m-%d"),
            str(sub.customer_id)
        )
    console.print(sub_table)

def display_providers(providers):

    providers_table = Table(title="Providers List")
    providers_table.add_column("Provider ID", style="cyan", no_wrap=True)
    providers_table.add_column("Provider Name", style="magenta")
    providers_table.add_column("Tagline", justify="right", style="bright_cyan")

    for provider in providers:
        providers_table.add_row(str(provider.id), provider.name, provider.tagline)

    console.print(providers_table)

def display_customers(customers):
    customers_table = Table(title="Customers List")
    customers_table.add_column("Customer ID", style="cyan", no_wrap=True)
    customers_table.add_column("Customer Name", style="magenta")

    for customer in customers:
        customers_table.add_row(str(customer.id), customer.name)

    console.print(customers_table)
