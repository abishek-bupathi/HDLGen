import os
import shutil
import sys
#import webbrowser
from xml.dom import minidom
import markdown as md

#from PySide2.QtCore import QUrl
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *

HELP_DOC_FILE_PATH = "./Help/help.md"
OLD_HELP_DOC_FILE_PATH = "./Help/help(old).md"
HELP_DOC_FILE_DIR = "./Help/"

class Help(QWidget):

    def __init__(self):
        super().__init__()

        self.uploadButton = QPushButton("Upload Help doc")

        # self.webEngineView = QWebEngineView()

        self.markdown_view = QTextEdit(readOnly=True)
        self.mainLayout = QVBoxLayout()

        self.setup_ui()

    def setup_ui(self):

        # Writing xml file
        with open(HELP_DOC_FILE_PATH, "r") as f:
           doc = md.markdown(f.read(),  extensions=['fenced_code', 'codehilite', 'tables', 'attr_list'])

        #self.webview = HtmlView()
        #self.webview.setHtml(doc)
        self.markdown_view.setHtml(doc)
        self.uploadButton.clicked.connect(self.update_help_doc)
        self.mainLayout.addWidget(self.uploadButton, alignment=Qt.AlignRight)
        self.mainLayout.addWidget(self.markdown_view)
        #self.mainLayout.addWidget(self.webview)
        self.setLayout(self.mainLayout)

    def update_help_doc(self):
        custom_doc_path= QFileDialog.getOpenFileName(self, "Select the Help document XML File", filter="Markdown (*.md)")
        if os.path.exists(OLD_HELP_DOC_FILE_PATH):
            os.remove(OLD_HELP_DOC_FILE_PATH)
        os.rename(HELP_DOC_FILE_PATH, OLD_HELP_DOC_FILE_PATH)
        shutil.copyfile(custom_doc_path[0], HELP_DOC_FILE_PATH)
        self.uploadButton.clicked.disconnect(self.update_help_doc)
        self.mainLayout.removeWidget(self.uploadButton)
        self.mainLayout.removeWidget(self.markdown_view)
        self.setup_ui()


class HelpDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("New IO Port")
        # self.webEngineView = QWebEngineView()

        self.markdown_view = QTextEdit(readOnly=True)
        self.mainLayout = QVBoxLayout()
        self.setFixedSize(700, 500)
        self.setup_ui()

    def setup_ui(self):

        # Writing xml file
        with open(HELP_DOC_FILE_PATH, "r") as f:
           doc = md.markdown(f.read(),  extensions=['fenced_code', 'codehilite', 'tables', 'attr_list'])

        #self.webview = HtmlView()
        #self.webview.setHtml(doc)
        self.markdown_view.setHtml(doc)
        self.mainLayout.addWidget(self.markdown_view)
        #self.mainLayout.addWidget(self.webview)
        self.setLayout(self.mainLayout)


"""
class WebEnginePage(QWebEnginePage):
    def acceptNavigationRequest(self, url,  _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            QDesktopServices.openUrl(url);
            return False
        return True

class HtmlView(QWebEngineView):
    def __init__(self, *args, **kwargs):
        QWebEngineView.__init__(self, *args, **kwargs)
        self.setPage(WebEnginePage(self))
"""



