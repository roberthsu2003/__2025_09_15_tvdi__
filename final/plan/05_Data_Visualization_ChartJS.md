## 第五階段：數據視覺化 with Chart.js

**目標**：學習使用 Chart.js 這個強大的 JavaScript 函式庫來繪製圖表，為專案的 KNN 和迴歸分析結果做視覺化準備。

### A. 專案部分：在 HTML 中建立圖表

### B. 必備先備技能

#### 1. 什麼是 Chart.js？

- **教學重點**：Chart.js 是一個開源的 JS 函式庫，可以幫助我們輕鬆地將數據轉換成各種漂亮的圖表（長條圖、折線圖、散佈圖等）。它讓我們不用去處理複雜的繪圖細節。

#### 2. 如何引入 Chart.js

- **教學重點**：最簡單的方式是使用 CDN (Content Delivery Network)。這就像是直接從一個公開的圖書館借書，而不是自己下載回來。將 `<script>` 標籤加到 HTML 的 `<head>` 或 `<body>` 結尾。
- **範本**：
  ```html
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  ```

#### 3. Chart.js 的核心：`<canvas>` 與 `Chart` 物件

- **教學重點**：Chart.js 需要一個 HTML 的 `<canvas>` 元素作為它的「畫布」。然後，我們在 JavaScript 中建立一個 `new Chart()` 物件，告訴它要在哪個畫布上畫畫，以及要畫什麼。
- **範本**：
  ```html
  <!-- HTML 中需要一個 canvas 元素，並給它一個 id -->
  <div style="width: 80%; margin: auto;">
      <canvas id="myChart"></canvas>
  </div>
  ```
  ```javascript
  // 1. 取得 canvas 元素
  const ctx = document.getElementById('myChart');

  // 2. 建立新的 Chart 物件
  new Chart(ctx, {
      // ... 設定會放在這裡 ...
  });
  ```

#### 4. Chart.js 的設定物件 (Configuration)

- **教學重點**：這是 Chart.js 最重要的部分。它是一個 JavaScript 物件，用來定義圖表的 `type` (類型), `data` (資料), 和 `options` (選項)。
- **範本 (一個簡單的長條圖)**：
  ```javascript
  new Chart(ctx, {
      type: 'bar', // 圖表類型：長條圖
      data: {
          labels: ['一月', '二月', '三月', '四月', '五月'], // X 軸標籤
          datasets: [{
              label: '# 每月銷售量', // 這個資料集的標籤
              data: [12, 19, 3, 5, 2], // Y 軸的數據
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true // Y 軸從 0 開始
              }
          }
      }
  });
  ```

#### 5. 專案應用：散佈圖 (Scatter Plot)

- **教學重點**：對於 KNN 和迴歸分析，散佈圖是最合適的圖表類型。它的 `data` 格式是一個包含 `x` 和 `y` 座標的物件陣列。
- **範本 (模擬 KNN 的資料點)**：
  ```javascript
  new Chart(ctx, {
      type: 'scatter', // 圖表類型：散佈圖
      data: {
          datasets: [
          {
              label: '類別 A', // 第一群資料
              data: [
                  {x: 1, y: 2}, {x: 2, y: 3}, {x: 3, y: 2.5}
              ],
              backgroundColor: 'rgba(255, 99, 132, 0.6)' // 紅色
          }, 
          {
              label: '類別 B', // 第二群資料
              data: [
                  {x: 6, y: 7}, {x: 7, y: 8}, {x: 8, y: 7.5}
              ],
              backgroundColor: 'rgba(54, 162, 235, 0.6)' // 藍色
          }, 
          {
              label: '新資料點', // 要預測的點
              data: [
                  {x: 4, y: 5}
              ],
              backgroundColor: 'rgba(75, 192, 192, 1)', // 綠色
              pointRadius: 8 // 讓這個點大一點
          }]
      },
      options: {
          scales: {
              x: { type: 'linear', position: 'bottom' }
          }
      }
  });
  ```
