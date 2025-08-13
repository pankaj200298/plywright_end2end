# 🎯 Playwright End-to-End Testing with Python (Sync Mode)

This project demonstrates **end-to-end test automation** using **Playwright with Python** in **sync mode**, following the **Page Object Model (POM)** structure.  
It covers a complete user journey: **Registration → Login → Verification**, with **random data generation** and **persistent storage** for reusability.

---

## 📂 Project Structure
```
plywright_end2end/
│── tests/            # Test files
│── pages/            # Page Object Model classes
│── utils/            # Helper functions (data generation, file handling)
│── conftest.py       # Pytest fixtures (browser/page setup & teardown)
│── requirements.txt  # Dependencies
│── README.md         # Project documentation
```

---

## 🚀 Features
- ⚡ **Playwright Sync API** for browser automation  
- 🎯 **Page Object Model (POM)** for maintainable, reusable code  
- 🔄 **Random email & mobile generation** to prevent collisions  
- 💾 **Data persistence** in `test_data.json` for cross-test credential sharing  
- 🌐 **Cross-browser support** (Chromium, Firefox, WebKit)  
- 🔍 **Assertions** at each critical step for reliability  
- 📊 **HTML reporting** with `pytest-html`  

---

## ⚡ Installation

**1️⃣ Clone the repository**
```bash
git clone https://github.com/pankaj200298/plywright_end2end.git
cd plywright_end2end
```

**2️⃣ Create & activate virtual environment**

**Mac/Linux**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**3️⃣ Install dependencies**
```bash
pip install -r requirements.txt
playwright install
```

---

## 🧪 Running Tests

**Run all tests**
```bash
pytest -v
```

**Run a specific test**
```bash
pytest tests/test_registration.py -v
```

**Run with HTML report**
```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 💡 Best Practices Followed
✅ Locators are **only inside POM classes** (no locators in tests)  
✅ **Fixtures** manage browser/page lifecycle  
✅ **Dynamic test data** stored externally (no hardcoding)  
✅ **Sensitive credentials** stored in `.env` (gitignored)  
✅ **Assertions** after each major step for reliability and better debugging  

---

## 📌 Author
**Pankaj Chanekar**  
📧 pankaj.chanekar98@gmail.com  
