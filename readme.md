# QGIS Wind Barbs Plugin

## English

### Introduction

QGIS Wind Barbs Plugin can set wind barbs symbols based on the two components of wind (U, V) for point vector data, helping users visualize the distribution of wind.

### Features
- Provides an interface to select the layer to which the wind barbs symbols will be applied.
- Calculates wind speed and direction based on the U and V wind speed component fields entered by the user.
- Automatically converts according to the set wind speed unit (m/s, km/hr, knots).
- Sets the corresponding wind barbs symbols according to different wind direction and speed settings.

### Installation Steps
1. Download this repository as a zip file to your local machine.
2. Use the QGIS plugin manager to install the plugin using the "Install from zip file" feature.
3. After installation, start QGIS and find the **QGIS Wind Barbs** plugin in the plugin list, and enable it.

### Usage
1. Load a point vector layer in QGIS, ensuring that the layer has fields for U and V wind speed components represented in m/s, km/hr, or knots.
2. In the QGIS menu bar, select **Plugins** > **Wind Barbs** > **Wind Barbs** to open the plugin interface.
3. From the **Select Layer** dropdown menu, select the point layer to which you want to apply wind barbs.
4. Enter the corresponding field names for the U and V components.
5. Select the wind speed unit: m/s, km/hr, or knots.
6. Click the **Apply Wind Barb Style** button, and the plugin will apply the corresponding wind barbs symbols based on the wind speed intervals (using rule-based rendering).

### Further Style Changes

If you want to further adjust the style of the wind barbs on the layer (e.g., size, color, opacity), please:
1. Select the layer in the layer panel.
2. Right-click and select Properties.
3. Check the Symbology tab.
4. Press Ctrl+A to select all Labels.
5. Right-click to choose Change Color, Change Size, or Change Opacity to adjust the color, size, or opacity.

### Compatibility
- Tested on QGIS version 3.40, but this plugin does not use overly complex new features, so it should also run normally on QGIS version 3.0 and above.

### Author
- Author: ericlwc  
- Email: ericlun60313@gmail.com

### Disclaimer
The wind barbs symbols used in this plugin are modified from the related files of [svg-wind-barbs](https://github.com/qulle/svg-wind-barbs) and comply with its [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause).

## Chinese

### 介紹
QGIS Wind Barbs Plugin 可以將點狀向量資料依據風的兩個分量 (U、V) 設定為風標符號 (Wind Barbs)，協助使用者視覺化風的分布狀況。

### 功能
- 提供介面選擇欲套用風標圖示的圖層。
- 依使用者輸入的 U 與 V 風速分量欄位計算風速與風向。
- 自動依照設定之風速單位（m/s、km/hr、knots）進行轉換。
- 根據不同風向風速設定對應的風標圖示

### 安裝步驟
1. 將此 Repository 以 zip 檔案下載至本地。
2. 使用 QGIS 的插件管理器使用 install from zip file 功能安裝插件。
3. 安裝完成後，啟動 QGIS 並在插件列表中找到 **QGIS Wind Barbs** 插件，並啟用它。

### 使用方式
1. 在 QGIS 中載入點狀圖層，並確保該圖層具備以 m/s、km/hr 或 knots 表示的 U 與 V 風速分量的欄位。
2. 在 QGIS 的菜單列中，選擇 **Plugins** > **Wind Barbs** > **Wind Barbs** 開啟插件介面。
3. 從 **Select Layer** 下拉選單中選擇欲套用風標的點狀圖層。
4. 輸入 U 與 V 分量對應的欄位名稱。
5. 選擇風速單位：m/s、km/hr 或 knots。
6. 點選 **Apply Wind Barb Style** 按鈕，插件會依據各區間風速 (使用規則式渲染) 套用對應的風標圖示。

### 進一步更改樣式

若要進一步調整圖層風標的樣式（例如大小、顏色、透明度），請：
1. 在圖層面板選定該圖層
2. 右鍵點選 Properties 
3. 查看 Symbology 標籤
4. 按 Ctrl+A 全選所有的Label
5. 右鍵選擇 Change Color、Change Size 或 Change Opacity 來調整顏色、大小或透明度。

### 相容性
- 測試於 QGIS 3.40 版本，惟本插件並未使用過於複雜的新功能，應也可正常運行於 QGIS 3.0 以上版本。

### 作者
- 作者：ericlwc  
- Email：ericlun60313@gmail.com

### 聲明

本插件所使用的風標圖示，是微調自 [svg-wind-barbs](https://github.com/qulle/svg-wind-barbs) 的相關檔案，並遵循其 [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause) 授權條款。
