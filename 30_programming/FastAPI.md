# ローカル起動
１：仮想環境有効化（backend ディレクトリ内）
```
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload --port 8000
```
２：requirements インストール（仮想環境有効化後）
```
pip install -r requirements.txt
```
３：動作確認（簡易 health エンドポイント（app/main.py））
- app/main.py
```Python
from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```
```
```
```
