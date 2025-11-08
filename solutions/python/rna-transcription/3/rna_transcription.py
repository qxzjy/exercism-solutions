def to_rna(dna_strand: str ) -> str:
    """
    Determine the RNA complement of a given DNA sequence.
 
    :param dna_strand: str - the DNA sequence.
    :return: str - the RNA complement of the DNA sequence.
    """

    dna_rna_transcode = str.maketrans("GCTA", "CGAU")

    return dna_strand.translate(dna_rna_transcode)
    
    
