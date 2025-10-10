# `knn.js` 程式碼說明書

## 總覽

`knn.js` 是專門負責「KNN 分類」頁面所有互動功能的腳本。它處理從後端載入鳶尾花資料、根據使用者調整的 K 值重新計算模型、使用 Chart.js 繪製散佈圖，以及處理圖表上的點擊事件以顯示詳細資訊。

---

## 全域變數與設定

```javascript
let chart = null;
let currentK = 5;
let modelData = null;
let targetNames = ["山鳶尾", "變色鳶尾", "維吉尼亞鳶尾"];
let featureNames = ["花萼長度", "花萼寬度", "花瓣長度", "花瓣寬度"];

const classColors = [
    { bg: '...', border: '...' },
    { bg: '...', border: '...' },
    { bg: '...', border: '...' }
];
```

- **教學重點**：
    - `let chart = null;`：用來存放 Chart.js 的圖表物件。設為全域變數是為了方便在不同函式中存取和更新它（例如，銷毀舊圖表、建立新圖表）。
    - `currentK`：儲存目前使用者選擇的 K 值，預設為 5。
    - `modelData`：儲存從後端 API 獲取的完整資料，避免重複請求。
    - `targetNames`, `featureNames`：儲存資料集的標籤名稱，方便在 UI 上顯示。
    - `classColors`：定義好每個類別在圖表上的顏色，讓視覺呈現保持一致。

---

## 主要流程

### 1. 頁面載入與事件綁定

```javascript
document.addEventListener('DOMContentLoaded', function() {
    loadKnnData();

    const kSlider = document.getElementById('k-slider');
    // ...

    kSlider.addEventListener('input', function() { ... });
    kSlider.addEventListener('change', function() { ... });
});
```

- **教學重點**：
    - 頁面載入完成後 (`DOMContentLoaded`)，立刻執行 `loadKnnData()` 來獲取預設 K=5 的資料並繪製圖表。
    - 綁定 K 值滑桿 (`k-slider`) 的兩個事件：
        - `input` 事件：當使用者**拖動滑桿時**觸發，即時更新顯示的 K 值數字 (`k-value`)。
        - `change` 事件：當使用者**放開滑桿時**觸發。這時才更新 `currentK` 變數，並呼叫 `loadKnnData()` 重新向後端請求資料，更新整個圖表和模型評估指標。這樣可以避免在拖動過程中發送大量不必要的 API 請求。

### 2. 載入 KNN 資料 (`loadKnnData`)

```javascript
async function loadKnnData() {
    showLoading(true);
    try {
        const url = `/api/knn/data?k=${currentK}&feature_x=2&feature_y=3`;
        const response = await fetch(url);
        const data = await response.json();

        if (data.success) {
            modelData = data;
            renderChart(data);
            updateMetrics(data.metrics);
            updateModelInfo(data.description, data.k_neighbors);
        } else { ... }
    } catch (error) { ... }
    finally {
        showLoading(false);
    }
}
```

- **教學重點**：
    - 這是一個 `async` 函式，表示內部可以使用 `await` 來等待非同步操作（如 `fetch`）完成。
    - `showLoading(true)`：在請求開始前顯示載入動畫，提升使用者體驗。
    - `const url = ...`：動態組合 API 的 URL，將目前的 `currentK` 和固定的特徵索引（2 和 3，代表花瓣長度/寬度）作為查詢參數傳給後端。
    - `const response = await fetch(url);`：使用 `fetch` 向後端發送 GET 請求。
    - `const data = await response.json();`：將後端回傳的 JSON 字串解析成 JavaScript 物件。
    - `if (data.success)`：如果請求成功，就用回傳的資料依序呼叫 `renderChart` (繪製圖表), `updateMetrics` (更新準確率等指標), `updateModelInfo` (更新資料集資訊)。
    - `finally { showLoading(false); }`：無論請求成功或失敗，最後都要隱藏載入動畫。

### 3. 繪製圖表 (`renderChart`)

```javascript
function renderChart(data) {
    const ctx = document.getElementById('knnChart').getContext('2d');
    if (chart) { chart.destroy(); }

    const datasets = [];
    // ... 遍歷資料，建立 datasets 陣列 ...

    chart = new Chart(ctx, { ... });
}
```

- **教學重點**：
    - **銷毀舊圖表**：`if (chart) { chart.destroy(); }` 是動態更新圖表的關鍵。在繪製新圖表前，必須先銷毀舊的圖表實例，否則會造成記憶體洩漏和畫面重疊。
    - **資料分組**：Chart.js 的 `datasets` 是一個陣列，每個元素代表一組資料（例如「類別A的訓練資料」、「類別B的測試資料」）。這段程式碼的核心邏輯就是將後端傳來的一整包 `data`，根據「訓練/測試」和「類別」拆分成多個 `dataset` 物件。
    - **視覺區分**：透過設定不同的 `pointStyle` ('circle', 'triangle', 'crossRot') 和 `pointRadius`，在視覺上明確區分訓練資料、正確預測的測試資料和錯誤預測的測試資料。
    - **`onClick` 事件**：在 `options` 中設定 `onClick` 回呼函式。當使用者點擊圖表上的任一個點時，Chart.js 會提供被點擊元素的資訊。我們可以從中獲取該點的資料，並呼叫 `showClassificationResult()` 來顯示詳細資訊。
    - **`plugins` 設定**：用於設定圖表標題 (`title`)、圖例 (`legend`) 和提示框 (`tooltip`) 的外觀和行為。

### 4. 顯示點擊結果 (`showClassificationResult`)

```javascript
function showClassificationResult(dataPoint, datasetType, index) {
    const container = document.getElementById('classification-result');
    // ... 組合 HTML 字串 ...
    container.innerHTML = html;
}
```

- **教學重點**：
    - 這個函式接收被點擊的資料點物件 (`dataPoint`)。
    - 它會動態地組合一段 HTML 字串，包含該點的特徵值、實際品種，以及（如果是測試資料）模型的預測結果。
    - `container.innerHTML = html;`：將組合好的 HTML 寫入到指定的 `div` 中，實現畫面上資訊卡的更新。

### 5. 更新 UI 資訊 (`updateMetrics`, `updateModelInfo`)

- **教學重點**：
    - 這兩個函式相對單純，它們根據 `loadKnnData` 獲取的資料，選取對應的 HTML 元素（如 `document.getElementById('accuracy')`），並更新其 `textContent`，將最新的模型準確率和資料集資訊顯示在畫面上。
