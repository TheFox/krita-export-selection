from krita import *
#from PyQt5.QtWidgets import QFileDialog
from os import path

class ExportSelection(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction('exportSelection', 'Export Selection')
        action.triggered.connect(self.exportSelection)

    def exportSelection(self):
        application = Krita.instance()
        currentDocument = application.activeDocument()

        currentLayer = currentDocument.activeNode()

        #filePath = path.dirname(currentDocument.fileName())
        (basePath, ext) = path.splitext(currentDocument.fileName())

        items = [
            basePath,
            currentLayer.name(),
            str(currentLayer.selection().width()) + 'x' + str(currentLayer.selection().height()),
        ]
        newPath = '_'.join(items) + '.png'

        application.action('copy_merged').trigger()
        application.action('paste_new').trigger()
        #application.action('file_save_as').trigger()
        #application.action('file_close').trigger()

        currentDocument = application.activeDocument()
        currentDocument.saveAs(newPath)

        application.action('file_close').trigger()
