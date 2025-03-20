import pytest
from variantAnnotator import main, resources

def test_validate_genome_build_valid():
    assert main.validate_genome_build("GRCh37") == "GRCh37"
    assert main.validate_genome_build("GRCh38") == "GRCh38"

def test_validate_genome_build_invalid():
    with pytest.raises(ValueError):
        main.validate_genome_build("GRCh36")
