from krita import Krita
from .export_selection import ExportSelection

Krita.instance().addExtension(ExportSelection(Krita.instance()))
