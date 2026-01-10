# Secure AI-Based Voice Communication (Backend)


✅ STEP 1 — Clone the Repository
git clone https://github.com/ShifanaKoormath/Secure-AI-Based-Voice-Communication.git


This will create a folder:

Secure-AI-Based-Voice-Communication

✅ STEP 2 — Navigate to the Backend Folder
cd Secure-AI-Based-Voice-Communication\backend

✅ STEP 3 — Create and Activate Python Virtual Environment
python -m venv venv


Activate it:

.\venv\Scripts\activate


After activation, your prompt should show:

(venv) PS C:\Users\…\backend>


If it doesn’t show (venv) — stop and fix that before moving on.

✅ STEP 4 — Install All Dependencies

Make sure requirements.txt includes AI and backend packages.

Then run:

pip install -r requirements.txt



This will install:

FastAPI

Uvicorn

Cryptography

Whisper & Torch

Transformers & scikit-learn


(updated requirements installation:

pip install torch torchaudio soundfile numpy scipy




)




✅ STEP 5 — Run the Server

Once all deps are installed and (venv) is active:

uvicorn app.main:app --reload


If that fails:

python -m uvicorn app.main:app --reload

✅ STEP 6 — Open the API

After the server starts, open in your browser:

http://127.0.0.1:8000


And for documentation:

http://127.0.0.1:8000/docs


This is where you test your endpoints.

⚠️ TROUBLESHOOTING TIPS
🔹 If (venv) is missing

Make sure you are in the backend folder when you run:

.\venv\Scripts\activate

🔹 If uvicorn is not found

Make sure your virtual environment is active ((venv) must appear).
Then run:

python -m uvicorn app.main:app --reload

🔹 If port 8000 is busy

Run:

uvicorn app.main:app --reload --port 8001


Then open:

http://127.0.0.1:8001/docs

📌 CHECKLIST (Quick)

Before running the server:

✔ You are in Secure-AI-Based-Voice-Communication\backend
✔ (venv) is active
✔ Dependencies installed
✔ No errors during install


This repository contains the backend implementation for a **Secure AI-Based Voice Communication System**, developed as an academic prototype and delivered as a stable, demo-ready backend.

The system demonstrates **secure voice handling**, **speech-to-text conversion**, and **AI-based message analysis**, aligned with typical college project requirements and feasibility constraints.

---

## 🔐 Core Features

- Secure voice transmission using **X25519 key exchange**
- **AES-256-GCM** encryption for voice data
- Encrypted voice storage (no plaintext audio at rest)
- Speech-to-text conversion using a pretrained ASR model
- AI-based message classification:
  - Harmful content detection
  - Urgency detection
- WhatsApp-like asynchronous voice messaging flow

---

## 🧠 System Architecture

Voice (.wav)
→ Key Exchange (X25519)
→ Encryption (AES-256-GCM)
→ Encrypted Storage
→ Decryption
→ Speech-to-Text (ASR)
→ AI Classification
→ SAFE / HARMFUL / URGENT

yaml
Copy code

---

## 🧩 Technology Mapping

| Component | Technology Used |
|---------|-----------------|
| Backend Framework | FastAPI (Python) |
| Key Exchange | X25519 |
| Encryption | AES-256-GCM |
| Speech Enhancement | DCCRN (architectural integration) |
| Speech Recognition | Whisper (pretrained ASR) |
| Harmful Detection | CNN–LSTM inspired prototype |
| Urgency Detection | BERT (pretrained inference) |

---

## 📌 Implementation Notes

- **DCCRN** is included at the architectural level. Model training is excluded to maintain feasibility and demo stability.
- **CNN–LSTM** is implemented at prototype level to demonstrate harmful content detection logic.
- **BERT** is used in pretrained inference mode for urgency classification.
- The system prioritizes **secure integration and working demonstration** over model training.

---

## 🚀 API Endpoints

### Upload Voice
POST /api/send-voice

yaml
Copy code
Encrypts and stores voice data securely.

---

### List Messages
GET /api/messages

yaml
Copy code
Returns message metadata.

---

### Transcribe & Classify
GET /api/transcribe/{message_id}

yaml
Copy code
Decrypts audio, converts speech to text, and classifies the message as:
- `SAFE`
- `HARMFUL`
- `URGENT`

---

## ▶️ Running the Backend

### 1. Create and activate virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
This installs:

FastAPI and backend dependencies

Cryptography libraries

Speech-to-text (Whisper + Torch)

NLP libraries (Transformers, scikit-learn)

3. Run the server
bash
Copy code
uvicorn app.main:app --reload
4. Access the API
Base URL: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

⚠️ Important Notes
This project is an academic prototype, not a production system

Encrypted audio data and private keys are intentionally excluded from version control

Designed for demo reliability and clear explanation during evaluation

📈 Future Scope
Full DCCRN model integration

Trained CNN–LSTM classifier

Real-time voice communication

Android client-side encryption and inference

📄 License
This project is intended for academic demonstration purposes only.