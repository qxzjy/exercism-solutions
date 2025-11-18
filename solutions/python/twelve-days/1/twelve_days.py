DAYS = ["first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth"]

GIFTS = ["a Partridge in a Pear Tree",
         "two Turtle Doves",
         "three French Hens",
         "four Calling Birds",
         "five Gold Rings",
         "six Geese-a-Laying",
         "seven Swans-a-Swimming",
         "eight Maids-a-Milking",
         "nine Ladies Dancing",
         "ten Lords-a-Leaping",
         "eleven Pipers Piping",
         "twelve Drummers Drumming"]

VERSE = "On the {} day of Christmas my true love gave to me: {}."

def oxford_join(items: list[str]) -> str:
    """
    Joins a list of items with commas in the Oxford style.
 
    Example:
 
       >> oxford_join(["a", "b", "c"])
       'a, b, and c'
    """
    if len(items) == 1:
        return items[0]
        
    return ", ".join(items[:-1]) + ", and " + items[-1]

    
def verse(num: int) -> str:
    """
    Return an individual verse of The Twelve Days of Christmas.
    """
    day = num - 1
    
    return VERSE.format(DAYS[day], oxford_join(GIFTS[day::-1]))

    
def recite(start: int, end: int) -> list[str]:
    """
    Recite The Twelve Days of Christmas from the start to the end verse.
    """
    
    return [verse(num) for num in range(start, end + 1)]