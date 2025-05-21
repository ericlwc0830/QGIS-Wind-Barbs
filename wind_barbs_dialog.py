from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from qgis.core import QgsProject, QgsSvgMarkerSymbolLayer, QgsMarkerSymbol, QgsProperty, QgsSymbolLayer, QgsRuleBasedRenderer
import os


class WindBarbsDialog(QDialog):
    def __init__(self, iface):
        super().__init__()
        self.iface = iface
        self.setWindowTitle("QGIS Wind Barbs")

        # Create widgets
        self.layerLabel = QLabel("Select Layer:")
        self.layerCombo = QComboBox()

        self.uLabel = QLabel("U Component Field Name:")
        self.uField = QLineEdit()

        self.vLabel = QLabel("V Component Field Name:")
        self.vField = QLineEdit()

        self.unitLabel = QLabel("Wind Speed Unit:")
        self.unitCombo = QComboBox()
        self.unitCombo.addItems(["m/s", "km/hr", "knots"])

        self.btnApply = QPushButton("Apply Wind Barb Style")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.layerLabel)
        layout.addWidget(self.layerCombo)
        layout.addWidget(self.uLabel)
        layout.addWidget(self.uField)
        layout.addWidget(self.vLabel)
        layout.addWidget(self.vField)
        layout.addWidget(self.unitLabel)
        layout.addWidget(self.unitCombo)
        layout.addWidget(self.btnApply)
        self.setLayout(layout)

        self.populateLayers()
        self.btnApply.clicked.connect(self.applyWindBarbs)

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
        wind_speed_thresholds = [(wind_speed_levels[i] + wind_speed_levels[i + 1])/2 for i in range(len(wind_speed_levels) - 1)]
        for i in range(len(wind_speed_thresholds)):
            # set wind speed threshold
            wind_speed_threshold_lower_bound = 0 if i == 0 else wind_speed_thresholds[i - 1]
            wind_speed_threshold_upper_bound = wind_speed_thresholds[i]
            wind_speed_level = wind_speed_levels[i]

            # create SVG marker symbol
            svg_path = os.path.join(svg_dir, f'{wind_speed_level}.svg')
            sym = QgsMarkerSymbol.createSimple({})
            svg_layer_rule = QgsSvgMarkerSymbolLayer(svg_path, 50)

            # set wind barb rotation
            rotation_expr = f"(180/pi())*atan2(-\"{u_field}\", -\"{v_field}\") % 360"
            svg_layer_rule.setDataDefinedProperty(QgsSymbolLayer.PropertyAngle, QgsProperty.fromExpression(rotation_expr))

            # set wind barb rule
            sym.changeSymbolLayer(0, svg_layer_rule)

            # set wind barb filter expression
            filter_expr = f"sqrt(\"{u_field}\"^2 + \"{v_field}\"^2) * {coef} <= {wind_speed_threshold_upper_bound} AND sqrt(\"{u_field}\"^2 + \"{v_field}\"^2) * {coef} > {wind_speed_threshold_lower_bound}"
            rule = QgsRuleBasedRenderer.Rule(sym)
            rule.setFilterExpression(filter_expr)
            rule.setLabel(f"{wind_speed_level} kt")
            root_rule.appendChild(rule)

        # apply rule-based renderer
        renderer = QgsRuleBasedRenderer(root_rule)
        layer.setRenderer(renderer)
        layer.triggerRepaint()
