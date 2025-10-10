## 第二階段：HTML 基礎與模板渲染

**目標**：讓學生學會建立網頁的「骨架」，並從 Flask 後端動態載入頁面，傳遞簡單資料。

### A. 專案部分：`templates/index.html` 與 `app.py` 的修改

```python
# app.py (第二階段)
from flask import Flask, render_template # 匯入 render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 準備要傳到前端的資料
    teacher_name = "Gemin"
    student_count = 20
    # 將變數傳入模板
    return render_template('index.html', 
                           teacher=teacher_name, 
                           students=student_count)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>歡迎來到我的課程</title>
</head>
<body>
    <h1>歡迎！</h1>
    <!-- 使用 Jinja2 語法 {{ ... }} 來顯示從後端傳來的變數 -->
    <p>授課老師: {{ teacher }}</p>
    <p>目前學生人數: {{ students }}</p>
</body>
</html>
```

### B. 必備先備技能

#### 1. HTML 結構與常用標籤

- **教學重點**：強調 HTML (HyperText Markup Language) 是用來定義網頁「內容結構」的語言，不是用來做樣式的。介紹各種標籤的「語意」(semantic meaning)，例如 `<h1>` 是最重要的標題，`<nav>` 是導覽列。
- **範本**：
  ```html
  <header>
      <h1>網站標題</h1>
      <nav>
          <ul>
              <li><a href="/">首頁</a></li>
              <li><a href="/about">關於我們</a></li>
          </ul>
      </nav>
  </header>
  <main>
      <article>
          <h2>文章標題</h2>
          <p>這是一段文章內容...</p>
      </article>
  </main>
  <footer>
      <p>&copy; 2025 版權所有</p>
  </footer>
  ```

#### 2. Flask 模板引擎 Jinja2

- **教學重點**：解釋 `render_template` 的作用，以及 Jinja2 如何讓 HTML 變成「動態的」。它就像是一個填空遊戲，`{{ variable }}` 就是我們要填空的格子。
- **範本 (Jinja2 流程控制)**：
  ```html
  <!-- templates/example.html -->
  <h2>學生列表</h2>
  <ul>
      {% for student in student_list %}
          <li>{{ student.name }} - {{ student.score }} 分</li>
      {% endfor %}
  </ul>

  {% if average_score > 60 %}
      <p>平均分數及格！</p>
  {% else %}
      <p>平均分數不及格，大家要加油！</p>
  {% endif %}
  ```
  ```python
  # app.py
  @app.route('/students')
def show_students():
      students = [
          {'name': '小明', 'score': 88},
          {'name': '小華', 'score': 52},
          {'name': '小英', 'score': 95}
      ]
      avg = sum(s['score'] for s in students) / len(students)
      return render_template('example.html', student_list=students, average_score=avg)
  ```
