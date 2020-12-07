"""
Unit and regression test for the mmic_docking package.
"""

# Import package, test suite, and other packages as needed
import mmic_docking
import pytest
import sys


def test_mmic_docking_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mmic_docking" in sys.modules
