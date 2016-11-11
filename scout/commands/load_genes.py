#!/usr/bin/env python
# encoding: utf-8
"""
load_hgnc.py

Build a file with genes that are based on hgnc format.
Parses ftp://ftp.ebi.ac.uk/pub/databases/genenames/new/tsv/hgnc_complete_set.txt,
ftp.broadinstitute.org/pub/ExAC_release//release0.3/functional_gene_constraint/
and a biomart dumb from ensembl with
'Gene ID' 'Chromosome' 'Gene Start' 'Gene End' 'HGNC symbol'

The hgnc file will determine which genes that are added and most of the meta information.
The ensembl gene file will add coordinates and the exac file will add pLi scores.

Created by Måns Magnusson on 2015-01-14.
Copyright (c) 2015 __MoonsoInc__. All rights reserved.

"""
from codecs import open
import gzip
import logging

import click

from scout.load import load_hgnc_genes
from scout.resources import (hgnc_path, exac_path, transcripts_path, 
                             hpogenes_path)


from . import get_file_handle

logger = logging.getLogger(__name__)

@click.command()
@click.option('--hgnc',
                type=click.Path(exists=True),
                default=hgnc_path,
                help="Path to hgnc file",
)
@click.option('--ensembl',
                type=click.Path(exists=True),
                default=transcripts_path,
                help="Path to ensembl transcripts file",
)
@click.option('--exac',
                type=click.Path(exists=True),
                default=exac_path,
                help="Path to exac gene file",
)
@click.option('--hpo',
                type=click.Path(exists=True),
                default=hpogenes_path,
                help="Path to HPO gene file",
)
@click.pass_context
def genes(ctx, hgnc, ensembl, exac, hpo):
    """
    Load the hgnc aliases to the mongo database.
    """
    adapter=ctx.obj['adapter']

    if not (hgnc and ensembl and exac and hpo):
        logger.info("Please provide all gene files")
        ctx.abort()

    logger.info("Loading hgnc file from {0}".format(hgnc))
    hgnc_handle = get_file_handle(hgnc)
    
    logger.info("Loading ensembl transcript file from {0}".format(
                ensembl))
    ensembl_handle = get_file_handle(ensembl)
    
    logger.info("Loading exac gene file from {0}".format(
                exac))
    exac_handle = get_file_handle(exac)
    
    logger.info("Loading HPO gene file from {0}".format(
                hpo))
    hpo_handle = get_file_handle(hpo)
    
    load_hgnc_genes(
        adapter=adapter,
        ensembl_lines=ensembl_handle, 
        hgnc_lines=hgnc_handle, 
        exac_lines=exac_handle,
        hpo_lines=hpo_handle
    )