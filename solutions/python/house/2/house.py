RHYME_START = "This is"
VERSES = [ " the horse and the hound and the horn that belonged to",
           " the farmer sowing his corn that kept",
           " the rooster that crowed in the morn that woke",
           " the priest all shaven and shorn that married",
           " the man all tattered and torn that kissed",
           " the maiden all forlorn that milked",
           " the cow with the crumpled horn that tossed",
           " the dog that worried",
           " the cat that killed",
           " the rat that ate",
           " the malt that lay in",
           " the house"]
RHYME_END = " that Jack built."

def recite(start_verse: int, end_verse: int) -> list[str]:
    """ Recite the nursery rhyme between two specifics verses.
 
    :param start_verse: int - the verse to start.
    :param end_verse: int - the verse to end.
    :return: list[str] - the nursery rhyme between the two verses.
    """
    rhyme = [(RHYME_START + "".join(VERSES[len(VERSES)-i:len(VERSES)]) + RHYME_END) for i in range(start_verse,end_verse+1)]
    
    return rhyme

