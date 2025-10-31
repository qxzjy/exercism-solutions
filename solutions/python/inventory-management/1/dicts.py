"""Functions to keep track and alter inventory."""


def create_inventory(items: list[str]) -> dict[str, int]:
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """

    return {i: items.count(i) for i in items}


def add_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    items = create_inventory(items)
    keys = set(list(inventory.keys()) + list(items.keys()))
    
    return {key: inventory.get(key, 0) + items.get(key, 0) for key in keys}


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    
    return {key: 0 if (new := value - items.count(key)) < 0 else new for key, value in inventory.items()}


def remove_item(inventory: dict[str, int], item: str) -> dict[str, int]:
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        del inventory[item]
        
    return inventory


def list_inventory(inventory: dict[str, int]) -> list[tuple[str, int]]:
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

    return [(key, value) for (key, value) in inventory.items() if value > 0]