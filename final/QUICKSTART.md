# 快速啟動指南 🚀

## 一鍵啟動

```bash
# 進入專案目錄
cd final

# 啟動應用程式
uv run python app.py
```

然後在瀏覽器開啟：**http://127.0.0.1:5000**

---

## 專案已包含的功能 ✅

### 1️⃣ 首頁 - 機器學習介紹
- 訪問：http://127.0.0.1:5000/
- 內容：線性迴歸和 KNN 演算法的完整中文介紹

### 2️⃣ 線性迴歸互動展示
- 訪問：http://127.0.0.1:5000/regression
- 功能：
  - 選擇 10 個特徵中的任一個
  - 查看迴歸線和散點圖
  - 即時顯示 R²、MSE、RMSE 等指標

### 3️⃣ KNN 分類互動展示
- 訪問：http://127.0.0.1:5000/knn
- 功能：
  - 調整 K 值（1-20）
  - 選擇要顯示的 2 個特徵
  - 查看分類結果和混淆矩陣
  - 即時顯示準確率

---

## API 端點測試

### 線性迴歸 API
```bash
# 預設使用 BMI（身體質量指數）
curl http://127.0.0.1:5000/api/regression/data

# 使用其他特徵（例如：特徵索引 0 = 年齡）
curl http://127.0.0.1:5000/api/regression/data?feature=0
```

### KNN 分類 API
```bash
# 預設 K=5，使用花瓣長度和花瓣寬度
curl http://127.0.0.1:5000/api/knn/data

# 自訂參數：K=3，使用花萼長度(0)和花萼寬度(1)
curl "http://127.0.0.1:5000/api/knn/data?k=3&feature_x=0&feature_y=1"
```

---

## 檔案結構速覽

```
final/
├── app.py                  # 後端（Flask + scikit-learn）
├── templates/              # 前端 HTML
│   ├── base.html          # 共用模板（含 Chart.js）
│   ├── index.html         # 首頁
│   ├── regression.html    # 線性迴歸頁面
│   └── knn.html           # KNN 頁面
├── static/
│   ├── css/               # 樣式檔案
│   │   ├── index.css
│   │   ├── regression.css
│   │   └── knn.css
│   └── js/                # 互動邏輯
│       ├── index.js
│       ├── regression.js  # 呼叫 API + 繪製圖表
│       └── knn.js         # 呼叫 API + 繪製圖表
└── README.md              # 完整文件
```

---

## 常見問題 ❓

### Q: 圖表沒有顯示？
A: 確認瀏覽器已啟用 JavaScript，並檢查主控台是否有錯誤訊息。

### Q: API 回應 404 錯誤？
A: 確認 Flask 伺服器已正常啟動，檢查終端機是否顯示錯誤訊息。

### Q: 想修改顏色或樣式？
A: 編輯 `static/css/` 目錄下的對應 CSS 檔案。

### Q: 想調整機器學習參數？
A: 編輯 `app.py` 中的 `train_test_split` 或模型參數。

### Q: 想換其他資料集？
A: 修改 `app.py` 中的 `load_diabetes()` 或 `load_iris()` 為其他 scikit-learn 資料集。

---

## 停止伺服器

在終端機按 **Ctrl + C** 即可停止 Flask 伺服器。

---

## 下一步建議 💡

1. 瀏覽首頁了解演算法原理
2. 試試線性迴歸頁面的不同特徵
3. 在 KNN 頁面調整 K 值，觀察準確率變化
4. 查看 API 回應的 JSON 資料結構
5. 修改樣式或新增功能

**祝你學習愉快！** 🎉
