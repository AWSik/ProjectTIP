import sys
import os

from PyQt5 import QtWidgets

import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnBrowse.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        if directory:
            for file_name in os.listdir(directory):
                self.listWidget.addItem(file_name)
