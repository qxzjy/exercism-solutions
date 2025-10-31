"""Functions to manage a users shopping cart items."""
from typing import Iterable

def add_item(current_cart: dict[str,int], items_to_add: Iterable[str]) -> dict[str, int]:
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item]=current_cart.setdefault(item,0)+1
        
    return current_cart


def read_notes(notes: Iterable[str]) -> dict[str]:
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return dict.fromkeys(notes, 1)


def update_recipes(ideas: dict[str, dict[str, int]], recipe_updates: Iterable) -> dict[str, dict[str, int]]:
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
        
    return ideas.update(recipe_updates) or ideas


def sort_entries(cart: dict)-> dict:
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart: dict[str,int], aisle_mapping: dict[str, bool]) -> dict[str, list[int, str, bool]]:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = dict()
    
    for key, value in cart.items():
        fulfillment_cart[key] = list((value,))+aisle_mapping[key]

    return dict(reversed(sorted(fulfillment_cart.items())))


def update_store_inventory(fulfillment_cart: dict[str, list[int, str, bool]], store_inventory: dict[str, list[int, str, bool]]) -> dict[str, list[int, str, bool]]:
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    return { x[0] :[x[1][0] - fulfillment_cart.get(x[0], [0])[0] or "Out of Stock"] + [x[1][1]] + [x[1][2]] for x in store_inventory.items()}
