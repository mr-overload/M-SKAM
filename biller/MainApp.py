# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainApp.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1159, 772)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.item1 = QtWidgets.QPlainTextEdit(self.tab)
        self.item1.setGeometry(QtCore.QRect(160, 90, 241, 31))
        self.item1.setObjectName("item1")
        self.item2 = QtWidgets.QPlainTextEdit(self.tab)
        self.item2.setGeometry(QtCore.QRect(160, 170, 241, 31))
        self.item2.setObjectName("item2")
        self.item3 = QtWidgets.QPlainTextEdit(self.tab)
        self.item3.setGeometry(QtCore.QRect(160, 260, 241, 31))
        self.item3.setObjectName("item3")
        self.item4 = QtWidgets.QPlainTextEdit(self.tab)
        self.item4.setGeometry(QtCore.QRect(160, 340, 241, 31))
        self.item4.setObjectName("item4")
        self.qty4 = QtWidgets.QPlainTextEdit(self.tab)
        self.qty4.setGeometry(QtCore.QRect(470, 340, 241, 31))
        self.qty4.setObjectName("qty4")
        self.qty2 = QtWidgets.QPlainTextEdit(self.tab)
        self.qty2.setGeometry(QtCore.QRect(470, 170, 241, 31))
        self.qty2.setObjectName("qty2")
        self.qty1 = QtWidgets.QPlainTextEdit(self.tab)
        self.qty1.setGeometry(QtCore.QRect(470, 90, 241, 31))
        self.qty1.setObjectName("qty1")
        self.qty3 = QtWidgets.QPlainTextEdit(self.tab)
        self.qty3.setGeometry(QtCore.QRect(470, 260, 241, 31))
        self.qty3.setObjectName("qty3")
        self.price4 = QtWidgets.QPlainTextEdit(self.tab)
        self.price4.setGeometry(QtCore.QRect(800, 340, 241, 31))
        self.price4.setObjectName("price4")
        self.price2 = QtWidgets.QPlainTextEdit(self.tab)
        self.price2.setGeometry(QtCore.QRect(800, 170, 241, 31))
        self.price2.setObjectName("price2")
        self.price1 = QtWidgets.QPlainTextEdit(self.tab)
        self.price1.setGeometry(QtCore.QRect(800, 90, 241, 31))
        self.price1.setObjectName("price1")
        self.price3 = QtWidgets.QPlainTextEdit(self.tab)
        self.price3.setGeometry(QtCore.QRect(800, 260, 241, 31))
        self.price3.setObjectName("price3")
        self.Calculate = QtWidgets.QPushButton(self.tab)
        self.Calculate.setGeometry(QtCore.QRect(500, 550, 117, 32))
        self.Calculate.setObjectName("Calculate")
        self.Store = QtWidgets.QPushButton(self.tab)
        self.Store.setGeometry(QtCore.QRect(500, 610, 117, 32))
        self.Store.setObjectName("Store")
        self.Store.clicked.connect(lambda:self.store())
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(230, 20, 111, 22))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(550, 20, 111, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(860, 30, 111, 22))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(490, 460, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.total = QtWidgets.QLabel(self.tab)
        self.total.setGeometry(QtCore.QRect(570, 460, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.total.setFont(font)
        self.total.setObjectName("total")
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        TabWidget.addTab(self.tab1, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)
        self.show()
    def store(self):
        row1 = [self.item1.text(),self.qty1.text(),self.price1.text()]
        row2 = [self.item2.text(),self.qty2.text(),self.price2.text()]
        row3 = [self.item3.text(),self.qty3.text(),self.price3.text()]
        row4 = [self.item4.text(),self.qty4.text(),self.price4.text()]
        data = [row1 , row2 , row3 , row4]
        print(data)


    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.Calculate.setText(_translate("TabWidget", "Calculate"))
        self.Store.setText(_translate("TabWidget", "Store"))
        self.label.setText(_translate("TabWidget", "Item Name"))
        self.label_3.setText(_translate("TabWidget", "Qty."))
        self.label_4.setText(_translate("TabWidget", "Price"))
        self.label_2.setText(_translate("TabWidget", "Total"))
        self.total.setText(_translate("TabWidget", "0.0"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Tab 1"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Tab 2"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TabWidget()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
