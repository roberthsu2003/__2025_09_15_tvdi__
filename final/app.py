from flask import Flask, render_template, jsonify, request
from sklearn.datasets import fetch_california_housing, load_iris
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, accuracy_score, confusion_matrix
import numpy as np

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/regression")
def regression():
    return render_template("regression.html")

@app.route("/knn")
def knn():
    return render_template("knn.html")

@app.route("/api/regression/data")
def regression_data():
    """線性迴歸 API - 使用加州房價資料集（簡化版）"""
    try:
        # 載入加州房價資料集
        housing = fetch_california_housing()

        # 只使用前 200 筆資料作為展示
        sample_size = 200
        X_full = housing.data[:sample_size]
        y_full = housing.target[:sample_size]  # 房價（單位：十萬美元）

        # 使用「平均房間數」作為預測特徵（索引 0）
        # 特徵: 平均房間數（AveRooms）
        feature_idx = 0
        X = X_full[:, feature_idx].reshape(-1, 1)
        y = y_full * 10  # 轉換為萬美元，更易理解

        # 分割訓練和測試資料（80/20）
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # 訓練線性迴歸模型
        model = LinearRegression()
        model.fit(X_train, y_train)

        # 預測
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        # 計算評估指標
        r2 = r2_score(y_test, y_test_pred)
        mse = mean_squared_error(y_test, y_test_pred)
        rmse = np.sqrt(mse)

        # 生成迴歸線資料（用於繪圖）
        X_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
        y_line = model.predict(X_line)

        # 準備回應資料
        response = {
            "success": True,
            "data": {
                "train": {
                    "x": X_train.flatten().tolist(),
                    "y": y_train.tolist(),
                    "y_pred": y_train_pred.tolist()
                },
                "test": {
                    "x": X_test.flatten().tolist(),
                    "y": y_test.tolist(),
                    "y_pred": y_test_pred.tolist()
                },
                "regression_line": {
                    "x": X_line.flatten().tolist(),
                    "y": y_line.tolist()
                }
            },
            "metrics": {
                "r2_score": round(r2, 4),
                "mse": round(mse, 2),
                "rmse": round(rmse, 2),
                "coefficient": round(model.coef_[0], 2),
                "intercept": round(model.intercept_, 2)
            },
            "description": {
                "dataset": "加州房價資料集",
                "samples": len(y),
                "train_size": len(y_train),
                "test_size": len(y_test),
                "feature_name": "平均房間數",
                "feature_unit": "間",
                "target_name": "房價",
                "target_unit": "萬美元",
                "info": "此資料集取自 1990 年加州人口普查資料"
            }
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/api/regression/predict")
def regression_predict():
    """線性迴歸預測 API - 根據房間數預測房價"""
    try:
        # 取得使用者輸入的房間數
        rooms = float(request.args.get('rooms', 5.0))

        # 載入資料並訓練模型（與上面相同）
        housing = fetch_california_housing()
        sample_size = 200
        X = housing.data[:sample_size, 0].reshape(-1, 1)  # 平均房間數
        y = housing.target[:sample_size] * 10  # 房價（萬美元）

        # 訓練模型
        model = LinearRegression()
        model.fit(X, y)

        # 預測
        X_input = np.array([[rooms]])
        predicted_price = model.predict(X_input)[0]

        response = {
            "success": True,
            "input": {
                "rooms": rooms,
                "unit": "間"
            },
            "prediction": {
                "price": round(predicted_price, 2),
                "unit": "萬美元"
            },
            "formula": {
                "coefficient": round(model.coef_[0], 2),
                "intercept": round(model.intercept_, 2),
                "equation": f"房價 = {round(model.coef_[0], 2)} × 房間數 + {round(model.intercept_, 2)}"
            }
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route("/api/knn/data")
def knn_data():
    """KNN 分類 API - 使用鳶尾花資料集"""
    try:
        # 載入鳶尾花資料集
        iris = load_iris()
        X = iris.data
        y = iris.target

        # 特徵名稱翻譯為繁體中文
        feature_names_zh = ["花萼長度", "花萼寬度", "花瓣長度", "花瓣寬度"]
        target_names_zh = ["山鳶尾", "變色鳶尾", "維吉尼亞鳶尾"]

        # 取得特徵索引（預設使用花瓣長度和花瓣寬度）
        feature_x = int(request.args.get('feature_x', 2))
        feature_y = int(request.args.get('feature_y', 3))
        k_neighbors = int(request.args.get('k', 5))

        # 驗證參數
        if feature_x < 0 or feature_x >= X.shape[1]:
            feature_x = 2
        if feature_y < 0 or feature_y >= X.shape[1]:
            feature_y = 3
        if k_neighbors < 1 or k_neighbors > 20:
            k_neighbors = 5

        # 使用兩個特徵進行分類
        X_2d = X[:, [feature_x, feature_y]]

        # 分割訓練和測試資料
        X_train, X_test, y_train, y_test = train_test_split(
            X_2d, y, test_size=0.3, random_state=42
        )

        # 訓練 KNN 分類器
        knn = KNeighborsClassifier(n_neighbors=k_neighbors)
        knn.fit(X_train, y_train)

        # 預測
        y_pred = knn.predict(X_test)

        # 計算評估指標
        accuracy = accuracy_score(y_test, y_pred)
        conf_matrix = confusion_matrix(y_test, y_pred)

        # 準備回應資料
        response = {
            "success": True,
            "feature_names": feature_names_zh,
            "target_names": target_names_zh,
            "current_features": {
                "x": feature_names_zh[feature_x],
                "y": feature_names_zh[feature_y],
                "x_idx": feature_x,
                "y_idx": feature_y
            },
            "k_neighbors": k_neighbors,
            "data": {
                "train": {
                    "x": X_train[:, 0].tolist(),
                    "y": X_train[:, 1].tolist(),
                    "labels": y_train.tolist()
                },
                "test": {
                    "x": X_test[:, 0].tolist(),
                    "y": X_test[:, 1].tolist(),
                    "labels": y_test.tolist(),
                    "predictions": y_pred.tolist()
                }
            },
            "metrics": {
                "accuracy": round(accuracy, 4),
                "confusion_matrix": conf_matrix.tolist()
            },
            "description": {
                "dataset": "鳶尾花資料集",
                "samples": len(y),
                "train_size": len(y_train),
                "test_size": len(y_test),
                "classes": len(target_names_zh)
            }
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


def main():
    """啟動應用（教學用：啟用 debug 模式）"""
    # 在開發環境下使用 debug=True，部署時請關閉
    app.run(debug=True)

if __name__ == "__main__":
    main()