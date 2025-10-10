## 第三階段：CSS 樣式與靜態檔案

**目標**：美化網頁，讓學生學會用 CSS 將網頁從「骨架」變成有「血肉」的樣貌。

### A. 專案部分：`static/css/index.css` 與 `templates/base.html` 的模板繼承

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}我的網站{% endblock %}</title>
    <!-- 連結到 CSS 檔案 -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        {% block content %}
        <!-- 子模板的內容會顯示在這裡 -->
        {% endblock %}
    </div>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends "base.html" %}

{% block title %}首頁{% endblock %}

{% block content %}
    <h1 class="page-title">歡迎來到首頁</h1>
    <p>這是繼承自 base.html 的頁面。</p>
{% endblock %}
```

### B. 必備先備技能

#### 1. CSS 選擇器與屬性

- **教學重點**：詳細解釋「層疊」(Cascade) 的概念，即樣式衝突時的優先級順序 (ID > Class > 標籤)。介紹偽類 (pseudo-classes) 如 `:hover`，讓網頁有互動感。
- **範本**：
  ```css
  /* static/css/style.css */
  body {
      font-family: sans-serif; /* 設定預設字體 */
  }

  .page-title {
      color: #333;
      border-bottom: 2px solid #ccc;
  }

  /* 按鈕樣式 */
  .btn {
      display: inline-block;
      padding: 10px 15px;
      background-color: #007bff;
      color: white;
      text-decoration: none;
      border-radius: 5px;
  }

  /* 滑鼠懸停在按鈕上時的樣式 */
  .btn:hover {
      background-color: #0056b3;
  }
  ```

#### 2. CSS 盒模型 (Box Model)

- **教學重點**：解釋每個 HTML 元素都是一個「盒子」，包含 `content`, `padding`, `border`, `margin` 四個部分。務必用開發者工具 (F12) 展示盒模型，讓學生有具象的理解。

#### 3. Flexbox 佈局

- **教學重點**：Flexbox 是現代網頁排版的核心技術，用來輕鬆實現水平或垂直對齊。解釋 `display: flex` 以及 `justify-content` 和 `align-items` 的作用。
- **範本**：
  ```html
  <div class="flex-container">
      <div class="flex-item">1</div>
      <div class="flex-item">2</div>
      <div class="flex-item">3</div>
  </div>
  ```
  ```css
  .flex-container {
      display: flex; /* 啟用 Flexbox */
      justify-content: space-around; /* 主軸對齊方式 (水平) */
      align-items: center; /* 副軸對齊方式 (垂直) */
      background-color: #f0f0f0;
      height: 100px;
  }
  .flex-item {
      width: 50px;
      height: 50px;
      background-color: #007bff;
      color: white;
      text-align: center;
      line-height: 50px;
  }
  ```
