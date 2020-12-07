"""
mmic_docking
Component for molecular docking
"""

# Add imports here
from .mmic_docking import *
from . import components
from . import models

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
