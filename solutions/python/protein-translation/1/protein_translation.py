AMINO_ACID_CODONS = {
    "Methionine": ["AUG"],
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"],
    "STOP": ["UAA", "UAG", "UGA"],
}

CODON_AMINO_ACID = {c: p for p in AMINO_ACID_CODONS for c in AMINO_ACID_CODONS[p]}

def proteins(strand: str) -> list[str]:
    """ Translate a RNA strand into a list of amino acid.

    :param strand: str - a RNA strand in string format.
    :return: list[str] - the proteins contains into the RNA strand.
    """
    proteins = []
    
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        protein = CODON_AMINO_ACID[codon]
        
        if protein == "STOP":
            break
            
        proteins.append(protein)
        
    return proteins