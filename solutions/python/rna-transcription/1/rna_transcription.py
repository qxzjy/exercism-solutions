DNA_RNA_TRANSCODE = {"G": "C",
                      "C": "G",
                      "T": "A",
                      "A": "U"}


def to_rna(dna_strand: str ) -> str:
    """
    Determine the RNA complement of a given DNA sequence.
 
    :param dna_strand: str - the DNA sequence.
    :return: str - the RNA complement of the DNA sequence.
    """
    
    return "".join(DNA_RNA_TRANSCODE[letter] for letter in dna_strand)
    
    
