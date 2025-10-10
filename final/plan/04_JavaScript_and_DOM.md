## 第四階段：JavaScript 與 DOM 操作

**目標**：讓網頁具有「智慧」，能夠在不重新整理頁面的情況下，回應使用者的操作。

### A. 專案部分：`static/js/index.js` 與 `templates/index.html` 的互動

### B. 必備先備技能

#### 1. JavaScript 基礎與 DOM

- **教學重點**：強調 JS 是「跑在瀏覽器」的語言，負責網頁的「行為」。解釋 DOM (文件物件模型) 是 JS 與 HTML 溝通的橋樑。
- **範本 (讀取輸入框內容)**：
  ```html
  <input type="text" id="name-input" placeholder="請輸入你的名字">
  <button id="greet-btn">打招呼</button>
  <p id="greeting-output"></p>
  ```
  ```javascript
  // static/js/main.js
  const nameInput = document.getElementById('name-input');
  const greetBtn = document.getElementById('greet-btn');
  const outputArea = document.getElementById('greeting-output');

  greetBtn.addEventListener('click', function() {
      // 讀取輸入框的 .value
      const userName = nameInput.value;
      if (userName) { // 檢查是否有輸入
          outputArea.textContent = `你好, ${userName}!`;
      } else {
          outputArea.textContent = "請先輸入你的名字。";
      }
  });
  ```

#### 2. 事件 (Events)

- **教學重點**：除了 `click`，還可以介紹 `input` (輸入時觸發), `change` (值改變時觸發), `submit` (表單提交時觸發) 等常用事件。
- **範本 (即時預覽)**：
  ```html
  <label>輸入文字，下方會即時顯示：</label>
  <input type="text" id="live-preview-input">
  <h3>預覽：</h3>
  <p id="live-preview-output"></p>
  ```
  ```javascript
  const previewInput = document.getElementById('live-preview-input');
  const previewOutput = document.getElementById('live-preview-output');

  // 當在輸入框中打字時，'input' 事件會被觸發
  previewInput.addEventListener('input', function() {
      previewOutput.textContent = previewInput.value;
  });
  ```
