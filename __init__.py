"""
Photo Deduplicator - A tool to find and remove duplicate or similar images.
"""

__version__ = "0.1.0"

# Import main components
from .image_comparator import ImageComparator, ImagePair
from .ui.main_window import MainWindow

__all__ = [
    "ImageComparator",
    "ImagePair",
    "MainWindow",
    "__version__",
]
