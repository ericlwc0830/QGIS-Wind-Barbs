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
3. Select the point layer to which you want to apply wind barbs.
4. Select the corresponding field names for the U and V components.
5. Select the wind speed unit: m/s, km/hr, or knots.
6. Choose the size, color, and thickness of the wind barbs.
7. Click the **Apply Wind Barb Style** button, and the plugin will apply the corresponding wind barbs symbols based on the wind speed intervals (using rule-based rendering).

### Compatibility
- Tested on QGIS version 3.40, but this plugin does not use overly complex new features, so it should also run normally on QGIS version 3.0 and above.

### Author
- Author: ericlwc  
- Email: ericlun60313@gmail.com

### Version
- Version: 0.2.2:  Modified calm wind symbol size.
- Version: 0.2.1: Added a dropdown menu to select component field names, reducing the chance of user input errors.
- Version: 0.2.0: Added a new feature to set the size, color, and thickness of wind barbs.
- Version: 0.1.0: Initial release

### Disclaimer
The wind barbs symbols used in this plugin are modified from the related files of [svg-wind-barbs](https://github.com/qulle/svg-wind-barbs) and comply with its [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause).

## 中文版（Chinese Version）

### 介紹
QGIS Wind Barbs Plugin 可以將點狀向量資料依據風的兩個分量 (U、V) 設定為風標符號 (Wind Barbs)，協助使用者視覺化風的分布狀況。

### 功能
- 提供介面選擇欲套用風標圖示的圖層。
- 依使用者輸入的 U 與 V 風速分量欄位計算風速與風向。
- 自動依照設定之風速單位（m/s、km/hr、knots）進行轉換。
- 根據不同風向風速設定對應的風標圖示

### 安裝步驟
1. 將此 Repository 以 zip 檔案下載至本地。
2. 使用 QGIS 的外掛管理器使用 install from zip file 功能安裝外掛。
3. 安裝完成後，啟動 QGIS 並在外掛列表中找到 **QGIS Wind Barbs** 外掛，並啟用它。

### 使用方式
1. 在 QGIS 中載入點狀圖層，並確保該圖層具備以 m/s、km/hr 或 knots 表示的 U 與 V 風速分量的欄位。
2. 在 QGIS 的選單列中，選擇 **Plugins** > **Wind Barbs** > **Wind Barbs** 開啟外掛介面。
3. 從 **Select Layer** 下拉選單中選擇欲套用風標的點狀圖層。
4. 選擇對應的 U 與 V 分量欄位名稱。
5. 選擇風速單位：m/s、km/hr 或 knots。
6. 選擇風標的大小、顏色、粗細。
7. 點選 **Apply Wind Barb Style** 按鈕，外掛會依據各區間風速 (使用規則式渲染) 套用對應的風標圖示。

### 相容性
- 測試於 QGIS 3.40 版本，惟本外掛並未使用過於複雜的新功能，應也可正常運行於 QGIS 3.0 以上版本。

### 作者
- 作者：ericlwc  
- Email：ericlun60313@gmail.com

### 版本
- 版本：0.2.2：調整靜風符號大小。
- 版本：0.2.1：以下拉式選單選擇分量欄位名稱，降低使用者輸入錯誤機率。
- 版本：0.2.0：新增設定風標大小、顏色、粗細的功能。
- 版本：0.1.0：初始版本。

### 聲明

本外掛所使用的風標圖示，是微調自 [svg-wind-barbs](https://github.com/qulle/svg-wind-barbs) 的相關檔案，並遵循其 [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause) 授權條款。
