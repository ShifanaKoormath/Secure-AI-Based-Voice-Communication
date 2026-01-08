python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt



1️⃣ Install STT dependency

Inside (venv):

pip install openai-whisper torch

pip install torch transformers scikit-learn


Still inside (venv):

uvicorn app.main:app --reload

http://127.0.0.1:8000
http://127.0.0.1:8000/docs
