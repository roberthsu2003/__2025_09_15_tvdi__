# `index.js` 程式碼說明書

## 總覽

`index.js` 是專案中用於處理**全站通用**互動效果的 JavaScript 檔案。它的主要功能是控制導覽列在手機版螢幕上的顯示與隱藏（漢堡選單功能）。

---

## 程式碼詳解

### 1. 確保 DOM 載入完成

```javascript
document.addEventListener('DOMContentLoaded', function () {
    // ... 所有程式碼都在這裡面 ...
});
```

- **教學重點**：
    - `document.addEventListener('DOMContentLoaded', ...)` 是一個非常重要的實踐。
    - 它會等待整個 HTML 文件被瀏覽器完整讀取和解析後，才執行內部的 JavaScript 程式碼。
    - 這樣可以確保我們要操作的 HTML 元素（如下面的 `.nav-toggle`）都已經存在於頁面上，避免因找不到元素而產生的錯誤。
    - **比喻**：就像你不會在拿到菜單之前就開始點菜一樣，我們得等頁面（菜單）準備好，才能開始對它進行操作。

### 2. 獲取元素

```javascript
const toggle = document.querySelector('.nav-toggle');
const navList = document.querySelector('.nav-list');

if (!toggle || !navList) return;
```

- **教學重點**：
    - `document.querySelector()` 是用來選取頁面上**第一個**符合指定 CSS 選擇器的元素。
    - `.nav-toggle` 是漢堡選單的按鈕。
    - `.nav-list` 是要顯示或隱藏的選單列表。
    - `if (!toggle || !navList) return;` 是一個「防禦性」的寫法。如果頁面上剛好沒有這兩個元素，程式碼就會直接停止執行，避免後續的 `addEventListener` 出錯。

### 3. 漢堡選單點擊事件

```javascript
toggle.addEventListener('click', function () {
    navList.classList.toggle('open');
});
```

- **教學重點**：
    - `toggle.addEventListener('click', ...)` 為漢堡選單按鈕綁定了一個點擊事件監聽器。
    - 當使用者點擊這個按鈕時，內部的函式就會被觸發。
    - `navList.classList.toggle('open')` 是核心功能。`classList` 是元素的 CSS 類別列表，`toggle()` 方法會檢查 `navList` 是否有 `open` 這個 class：
        - 如果**沒有** `open`，就幫它**加上** `open`。
        - 如果**已經有** `open`，就把它**移除**。
    - 透過在 CSS 中定義 `.nav-list.open` 的樣式（例如 `display: block;`），我們就可以控制選單的顯示與隱藏。

### 4. 視窗尺寸改變時的處理

```javascript
window.addEventListener('resize', function () {
    if (window.innerWidth > 800) {
        if (navList.classList.contains('open')) {
            navList.classList.remove('open');
        }
        // ... (其他相關的 class 移除)
    }
});
```

- **教學重點**：
    - 這是一個提升使用者體驗的細節。
    - `window.addEventListener('resize', ...)` 會在瀏覽器視窗大小改變時觸發。
    - `window.innerWidth` 是目前視窗的寬度。
    - **目的**：想像一下，使用者在手機版打開了選單，然後將手機橫放或將瀏覽器視窗拉寬到桌機尺寸（大於 800px）。如果沒有這段程式碼，那個手機版的彈出式選單會一直開著，在桌機版上看起來很奇怪。
    - 這段程式碼的作用就是，當視窗寬度大於 800px 時，自動檢查並移除 `open` class，確保選單恢復到桌機版的預設狀態。
