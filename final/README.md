# Flask 機器學習展示專案

這是一個使用 Flask 框架建立的互動式機器學習展示網站，包含線性迴歸和 KNN 分類演算法的視覺化展示。

## 專案特色

- ✅ **互動式視覺化**：使用 Chart.js 繪製互動式圖表
- ✅ **RESTful API**：提供 JSON 格式的資料端點
- ✅ **繁體中文介面**：所有介面、說明和資料欄位皆為繁體中文
- ✅ **響應式設計**：支援桌面和行動裝置
- ✅ **真實資料集**：使用 scikit-learn 經典資料集

## 專案結構

```
/final
├── app.py                          # Flask 應用程式主檔案
├── static/                         # 靜態資源目錄
│   ├── css/                        # CSS 樣式檔案
│   │   ├── index.css              # 首頁樣式
│   │   ├── regression.css         # 線性迴歸頁面樣式
│   │   └── knn.css                # KNN 頁面樣式
│   └── js/                         # JavaScript 檔案
│       ├── index.js               # 首頁互動功能
│       ├── regression.js          # 線性迴歸互動功能
│       └── knn.js                 # KNN 互動功能
├── templates/                      # HTML 模板目錄
│   ├── base.html                  # 基礎模板
│   ├── index.html                 # 首頁（機器學習介紹）
│   ├── regression.html            # 線性迴歸展示頁面
│   └── knn.html                   # KNN 分類展示頁面
├── CLAUDE.md                       # 專案說明文件
├── todolist.md                     # 開發任務清單
└── README.md                       # 本檔案
```

## 功能說明

### 1. 首頁（機器學習介紹）

- 路由：`/`
- 功能：
  - 線性迴歸演算法完整介紹（原理、適用場景、優缺點、應用案例）
  - KNN 演算法完整介紹（原理、適用場景、優缺點、應用案例）
  - 精美的卡片式設計
  - 快速導航到各實作頁面

### 2. 線性迴歸展示

- 路由：`/regression`
- API 端點：`/api/regression/data?feature=<特徵索引>`
- 功能：
  - 使用**糖尿病資料集**（442 個樣本，10 個特徵）
  - 可選擇不同特徵進行迴歸分析
  - 視覺化展示：
    - 訓練資料點（藍色圓點）
    - 測試資料點（粉紅色圓點）
    - 迴歸線（黃色直線）
  - 評估指標：
    - R² 分數（決定係數）
    - MSE（均方誤差）
    - RMSE（均方根誤差）
    - 迴歸係數
  - 互動功能：
    - 特徵選擇器
    - 即時更新圖表
    - Hover 顯示資料點資訊

### 3. KNN 分類展示

- 路由：`/knn`
- API 端點：`/api/knn/data?k=<K值>&feature_x=<X軸特徵>&feature_y=<Y軸特徵>`
- 功能：
  - 使用**鳶尾花資料集**（150 個樣本，4 個特徵，3 個類別）
  - 類別：山鳶尾、變色鳶尾、維吉尼亞鳶尾
  - 視覺化展示：
    - 訓練資料點（不同顏色圓點）
    - 測試資料點正確預測（三角形）
    - 測試資料點錯誤預測（紅色叉叉）
  - 評估指標：
    - 準確率（Accuracy）
    - 混淆矩陣（Confusion Matrix）
  - 互動功能：
    - K 值調整（slider 1-20）
    - 特徵選擇器（X 軸和 Y 軸）
    - 即時更新分類結果
    - Hover 顯示資料點資訊

## 環境設定與執行

### 前置需求

- Python 3.8+
- uv（Python 套件管理工具）

### 安裝步驟

1. **安裝依賴套件**
   ```bash
   uv add flask scikit-learn numpy pandas
   ```

2. **執行應用程式**
   ```bash
   uv run python ./final/app.py
   ```

3. **存取應用程式**
   - 開啟瀏覽器，前往 `http://127.0.0.1:5000`
   - Debug 模式已啟用（開發環境專用）

## API 文件

### 線性迴歸 API

**端點**：`GET /api/regression/data`

**參數**：
- `feature`（可選）：特徵索引（0-9），預設為 2（身體質量指數）

**回應範例**：
```json
{
  "success": true,
  "feature_names": ["年齡", "性別", "身體質量指數", ...],
  "current_feature": "身體質量指數",
  "data": {
    "train": { "x": [...], "y": [...] },
    "test": { "x": [...], "y": [...], "y_pred": [...] },
    "regression_line": { "x": [...], "y": [...] }
  },
  "metrics": {
    "r2_score": 0.4789,
    "mse": 2900.19,
    "rmse": 53.85,
    "coefficient": 949.43,
    "intercept": 152.13
  }
}
```

### KNN 分類 API

**端點**：`GET /api/knn/data`

**參數**：
- `k`（可選）：K 值（1-20），預設為 5
- `feature_x`（可選）：X 軸特徵索引（0-3），預設為 2（花瓣長度）
- `feature_y`（可選）：Y 軸特徵索引（0-3），預設為 3（花瓣寬度）

**回應範例**：
```json
{
  "success": true,
  "feature_names": ["花萼長度", "花萼寬度", "花瓣長度", "花瓣寬度"],
  "target_names": ["山鳶尾", "變色鳶尾", "維吉尼亞鳶尾"],
  "k_neighbors": 5,
  "data": {
    "train": { "x": [...], "y": [...], "labels": [...] },
    "test": { "x": [...], "y": [...], "labels": [...], "predictions": [...] }
  },
  "metrics": {
    "accuracy": 1.0,
    "confusion_matrix": [[...], [...], [...]]
  }
}
```

## 技術棧

- **後端框架**：Flask
- **機器學習**：scikit-learn
- **資料處理**：NumPy, Pandas
- **模板引擎**：Jinja2
- **前端技術**：HTML5, CSS3, JavaScript
- **視覺化**：Chart.js 4.4.0
- **套件管理**：uv

## 資料集說明

### 糖尿病資料集（Diabetes Dataset）

- **來源**：scikit-learn.datasets.load_diabetes
- **樣本數**：442
- **特徵數**：10 個生理指標
- **目標變數**：一年後疾病進展的量化指標（25-346）
- **特徵列表**：
  1. 年齡
  2. 性別
  3. 身體質量指數（BMI）
  4. 平均血壓
  5-10. 六項血清測量值

### 鳶尾花資料集（Iris Dataset）

- **來源**：scikit-learn.datasets.load_iris
- **樣本數**：150（每類 50 個）
- **特徵數**：4 個形態測量值
- **類別數**：3 種鳶尾花品種
- **特徵列表**：
  1. 花萼長度（cm）
  2. 花萼寬度（cm）
  3. 花瓣長度（cm）
  4. 花瓣寬度（cm）
- **類別列表**：
  1. 山鳶尾（Iris-Setosa）
  2. 變色鳶尾（Iris-Versicolor）
  3. 維吉尼亞鳶尾（Iris-Virginica）

## 開發重點

### 程式碼風格

- 遵循 Flask 最佳實踐
- 分離關注點（HTML/CSS/JS）
- RESTful API 設計
- 繁體中文註解

### 響應式設計

- 使用 CSS Grid 和 Flexbox
- 支援平板（≤768px）
- 支援手機（≤480px）
- 觸控友善的互動控制

## 注意事項

- **開發模式**：目前 debug 模式已啟用，適合學習和開發
- **生產環境**：部署前務必關閉 debug 模式
- **瀏覽器支援**：建議使用現代瀏覽器（Chrome, Firefox, Safari, Edge）
- **JavaScript**：需要啟用 JavaScript 才能使用互動功能

## 學習要點

1. Flask 路由與 API 開發
2. scikit-learn 機器學習模型使用
3. Chart.js 資料視覺化
4. 前後端資料交互（AJAX）
5. 響應式網頁設計
6. 模板繼承與資料傳遞

## 授權

本專案為教學用途，使用的資料集皆為公開資料集。

## 致謝

- scikit-learn 提供經典機器學習資料集
- Chart.js 提供優秀的圖表函式庫
- Flask 提供簡潔的 Web 框架

---

**建立日期**：2025-10-10
**作者**：職能發展學院
**版本**：1.0.0
