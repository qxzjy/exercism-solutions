DNA_RNA_TRANSCODE = str.maketrans("GCTA", "CGAU")

def to_rna(dna_strand: str ) -> str:
    """
    Determine the RNA complement of a given DNA sequence.
 
    :param dna_strand: str - the DNA sequence.
    :return: str - the RNA complement of the DNA sequence.
    """

    return dna_strand.translate(DNA_RNA_TRANSCODE)
    
    
