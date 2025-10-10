## 第六階段：前後端整合與專案完成

**目標**：將所有技能整合，實現從前端輸入數據，後端用 Python 計算，再將結果動態更新到前端 Chart.js 圖表上的完整流程。

### A. 專案部分：完整的 KNN/迴歸頁面

### B. 必備先備技能

#### 1. JavaScript `fetch` API 與非同步

- **教學重點**：解釋 `fetch` 如何在「不刷新頁面」的情況下，向後端 Flask 發送請求並接收數據。強調 `async/await` 或 `.then()` 是處理「等待」網路回應的方式。
- **範本**：
  ```javascript
  // 假設有一個表單和一個按鈕
  document.getElementById('predict-form').addEventListener('submit', async function(event) {
      event.preventDefault(); // 防止表單傳統提交導致頁面刷新

      const x_val = document.getElementById('input-x').value;
      const y_val = document.getElementById('input-y').value;

      const response = await fetch('/api/predict', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ x: x_val, y: y_val }),
      });

      const result = await response.json();
      
      // 在這裡呼叫函式來更新圖表
      updateChart(result.all_points, result.prediction);
  });
  ```

#### 2. Flask API 路由

- **教學重點**：建立一個專門用來回傳「資料」而不是「HTML 頁面」的路由。這種路由通常稱為 API Endpoint。`jsonify` 是 Flask 中將 Python 字典轉換為 JSON 格式回應的好幫手。
- **範本**：
  ```python
  from flask import request, jsonify

  @app.route('/api/predict', methods=['POST'])
  def api_predict():
      data = request.get_json()
      x = float(data['x'])
      y = float(data['y'])

      # --- 在這裡放入你的機器學習模型 --- #
      # 1. 根據 (x, y) 進行預測
      # 2. 準備好所有要顯示的點
      # --- 假設的結果 --- #
      prediction_label = '類別 A'
      all_data_points = {
          'class_a': [{...}],
          'class_b': [{...}]
      }

      return jsonify({
          'prediction': prediction_label,
          'all_points': all_data_points
      })
  ```

#### 3. 動態更新 Chart.js

- **教學重點**：`fetch` 拿到新資料後，如何更新已存在的圖表。最簡單的方式是銷毀舊圖表，用新資料建立一個新圖表。也可以直接更新 `chart.data` 然後呼叫 `chart.update()`。
- **範本**：
  ```javascript
  let myChart = null; // 將圖表物件存在一個全域變數

  function createOrUpdateChart(datasets) {
      const ctx = document.getElementById('myScatterChart');

      if (myChart) {
          myChart.destroy(); // 如果圖表已存在，先銷毀
      }

      myChart = new Chart(ctx, {
          type: 'scatter',
          data: {
              datasets: datasets // 從後端傳來的資料集
          },
          // ... options
      });
  }

  // 在 fetch 的 .then() 或 await 後呼叫這個函式
  // updateChart(result.all_points, result.prediction);
  ```
