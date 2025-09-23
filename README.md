# 🍷 FastAPI Wine Classifier

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-green)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4%2B-orange)

A **FastAPI** service that serves a **DecisionTreeClassifier** trained on the **Wine** dataset (scikit-learn).  
Includes a simple browser **dashboard** for making predictions.

---

## ⚙️ Setup

```bash
# clone (SSH)
git clone git@github.com:saumith/FastAPI.git
cd FastAPI

# (optional) create & activate a venv
python3 -m venv fastapi_lab1_env
source fastapi_lab1_env/bin/activate

# install dependencies
pip install -r requirements.txt
```

---

## ▶️ How to Run

### Retrain the model (if needed)
```bash
cd src
python train.py
```

### Start the API
```bash
uvicorn main:app --reload
```

### Open the app
- Health: http://127.0.0.1:8000/
- Docs:   http://127.0.0.1:8000/docs
- UI:     http://127.0.0.1:8000/dashboard

---

## 🖼️ Result

Here’s the dashboard in action with a sample prediction:

![Result Dashboard](assets/Result_Dashboard.png)

---

## 🧠 Notes

- **Dataset:** scikit-learn *Wine* (13 numerical features).
- **Model:** `DecisionTreeClassifier` (training logic unchanged from Iris version).
- **Target encoding:**
  - `0 → Class_0`
  - `1 → Class_1`
  - `2 → Class_2`

---

## 📂 Project Structure

```
FastAPI/
│── assets/
│   └── Result_Dashboard.png
│── model/
│   └── wine_model.pkl
│── src/
│   ├── data.py          # loads Wine data & train/test split
│   ├── train.py         # trains DecisionTree & saves model
│   ├── predict.py       # loads model & predicts
│   ├── main.py          # FastAPI app (+ /dashboard static mount)
│   └── static/
│       └── index.html   # dashboard UI
│── requirements.txt
│── README.md
```

---

## 🚀 Submit / Update on GitHub

```bash
# from repo root
git add src/ model/ assets/ README.md requirements.txt
git commit -m "Assignment submission: FastAPI Wine Classifier with dashboard"
git push -u origin main
```

---

## 🔧 Troubleshooting

- **Model dtype / pickle error:** retrain inside the same environment you serve from.
  ```bash
  rm -f model/wine_model.pkl
  cd src && python train.py
  ```
- **Dashboard 404:** ensure `src/static/index.html` exists and `main.py` mounts:
  ```python
  from fastapi.staticfiles import StaticFiles
  app.mount("/dashboard", StaticFiles(directory="static", html=True), name="dashboard")
  ```
- **Image not showing in README:** use a **relative path** (e.g., `assets/Result_Dashboard.png`), not a local absolute path.
