# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editorUI.ui'
#
# Created: Thu Dec 18 14:32:16 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName(_fromUtf8("Editor"))
        Editor.resize(529, 642)
        self.verticalLayout = QtGui.QVBoxLayout(Editor)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Editor)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.commodity_list = QtGui.QPlainTextEdit(Editor)
        self.commodity_list.setObjectName(_fromUtf8("commodity_list"))
        self.verticalLayout.addWidget(self.commodity_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.save = QtGui.QPushButton(Editor)
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout.addWidget(self.save)
        self.cancel = QtGui.QPushButton(Editor)
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Editor)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Editor.close)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        Editor.setWindowTitle(_translate("Editor", "Commodity Editor", None))
        self.label.setText(_translate("Editor", "Here you can add, remove or edit commodities. Duplicates will be removed and the entries will be automatically sorted once you click on Save. Please make sure there is only one commodity per line.", None))
        self.save.setText(_translate("Editor", "Save", None))
        self.cancel.setText(_translate("Editor", "Cancel", None))

