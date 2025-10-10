# 部署準備指南 ☁️

本文件說明如何將此 Flask 機器學習專案部署到雲端平台。

---

## 部署前檢查清單 ✅

### 1. 關閉 Debug 模式

編輯 `app.py`：

```python
def main():
    # 生產環境：關閉 debug 模式
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### 2. 建立 requirements.txt

```bash
uv pip freeze > requirements.txt
```

或手動建立 `requirements.txt`：

```txt
Flask>=3.0.0
scikit-learn>=1.3.0
numpy>=1.24.0
pandas>=2.0.0
```

### 3. 建立 .gitignore

建立 `.gitignore` 檔案：

```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/
.venv/
venv/
.env
.DS_Store
```

### 4. 設定環境變數

建立 `.env` 檔案（不要提交到 Git）：

```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

修改 `app.py` 使用環境變數：

```python
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-only')
```

---

## 推薦部署平台

### 選項 1：Render.com（推薦）⭐

**優點**：
- 免費方案
- 自動部署
- HTTPS 預設啟用
- 操作簡單

**步驟**：

1. 建立 `render.yaml`：

```yaml
services:
  - type: web
    name: ml-demo
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: FLASK_ENV
        value: production
```

2. 推送到 GitHub
3. 連結 Render 到你的 GitHub repo
4. 自動部署完成！

**參考**：https://render.com/docs/deploy-flask

---

### 選項 2：Railway.app

**優點**：
- 現代化介面
- 自動 HTTPS
- 簡單設定

**步驟**：

1. 建立 `railway.toml`：

```toml
[build]
builder = "NIXPACKS"

[deploy]
startCommand = "python app.py"
```

2. 推送到 GitHub
3. 使用 Railway CLI 或 Web 介面部署

**參考**：https://docs.railway.app/guides/python

---

### 選項 3：Fly.io

**優點**：
- 全球 CDN
- 彈性擴展

**步驟**：

1. 安裝 Fly CLI：`curl -L https://fly.io/install.sh | sh`

2. 建立 `fly.toml`：

```toml
app = "ml-demo"
primary_region = "sin"

[http_service]
  internal_port = 5000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 256
```

3. 建立 `Dockerfile`：

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

4. 部署：`fly deploy`

**參考**：https://fly.io/docs/languages-and-frameworks/python/

---

## 效能優化建議 🚀

### 1. 快取資料集

修改 `app.py` 使用快取：

```python
from functools import lru_cache

@lru_cache(maxsize=1)
def get_diabetes_data():
    return load_diabetes()

@lru_cache(maxsize=1)
def get_iris_data():
    return load_iris()
```

### 2. 壓縮靜態資源

```bash
# 安裝 Flask-Compress
pip install flask-compress
```

在 `app.py` 中：

```python
from flask_compress import Compress

app = Flask(__name__)
Compress(app)
```

### 3. 使用 CDN

確認 `base.html` 中的 Chart.js 使用 CDN（已設定）。

---

## 監控與除錯

### 查看錯誤日誌

大多數平台提供即時日誌：

```bash
# Render
render logs

# Railway
railway logs

# Fly.io
fly logs
```

### 健康檢查端點

在 `app.py` 中新增：

```python
@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200
```

---

## 安全性建議 🔒

1. **永遠不要**將 `.env` 檔案提交到 Git
2. 使用強隨機密鑰作為 `SECRET_KEY`
3. 啟用 HTTPS（大多數平台預設啟用）
4. 定期更新依賴套件：`pip install --upgrade -r requirements.txt`
5. 使用環境變數管理敏感資訊

---

## 成本預估 💰

### 免費方案（適合學習/展示）

| 平台 | 免費方案限制 |
|------|-------------|
| Render | 750 小時/月（約 31 天）|
| Railway | $5 免費額度/月 |
| Fly.io | 3 個 shared-cpu VM |

### 付費方案（適合生產環境）

- 月費約 $5-20 USD
- 取決於流量和運算需求

---

## 部署後測試

### 檢查清單

- [ ] 訪問首頁：`https://your-domain.com/`
- [ ] 測試線性迴歸頁面：`https://your-domain.com/regression`
- [ ] 測試 KNN 頁面：`https://your-domain.com/knn`
- [ ] 測試 API 端點：`https://your-domain.com/api/regression/data`
- [ ] 測試 API 端點：`https://your-domain.com/api/knn/data`
- [ ] 檢查手機版響應式設計
- [ ] 確認 HTTPS 正常運作
- [ ] 查看錯誤日誌是否有異常

---

## 常見部署問題

### 問題 1：模組找不到

**錯誤**：`ModuleNotFoundError: No module named 'sklearn'`

**解決**：確認 `requirements.txt` 包含所有依賴套件。

### 問題 2：記憶體不足

**錯誤**：`MemoryError`

**解決**：
- 升級到更大的實例
- 使用資料快取減少記憶體使用
- 減少資料集大小

### 問題 3：啟動超時

**錯誤**：`Application failed to respond`

**解決**：
- 確認 `app.run()` 使用 `host='0.0.0.0'`
- 檢查 port 設定是否正確（通常使用環境變數）

```python
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

---

## 進階功能（選用）

### 1. 資料庫支援

如果需要儲存使用者資料，可加入 PostgreSQL：

```bash
pip install psycopg2-binary flask-sqlalchemy
```

### 2. 使用者認證

```bash
pip install flask-login
```

### 3. API 限流

```bash
pip install flask-limiter
```

---

## 部署檢查表總結 ✅

在部署前，請確認：

- [x] ✅ 所有功能在本地測試通過
- [ ] 關閉 debug 模式
- [ ] 建立 `requirements.txt`
- [ ] 建立 `.gitignore`
- [ ] 設定環境變數
- [ ] 選擇部署平台
- [ ] 推送程式碼到 GitHub
- [ ] 完成部署設定
- [ ] 測試所有功能
- [ ] 監控錯誤日誌

---

**祝部署順利！** 🎉

如有問題，請查閱各平台的官方文件或社群論壇。
