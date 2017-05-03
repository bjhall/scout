import logging

logger = logging.getLogger(__name__)

def parse_clnsig(acc, sig, revstat):
    """Get the clnsig information

    Args:
        acc(str): The clnsig accession number, raw from vcf
        sig(str): The clnsig significance score, raw from vcf
        revstat(str): The clnsig revstat, raw from vcf

    Returns:
        clnsig_accsessions(list): A list with clnsig accessions
    """

    clnsig_accsessions = []
    if acc:
        
        accessions = acc.split('|')
        significance = sig.split('|')
        revision_statuses= revstat.split('|')
        
        for i,annotation in enumerate(significance):
            clnsig_entry = {
                'value': int(annotation),
                'accession': accessions[i],
                'revstat': revision_statuses[i]
            }
            clnsig_accsessions.append(clnsig_entry)

    return clnsig_accsessions
