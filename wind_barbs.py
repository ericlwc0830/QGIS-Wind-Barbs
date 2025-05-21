from PyQt5.QtWidgets import QAction
from qgis.core import QgsProject
from .wind_barbs_dialog import WindBarbsDialog

class WindBarbsPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.action = None
        self.dlg = None

    def initGui(self):
        self.action = QAction("QGIS Wind Barbs", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addPluginToMenu("&QGIS Wind Barbs", self.action)

    def unload(self):
        self.iface.removePluginMenu("&QGIS Wind Barbs", self.action)

    def run(self):
        self.dlg = WindBarbsDialog(self.iface)
        self.dlg.show()