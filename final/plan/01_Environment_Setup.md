## 第一階段：環境建置與 "Hello, World!"

**目標**：讓學生成功運行第一個最簡單的 Web 應用程式，並理解網頁伺服器的基本概念。

### A. 專案部分：`app.py` 的最小化版本

教學生建立一個只包含最基本路由的 `app.py`，並成功在瀏覽器看到結果。

```python
# app.py (教學用的最小版本)
from flask import Flask

# 建立一個 Flask 應用程式實例
app = Flask(__name__)

# 定義一個路由 (Route)，將 URL 路徑 '/' 對應到一個 Python 函式
@app.route('/')
def hello_world():
    # 這個函式回傳的內容，將會顯示在瀏覽器上
    return 'Hello, World! from Flask!'

# 確保當這個 Python 檔案被直接執行時，才啟動伺服器
if __name__ == '__main__':
    # app.run() 會啟動一個本地開發伺服器
    # debug=True 讓伺服器在程式碼變更後自動重啟，並提供詳細的錯誤訊息
    app.run(debug=True)
```

### B. 必備先備技能

#### 1. 概念說明：Client-Server 模型

- **教學重點**：用簡單的比喻解釋 Web 運作方式。例如，瀏覽器（Client）像是一個顧客，向餐廳（Server）點餐（發送請求 Request）。伺服器根據菜單（程式碼）準備餐點（產生 HTML），然後送回給顧客（回傳回應 Response）。我們寫的 Flask 程式，就是扮演伺服器的角色。

#### 2. Python 虛擬環境 (Virtual Environment)

- **教學重點**：強調「每個專案都應該有自己的乾淨房間」。虛擬環境就像是為每個專案準備一個獨立的工具箱，避免不同專案的工具（函式庫版本）互相打架。
- **範本**：
  ```bash
  # 1. 在專案資料夾中，建立一個名為 venv 的虛擬環境
  python -m venv venv

  # 2. 啟動虛擬環境
  # Windows (CMD/PowerShell)
  .\venv\Scripts\activate
  # macOS / Linux (bash/zsh)
  source venv/bin/activate

  # 成功啟動後，命令提示字元前面會出現 (venv) 的字樣
  # 3. 若要離開虛擬環境，執行 deactivate
  deactivate
  ```

#### 3. 使用 `pip` 安裝套件

- **教學重點**：解釋 `pip` 是 Python 的「App Store」。`requirements.txt` 則像是一張購物清單，記錄了專案需要的所有工具，方便我們一次性安裝。
- **範本**：
  ```bash
  # (在虛擬環境啟動的狀態下)
  # 安裝單一套件
  pip install Flask

  # 根據購物清單 (requirements.txt) 一次安裝所有東西
  pip install -r requirements.txt
  ```

#### 4. Python 基礎語法

- **教學重點**：複習函式定義、回傳值、字串和 `if __name__ == '__main__':` 的重要性。
- **範本**：
  ```python
  # 範例一：函式與回傳值
  def add(a, b):
      result = a + b
      return result

  sum_value = add(5, 3)
  print(f"5 + 3 的結果是: {sum_value}") # f-string 格式化字串

  # 範例二：主程式進入點
  # 如果這個檔案是被其他檔案 import 的，這段程式碼就不會執行
  if __name__ == '__main__':
      print("這個檔案被直接執行了！")
  ```
