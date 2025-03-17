import sys
from pathlib import Path
import pytest
from variantAnnotator import main, resources

# Add the parent directory (project root) to sys.path using pathlib
project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))


def test_validate_genome_build_valid():
    assert main.validate_genome_build("GRCh37") == "GRCh37"
    assert main.validate_genome_build("GRCh38") == "GRCh38"

def test_validate_genome_build_invalid():
    with pytest.raises(ValueError):
        main.validate_genome_build("GRCh36")
