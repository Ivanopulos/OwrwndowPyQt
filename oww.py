from PyQt5 import QtCore, QtGui, QtWidgets

class Canvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
        self.image.fill(QtCore.Qt.transparent)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self.image)

    def mouseMoveEvent(self, event):
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtCore.Qt.black)
        painter.drawLine(self.last_point, event.pos())
        self.last_point = event.pos()
        self.update()

    def mousePressEvent(self, event):
        self.last_point = event.pos()

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas()
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.canvas)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.showMaximized()
    sys.exit(app.exec_())