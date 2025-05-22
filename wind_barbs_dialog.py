from PyQt5.QtWidgets import (QDialog, QLabel, QComboBox, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox, QColorDialog,
                             QGroupBox)
from PyQt5.QtGui import QColor
from qgis.core import QgsProject, QgsSvgMarkerSymbolLayer, QgsMarkerSymbol, QgsProperty, QgsSymbolLayer, QgsRuleBasedRenderer, QgsUnitTypes
import os

class WindBarbsDialog(QDialog):
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.setWindowTitle("QGIS Wind Barbs")

        # Section One: Select Layer
        self.layerLabel = QLabel("Select Layer:")
        self.layerCombo = QComboBox()
        layerLayout = QVBoxLayout()
        layerLayout.addWidget(self.layerLabel)
        layerLayout.addWidget(self.layerCombo)
        layerGroup = QGroupBox("Select Layer")
        layerGroup.setLayout(layerLayout)

        # Section Two: Select Fields
        self.uLabel = QLabel("U Component Field Name:")
        self.uField = QLineEdit()
        self.vLabel = QLabel("V Component Field Name:")
        self.vField = QLineEdit()
        self.unitLabel = QLabel("Wind Speed Unit:")
        self.unitCombo = QComboBox()
        self.unitCombo.addItems(["m/s", "km/hr", "knots"])
        fieldLayout = QVBoxLayout()
        fieldLayout.addWidget(self.uLabel)
        fieldLayout.addWidget(self.uField)
        fieldLayout.addWidget(self.vLabel)
        fieldLayout.addWidget(self.vField)
        fieldLayout.addWidget(self.unitLabel)
        fieldLayout.addWidget(self.unitCombo)
        fieldGroup = QGroupBox("Select Fields")
        fieldGroup.setLayout(fieldLayout)

        # Section Three: Select Style
        self.sizeLabel = QLabel("Size (Millimeters):")
        self.sizeEdit = QLineEdit("50")
        self.colorLabel = QLabel("Select Color (Hex):")
        self.colorEdit = QLineEdit("#000000")
        self.btnColor = QPushButton("Choose Color")
        self.btnColor.clicked.connect(self.chooseColor)
        self.lineWidthLabel = QLabel("Line Width (px):")
        self.lineWidthEdit = QLineEdit("2")
        styleLayout = QVBoxLayout()
        styleLayout.addWidget(self.sizeLabel)
        styleLayout.addWidget(self.sizeEdit)
        styleLayout.addWidget(self.colorLabel)
        styleLayout.addWidget(self.colorEdit)
        styleLayout.addWidget(self.btnColor)
        styleLayout.addWidget(self.lineWidthLabel)
        styleLayout.addWidget(self.lineWidthEdit)
        styleGroup = QGroupBox("Select Style")
        styleGroup.setLayout(styleLayout)

        # Main Layout
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(layerGroup)
        mainLayout.addWidget(fieldGroup)
        mainLayout.addWidget(styleGroup)

        self.btnApply = QPushButton("Apply Wind Barb Style")
        mainLayout.addWidget(self.btnApply)
        self.setLayout(mainLayout)

        self.populateLayers()
        self.btnApply.clicked.connect(self.applyWindBarbs)

    def chooseColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.colorEdit.setText(color.name())

    def populateLayers(self):
        self.layerCombo.clear()
        for layer in QgsProject.instance().mapLayers().values():
            if layer.type() == layer.VectorLayer and layer.geometryType() == 0:
                self.layerCombo.addItem(layer.name(), layer)

    def applyWindBarbs(self):
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        svg_dir = os.path.join(plugin_dir, 'resources', 'svg')

        layer = self.layerCombo.currentData()
        u_field = self.uField.text().strip()
        v_field = self.vField.text().strip()
        unit = self.unitCombo.currentText()
        color_hex = self.colorEdit.text().strip()
        try:
            line_width = float(self.lineWidthEdit.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid line width, please enter a numeric value.")
            return

        if not layer or not u_field or not v_field:
            QMessageBox.warning(self, "Input Error", "Please fill in the correct fields.")
            return

        # Conversion factors
        unit_factors = {"m/s": 1.94384, "km/hr": 0.539957, "knots": 1.0}
        coef = unit_factors.get(unit, 1.0)

        # root rule (no filter)
        root_rule = QgsRuleBasedRenderer.Rule(None)

        # Create Rule-based renderer of wind barbs
        wind_speed_levels = [0, 2] + list(range(5, 195, 5))
        wind_speed_thresholds = [(wind_speed_levels[i] + wind_speed_levels[i+1])/2 for i in range(len(wind_speed_levels)-1)]
        for i in range(len(wind_speed_thresholds)):
            wind_speed_threshold_lower_bound = 0 if i == 0 else wind_speed_thresholds[i-1]
            wind_speed_threshold_upper_bound = wind_speed_thresholds[i]
            wind_speed_level = wind_speed_levels[i]

            svg_path = os.path.join(svg_dir, f'{wind_speed_level}.svg')
            sym = QgsMarkerSymbol.createSimple({})
            sym.setSizeUnit(QgsUnitTypes.RenderPixels)
            svg_layer_rule = QgsSvgMarkerSymbolLayer(svg_path, float(self.sizeEdit.text().strip()))

            rotation_expr = f"(180/pi())*atan2(-\"{u_field}\", -\"{v_field}\") % 360"
            svg_layer_rule.setDataDefinedProperty(QgsSymbolLayer.PropertyAngle, QgsProperty.fromExpression(rotation_expr))

            svg_layer_rule.setFillColor(QColor(color_hex))
            svg_layer_rule.setStrokeColor(QColor(color_hex))
            svg_layer_rule.setStrokeWidth(line_width)
            svg_layer_rule.setStrokeWidthUnit(QgsUnitTypes.RenderPixels)

            sym.changeSymbolLayer(0, svg_layer_rule)

            filter_expr = f"sqrt(\"{u_field}\"^2 + \"{v_field}\"^2) * {coef} <= {wind_speed_threshold_upper_bound} AND sqrt(\"{u_field}\"^2 + \"{v_field}\"^2) * {coef} > {wind_speed_threshold_lower_bound}"
            rule = QgsRuleBasedRenderer.Rule(sym)
            rule.setFilterExpression(filter_expr)
            rule.setLabel(f"{wind_speed_level} kt")
            root_rule.appendChild(rule)

        renderer = QgsRuleBasedRenderer(root_rule)
        layer.setRenderer(renderer)
        layer.triggerRepaint()