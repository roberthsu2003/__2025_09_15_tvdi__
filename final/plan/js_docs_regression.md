# `regression.js` 程式碼說明書

## 總覽

`regression.js` 是負責「線性迴歸」頁面所有互動功能的腳本。其主要職責包括：從後端載入波士頓房價資料、使用 Chart.js 將資料點和迴歸線視覺化、處理使用者輸入的房間數以進行即時預測，並將預測結果動態呈現在圖表上。

---

## 全域變數

```javascript
let chart = null;
let modelData = null;
```

- **教學重點**：
    - `let chart = null;`：與 `knn.js` 相同，用於存放 Chart.js 的圖表物件，以便後續的更新與銷毀。
    - `let modelData = null;`：用於快取從後端 `/api/regression/data` 獲取的完整模型資料（包含訓練集、測試集、迴歸線座標等），避免不必要的重複 API 請求。

---

## 主要流程

### 1. 頁面載入與事件綁定

```javascript
document.addEventListener('DOMContentLoaded', function() {
    loadRegressionData();

    document.getElementById('predict-btn').addEventListener('click', ...);
    document.getElementById('rooms-input').addEventListener('keypress', ...);
});
```

- **教學重點**：
    - 頁面載入完成後，立即呼叫 `loadRegressionData()` 獲取資料並繪製初始圖表。
    - 為「預測」按鈕綁定 `click` 事件，點擊時讀取輸入框的值並呼叫 `predictPrice()`。
    - 為房間數輸入框綁定 `keypress` 事件，監聽使用者是否按下 `Enter` 鍵。如果按下 `Enter`，也觸發 `predictPrice()` 函式，提供更流暢的使用體驗。

### 2. 載入迴歸資料 (`loadRegressionData`)

```javascript
async function loadRegressionData() {
    showLoading(true);
    try {
        const response = await fetch('/api/regression/data');
        const data = await response.json();
        if (data.success) {
            modelData = data;
            renderChart(data);
            updateMetrics(data.metrics);
            updateModelInfo(data.description);
            // ... 更新公式 ...
        }
    } ...
}
```

- **教學重點**：
    - 同樣使用 `async/await` 處理非同步 `fetch` 請求。
    - 此函式向後端 `/api/regression/data` 發送請求，一次性獲取所有需要的資料。
    - 成功獲取資料後，除了繪製圖表 (`renderChart`) 和更新指標 (`updateMetrics`, `updateModelInfo`) 外，還會動態地將後端計算出的迴歸公式（係數和截距）顯示在頁面上。

### 3. 預測房價 (`predictPrice`)

```javascript
async function predictPrice(rooms) {
    if (isNaN(rooms) || rooms < 1 || rooms > 15) { ... }

    try {
        const response = await fetch(`/api/regression/predict?rooms=${rooms}`);
        const data = await response.json();
        if (data.success) {
            // ... 更新預測價格顯示 ...
            addPredictionPoint(rooms, data.prediction.price);
        }
    } ...
}
```

- **教學重點**：
    - **前端驗證**：在發送 API 請求前，先在前端進行簡單的輸入驗證 (`isNaN`, `rooms < 1`, etc.)，可以減少不必要的後端負擔，並立即給予使用者回饋。
    - 此函式向後端 `/api/regression/predict` 發送請求，並將使用者輸入的房間數 `rooms` 作為查詢參數附加在 URL 上。
    - 成功獲取預測結果後，不僅會更新頁面上的價格顯示，還會呼叫 `addPredictionPoint()` 將這個新的預測點畫在圖表上。

### 4. 繪製圖表 (`renderChart`)

```javascript
function renderChart(data) {
    // ... 銷毀舊圖表 ...

    // 準備訓練/測試資料集 (type: 'scatter')
    const trainData = ...;
    const testData = ...;

    // 準備迴歸線資料集 (type: 'line')
    const regressionLine = ...;

    chart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [ ... ]
        },
        options: { ... }
    });
}
```

- **教學重點**：
    - **混合圖表類型**：這是線性迴歸圖表的關鍵。整個圖表的基礎類型是 `scatter` (散佈圖)，用於繪製訓練和測試資料點。但是，在 `datasets` 陣列中，代表迴歸線的那個資料集，其 `type` 被特別指定為 `line` (折線圖)。Chart.js 允許在同一個圖表中混合不同類型的資料集。
    - **迴歸線樣式**：為了讓迴歸線看起來像一條線而不是一堆點，需要設定 `pointRadius: 0`（點的半徑為0）和 `fill: false`（不填充線下方的區域）。
    - **`onClick` 互動**：與 KNN 圖表類似，這裡也設定了 `onClick` 事件。但互動方式不同：當使用者點擊任一個已存在的資料點（訓練或測試資料）時，程式會自動將該點的房間數填入輸入框，並呼叫 `predictPrice()` 進行一次新的預測，讓使用者可以方便地比較真實資料點和模型預測值的差異。

### 5. 新增預測點 (`addPredictionPoint`)

```javascript
function addPredictionPoint(x, y) {
    const existingDatasets = chart.data.datasets.filter(ds => ds.label !== '您的預測');

    existingDatasets.push({ ... });

    chart.data.datasets = existingDatasets;
    chart.update();
}
```

- **教學重點**：
    - **動態更新資料**：這個函式示範了如何在不銷毀整個圖表的情況下更新資料。
    - `chart.data.datasets.filter(...)`：首先，過濾掉舊的「您的預測」資料集（如果存在的話）。
    - `existingDatasets.push({ ... })`：然後，將包含新預測點座標 `(x, y)` 的新資料集推進陣列。
    - `chart.data.datasets = existingDatasets;`：將圖表的 `datasets` 更新為這個新的陣列。
    - `chart.update();`：**最後，必須呼叫 `chart.update()`**，Chart.js 才會根據新的資料重繪圖表。這比 `destroy()` 後再 `new Chart()` 的效能更好。
