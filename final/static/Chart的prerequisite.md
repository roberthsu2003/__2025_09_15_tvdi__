

要讓學生學會使用 Chart.js，特別是像您範例中的 `scatter` (散點圖)，他們確實需要一些 JavaScript 的基礎。Chart.js 本身是一個 JavaScript **函式庫 (Library)**，它把複雜的畫布 (Canvas) 繪圖操作封裝成了簡單易用的 API。

這是在教 Chart.js 之前，學生必須掌握的「先修技巧」：

---

### 一、 Chart.js 的先修技巧說明與範例

#### 1. HTML：圖表的「畫布」 (`<canvas>`)

Chart.js 需要一個 HTML 元素來當作畫布，它會在上面繪製圖表。這個元素就是 `<canvas>`。

- **說明：** `<canvas>` 標籤就像在網頁上放了一塊空白的畫布。我們必須給它一個 `id`，這樣 JavaScript 才能準確地找到「要在哪一塊畫布上作畫」。
- **範例 (`index.html`)：**

    HTML

```other
<!DOCTYPE html>
<html>
<head>
    <title>圖表畫布</title>
    <style>
        /* 幫畫布加個框線，並限制大小，方便觀察 */
        .chart-container {
            width: 500px;
            height: 300px;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>
    <h1>我的圖表</h1>
    <div class="chart-container">
        <canvas id="myChartCanvas"></canvas>
    </div>

    </body>
</html>
```

#### 2. JavaScript：如何「引入」函式庫

- **說明：** Chart.js 不是 JavaScript 內建的功能，它是一個「外掛」。我們必須在 HTML 中使用 `<script>` 標籤，透過 CDN (內容傳遞網路) 把它載入進來。
    - **重點：** 引入函式庫的 `<script>` 標籤，**必須**放在我們自己寫的圖表腳本 (`<script>`) 之前，這樣我們在用 `new Chart(...)` 時，瀏覽器才知道 `Chart` 是什麼東西。
- **範例 (加在 `<body>` 標籤結束前)：**

    HTML

```other
...
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
        // 我們自己的 JS 程式碼會寫在這裡
        console.log("Chart.js 已經載入，現在可以使用 'Chart' 這個物件了。");
    </script>
</body>
</html>
```

#### 3. JavaScript：DOM 操作 (`getElementById` 和 `getContext`)

- **說明：** 我們的 JS 程式碼需要「抓到」那塊 ID 為 `myChartCanvas` 的畫布。
    1. `document.getElementById('myChartCanvas')`：這會抓到 `<canvas>` 這個 HTML 元素。
    2. `.getContext('2d')`：這是對 `<canvas>` 元素呼叫的一個方法，意思是「請給我這塊畫布的 2D 繪圖工具箱」，Chart.js 需要這個工具箱才能開始畫圖。
- **範例 (寫在第二個 `<script>` 標籤內)：**

    JavaScript

```other
// 1. 抓到畫布元素
const canvasElement = document.getElementById('myChartCanvas');

// 2. 取得 2D 繪圖上下文 (Context)
const ctx = canvasElement.getContext('2d');

console.log(ctx); // 學生可以在控制台看到一個 CanvasRenderingContext2D 物件
```

#### 4. JavaScript：物件 (Objects) 與陣列 (Arrays)

- **說明：** 這是**最重要**的先修技巧。Chart.js 的**所有設定**都是透過一個巨大的 JavaScript **物件 (Object)** 來完成的。而圖表中的**資料**，通常是放在**陣列 (Array)** 中。
- **範例 1：簡單的陣列 (適用於長條圖的標籤)**

    JavaScript

```other
// 陣列 (Array) - 用中括號 []
let labels = ['一月', '二月', '三月'];
let data = [100, 150, 80];
```

- **範例 2：簡單的物件 (適用於圖表設定)**

    JavaScript

```other
// 物件 (Object) - 用大括號 {}，由 "鍵" (key) 和 "值" (value) 組成
let myOptions = {
    responsive: true, // 鍵 'responsive'，值 'true' (布林值)
    maintainAspectRatio: false, // 鍵 'maintainAspectRatio'，值 'false'

    // "值" 也可以是另一個 "物件" (形成巢狀結構)
    plugins: {
        title: {
            display: true,
            text: '我的圖表標題' // 鍵 'text'，值 '我的圖表標題' (字串)
        }
    }
};
```

- **範例 3：物件的陣列 (Array of Objects) - [散點圖的關鍵]**
    - **說明：** 對於散點圖，每個點都需要 `x` 和 `y` 兩個值。因此，`data` 陣列裡面放的不再是單純的數字，而是一個個代表「點」的**物件**。

    JavaScript

```other
let scatterData = [
    { x: 5,  y: 20 },  // 第 1 個點 (x=5, y=20)
    { x: 10, y: 30 },  // 第 2 個點
    { x: 15, y: 25 }   // 第 3 個點
];
```

    這就是您範例程式碼中 `data: [{x: x, y: y}]` 的由來。

---

### 二、 完整說明 Scatter (散點圖) 與範例

#### 1. 什麼是 Scatter (散點圖)？

散點圖 (Scatter Chart) 用來顯示兩個**數值變數**之間的關係。

- **用途：** 觀察資料的**分佈趨勢**、**相關性**或**群集**。
- **舉例：**
    - X 軸是「學習時數」，Y 軸是「考試成績」。
    - X 軸是「廣告花費」，Y 軸是「銷售額」。
    - (如同您的範例) X 軸是「房間數」，Y 軸是「房價」。

#### 2. Chart.js 的 Scatter 圖表結構

建立一個 Chart.js 圖表，我們需要 `new Chart(ctx, config)`。

- `ctx`：就是我們先修技巧中拿到的 2D 繪圖工具箱。
- `config`：這就是那個巨大的設定**物件**，它包含 `type`、`data` 和 `options`。

#### `type: 'scatter'`

這告訴 Chart.js 我們要畫的是散點圖。

#### `data` 物件

這個物件用來存放所有要顯示的資料。

- `data.datasets`：這是一個**陣列**，因為一張圖上可以有多組資料（例如您的範例中有「訓練資料」和「測試資料」）。
- `data.datasets[0]`：這是第一組資料的設定**物件**。
    - `label`: '身高體重分佈' (這組資料的名稱，會顯示在圖例上)。
    - `data`: `[{x: 170, y: 65}, {x: 155, y: 50}, ...]` (**[關鍵]** 散點圖的資料必須是這種 `x`, `y` 物件的陣列)。
    - `backgroundColor`: 'rgba(255, 99, 132, 0.6)' (點的顏色)。

#### `options` 物件

這個物件用來設定圖表的外觀和行為 (例如標題、座標軸)。

- `options.scales`：設定座標軸。
- `options.scales.x`：設定 X 軸。
    - `title: { display: true, text: '身高 (cm)' }` (顯示 X 軸的標題)。
- `options.scales.y`：設定 Y 軸。
    - `title: { display: true, text: '體重 (kg)' }` (顯示 Y 軸的標題)。
- `options.plugins.title`：設定圖表主標題。

#### 3. 完整的 Scatter 圖表範例 (可直接執行)

這是一個單一的 HTML 檔案，整合了所有先修技巧，建立了一個簡單的「身高 vs 體重」散點圖。學生可以直接儲存成 `.html` 檔案並用瀏覽器打開。

HTML

```other
<!DOCTYPE html>
<html>
<head>
    <title>Chart.js 散點圖 (Scatter) 範例</title>
    <style>
        /* 給圖表一個固定的繪圖區域 */
        .chart-container {
            position: relative;
            width: 80vw;
            height: 60vh;
            margin: 20px auto; /* 置中 */
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>

    <h1>範例：學生身高 vs 體重 散點圖</h1>

    <div class="chart-container">
        <canvas id="scatterChart"></canvas>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

    <script>
        // 確保頁面載入完成 (這和您範例的 DOMContentLoaded 意思相同)
        window.onload = function() {
            
            // 3. JS：抓取畫布和 2D 工具箱
            const ctx = document.getElementById('scatterChart').getContext('2d');
            
            // 4. JS (物件與陣列)：準備圖表資料
            // 散點圖的資料是 "物件的陣列"
            const studentData = [
                { x: 158, y: 55 },
                { x: 162, y: 58 },
                { x: 165, y: 62 },
                { x: 170, y: 65 },
                { x: 173, y: 70 },
                { x: 175, y: 68 },
                { x: 180, y: 75 },
                { x: 182, y: 78 }
            ];

            // 建立圖表
            const myScatterChart = new Chart(ctx, {
                // [關鍵] 指定圖表類型為 'scatter'
                type: 'scatter',
                
                // [關鍵] data 物件，存放資料
                data: {
                    datasets: [
                        {
                            label: '學生身高體重 (第一組)',
                            data: studentData, // 放入我們的資料
                            backgroundColor: 'rgba(255, 99, 132, 0.6)', // 點的顏色
                            borderColor: 'rgba(255, 99, 132, 1)',
                            pointRadius: 8, // 點的大小
                            pointHoverRadius: 10 // 滑鼠移上去時點的大小
                        }
                        // 如果有第二組資料，可以在這裡加 (例如您範例的 "測試資料")
                        /*
                        , {
                            label: '第二組資料',
                            data: [{x: 160, y: 70}, {x: 170, y: 80}],
                            backgroundColor: 'rgba(54, 162, 235, 0.6)'
                        }
                        */
                    ]
                },
                
                // [關鍵] options 物件，設定圖表外觀
                options: {
                    responsive: true,
                    maintainAspectRatio: false, // 讓圖表填滿容器
                    
                    // 座標軸設定
                    scales: {
                        x: { // X 軸
                            type: 'linear', // 軸的類型是「線性」
                            position: 'bottom',
                            title: {
                                display: true,
                                text: '身高 (cm)',
                                font: { size: 16 }
                            }
                        },
                        y: { // Y 軸
                            title: {
                                display: true,
                                text: '體重 (kg)',
                                font: { size: 16 }
                            }
                        }
                    },
                    
                    // 插件 (Plugins) 設定，例如標題、提示
                    plugins: {
                        title: {
                            display: true,
                            text: '身高與體重的關係',
                            font: { size: 20 },
                            padding: 20
                        },
                        tooltip: {
                            callbacks: {
                                // 自訂提示文字
                                label: function(context) {
                                    let label = context.dataset.label || '';
                                    let xVal = context.parsed.x;
                                    let yVal = context.parsed.y;
                                    return `${label}: ${xVal} cm, ${yVal} kg`;
                                }
                            }
                        }
                    }
                }
            });
        };
    </script>

</body>
</html>
```

---

### 三、 Chart.js 官方說明書

這是 Chart.js 最新的官方文件，是最好的學習資源。

- 官方文件首頁 (v4.x - 最新版)：

    [https://www.chartjs.org/docs/latest/](https://www.chartjs.org/docs/latest/)

- **建議學生閱讀的順序：**
    1. **Getting Started (開始使用)：** [https://www.chartjs.org/docs/latest/getting-started/](https://www.chartjs.org/docs/latest/getting-started/) (教如何安裝和建立第一張圖)。
    2. **General (通用設定)：** [https://www.chartjs.org/docs/latest/general/](https://www.chartjs.org/docs/latest/general/) (教資料結構、顏色、字型等)。
    3. **Charts > Scatter (散點圖)：** [https://www.chartjs.org/docs/latest/charts/scatter.html](https://www.chartjs.org/docs/latest/charts/scatter.html) (專門針對散點圖的設定和範例)。

