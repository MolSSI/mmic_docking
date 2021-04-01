"""
mmic_docking
Component for molecular docking
"""

# Add imports here
from . import components
from . import models

# For testing dummy component
_mainComponent = components.dummy_component.DockDummyComponent

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
