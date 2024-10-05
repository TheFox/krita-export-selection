from krita import Krita, Extension
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

        # Ensure there is an active document.
        if not currentDocument:
            print('No active document found.')
            return

        currentLayer = currentDocument.activeNode()

        # Get the selection from the active document.
        selection = currentDocument.selection()

        # Ensure there is a selection in the document.
        if selection is None or selection.width() == 0 or selection.height() == 0:
            print('No selection found.')
            return

        (basePath, ext) = path.splitext(currentDocument.fileName())

        items = [
            basePath,
            currentLayer.name(),
            str(selection.width()) + 'x' + str(selection.height()),
        ]
        newPath = '_'.join(items) + '.png'

        application.action('copy_merged').trigger()
        application.action('paste_new').trigger()

        currentDocument = application.activeDocument()
        currentDocument.saveAs(newPath)

        application.action('file_close').trigger()
