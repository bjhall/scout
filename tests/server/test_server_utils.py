import tempfile
from scout.server.links import get_variant_links
from scout.server.utils import find_index
from scout.server.utils import append_safe


def test_get_variant_links(variant_obj):
    ## GIVEN a variant object without links
    assert "thousandg_link" not in variant_obj
    ## WHEN fetching the variant links
    links = get_variant_links(variant_obj)
    ## THEN check that links are returned
    assert "thousandg_link" in links


def test_find_index_bai(case_obj):

    # GIVEN a case with this type of alignment files
    # bam_file.bam
    # bam_file.bai
    with tempfile.TemporaryDirectory() as tmpdirname:
        with tempfile.NamedTemporaryFile(dir=tmpdirname, suffix=".bai") as idx:

            bam_file = idx.name.replace(".bai", ".bam")
            # THEN the find_index function should return the correct index file
            index = find_index(bam_file)
            assert index.endswith("bam.bai") is False
            assert index.endswith(".bai")


def test_find_index_bam_bai(case_obj):

    # GIVEN a case with this type of alignment files
    # bam_file.bam
    # bam_file.bam.bai
    with tempfile.TemporaryDirectory() as tmpdirname:
        with tempfile.NamedTemporaryFile(dir=tmpdirname, suffix="bam.bai") as idx:

            bam_file = idx.name.replace(".bai", "")
            # THEN the find_index function should return the correct index file
            index = find_index(bam_file)
            assert index.endswith("bam.bai")


def test_find_index_crai(case_obj):

    # GIVEN a case with this type of alignment files
    # bam_file.cram
    # bam_file.crai
    with tempfile.TemporaryDirectory() as tmpdirname:
        with tempfile.NamedTemporaryFile(dir=tmpdirname, suffix=".crai") as idx:

            cram_file = idx.name.replace(".crai", ".cram")
            # THEN the find_index function should return the correct index file
            index = find_index(cram_file)
            assert index.endswith("cram.crai") is False
            assert index.endswith(".crai")


def test_find_index_cram_crai(case_obj):

    # GIVEN a case with this type of alignment files
    # bam_file.cram
    # bam_file.cram.crai
    with tempfile.TemporaryDirectory() as tmpdirname:
        with tempfile.NamedTemporaryFile(dir=tmpdirname, suffix="cram.crai") as idx:

            cram_file = idx.name.replace(".crai", "")
            # THEN the find_index function should return the correct index file
            index = find_index(cram_file)
            assert index.endswith("cram.crai")


def test_append_safe_noExcept():
    ## GIVEN a simple dict with list
    d = {"a": [1]}

    ## WHEN calling append_safe
    append_safe(d, "a", 2)

    ## THEN append_safe() will append elem at index
    assert d == {"a": [1, 2]}


def test_append_safe_Except():
    ## GIVEN a simple dict with list
    d = {}

    ## WHEN calling append_safe() on a empty
    append_safe(d, "a", 2)

    ## THEN list.append exception is caught in try/except and
    ## program execution continues
    assert d == {"a": [2]}
