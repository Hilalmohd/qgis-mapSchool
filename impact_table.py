from qgis.PyQt. QtWidgets import *
from .impact_table_dialoge import Ui_dlgImpact


class DlgTable(QDialog, Ui_dlgImpact):
    def __init__(self):
        super(DlgTable,self).__init__()
        self.setupUi(self)

        self.tblImpact.setColumnWidth(1, 175)