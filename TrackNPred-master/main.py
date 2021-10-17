
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from view.view import TrackNPredView
from control.controller import Controller
from model.model import TnpModel

# import torch
# a = torch.rand(10,3)
# a = a.cuda()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()  #https://blog.csdn.net/kilotwo/article/details/79238545 界面设计
    # print("this is fine")

    controller = Controller()
    view = TrackNPredView()

    ## to get attributes
    view.setupUi(Dialog)
    model = TnpModel(controller)
    controller.setView(view)
    controller.setModel(model)

    # print("that is ok")
    #show ui
    Dialog.show()
    sys.exit(app.exec_())