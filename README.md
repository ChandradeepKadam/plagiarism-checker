# 🧩 Code Plagiarism Checker PRO

A web-based application that detects similarity between two code files using algorithmic comparison and highlights matching lines.

---

## 🚀 Features

- 🔍 Compare two code files
- 📊 Overall similarity percentage
- 🎯 Line-by-line comparison
- ✨ Word-level highlighting
- 📈 Graph visualization (Chart)
- 🎨 Clean and modern UI

---

## 🛠️ Technologies Used

### Frontend:
- HTML
- CSS
- JavaScript

### Backend:
- Python (Flask)

### Libraries:
- Flask
- Flask-CORS
- ReportLab (for PDF)
- Chart.js (for graph)

---

## 📁 Project Structure


plagiarism-checker/
│
├── backend/
│ └── app.py
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/your-username/plagiarism-checker.git

cd plagiarism-checker


### 2️⃣ Create Virtual Environment (optional but recommended)

python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Dependencies

pip install flask flask-cors reportlab


### 4️⃣ Run Backend

cd backend
python app.py


### 5️⃣ Run Frontend
- Open `frontend/index.html` in browser

---

## 📊 How It Works

1. Upload two code files  
2. System tokenizes code into words  
3. Uses Jaccard similarity algorithm  
4. Finds matching lines  
5. Highlights common words  
6. Displays similarity score and chart  

---

## 🧠 Algorithm Used

**Jaccard Similarity**


Similarity = Intersection / Union


This measures similarity between two sets of tokens.

---

## 📌 Supported File Types

- `.py`
- `.java`
- `.c`
- `.cpp`
- `.txt`

---

## ❌ Not Supported

- `.class`
- `.exe`
- Binary files

---

## 📸 Output Preview

<img width="1917" height="917" alt="image" src="https://github.com/user-attachments/assets/ad70fe83-3699-4238-a594-dafe6cbd8947" />


---

## 👨‍💻 Team Members

- Member 1: Frontend Development  
- Member 2: Backend Development  

---

## 🎯 Future Improvements
  
- 📁 Multiple file comparison  
- 🤖 AI-based plagiarism detection  
- 🌐 Deploy online  

---

## 📄 License

This project is for educational purposes.

---

## ⭐ Conclusion

This project helps detect code plagiarism efficiently using algorithmic techniques and provides visual insights for better understanding.
