# Flask 專案說明文件

## 專案概述

這是一個使用 Python Flask 框架建立的網頁應用程式，整合了機器學習模型展示功能，包含線性迴歸（Regression）和 K 近鄰演算法（KNN）的互動式介面。

## 專案結構

```
/final
├── app.py                      # Flask 應用程式主檔案
├── static/                     # 靜態資源目錄
│   ├── css/                    # CSS 樣式檔案
│   │   ├── index.css
│   └── js/                     # JavaScript 檔案
│       ├── index.js
├── templates/                  # HTML 模板目錄
│   ├── base.html              # 基礎模板
│   ├── index.html             # 首頁
│   ├── regression.html        # 線性迴歸頁面
│   ├── knn.html               # KNN 演算法頁面
├── CLAUDE.md                  # 本說明文件
├── GEMINI.md                  # Gemini 相關文件
└── AGENTS.md                  # Agents 相關文件
```

## 功能說明

### 路由（Routes）

| 路由 | 功能 | 模板檔案 |
|------|------|----------|
| `/` | 首頁 | `index.html` |
| `/regression` | 線性迴歸展示 | `regression.html` |
| `/knn` | KNN 演算法展示 | `knn.html` |

### 主要功能

1. **首頁 (index)**: 專案入口頁面
2. **線性迴歸 (regression)**: 展示線性迴歸模型的應用
3. **KNN 演算法 (knn)**: 展示 K 近鄰分類器的應用


## 環境設定與執行

### 前置需求

- Python 3.8+
- uv（Python 套件管理工具）

### 安裝與執行步驟

1. **安裝依賴套件**
   ```bash
   uv add 套件名稱

2. **執行應用程式**
   ```bash
   uv run python ./final/app.py
   ```

3. **存取應用程式**
   - 開啟瀏覽器，前往 `http://127.0.0.1:5000`
   - Debug 模式已啟用（開發環境專用）

### 開發模式說明

- 應用程式目前設定為 `debug=True`，會自動重新載入程式碼變更
- **生產環境部署時請務必關閉 debug 模式**

## 開發規範

### 檔案組織原則

1. **模板檔案（Templates）**
   - 所有 HTML 檔案放置於 `templates/` 目錄
   - 使用 Jinja2 模板語法
   - 建議使用模板繼承（base templates）來重用共用結構

2. **靜態資源（Static Files）**
   - CSS 檔案：`static/css/`
   - JavaScript 檔案：`static/js/`
   - 圖片檔案：`static/images/`（若需要）

3. **程式碼風格**
   - 避免在 HTML 中使用行內樣式（inline styles）
   - CSS 規則統一寫在對應的 `.css` 檔案中
   - JavaScript 邏輯應獨立於 HTML 檔案

### 命名規範

- **路由函式**：使用小寫 + 底線（如 `lesson6_1`）
- **CSS 檔案**：對應頁面名稱（如 `lesson6_1.css`）
- **JavaScript 檔案**：對應頁面名稱（如 `lesson6_1.js`）
- **模板檔案**：對應路由名稱（如 `lesson6_1.html`）

## 技術棧

- **後端框架**: Flask
- **模板引擎**: Jinja2
- **前端技術**: HTML5, CSS3, JavaScript
- **開發工具**: uv (套件管理)

## 學習要點

1. Flask 路由與視圖函式的定義
2. Jinja2 模板語法與資料傳遞
3. 靜態檔案的組織與引用
4. 模板繼承（Template Inheritance）
5. 動態資料渲染（如用戶列表、VIP 狀態）

## 注意事項

- 生產環境部署時需關閉 debug 模式
- 敏感資訊（如密鑰）應使用環境變數管理
- 建議加入 `.gitignore` 忽略虛擬環境與快取檔案
