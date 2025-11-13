def distance(strand_a: list[str], strand_b: list[str]) -> int:
    """Calculate the Hamming distance between two DNA strands.

    :param strand_a: listr[str] - the original DNA strand.
    :param strand_b: listr[str] - the replicate DNA strand.
    :return: int - the Hamming distance.
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
        
    return sum(char_a != char_b for char_a, char_b in zip(strand_a, strand_b))