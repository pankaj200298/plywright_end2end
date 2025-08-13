# Playwright End-to-End Testing with Python (Sync Mode)

This project demonstrates **end-to-end test automation** using **Playwright with Python** in **sync mode**, following the **Page Object Model (POM)** structure.  
It implements a **user registration with random data generation** and a **login test using stored credentials**, simulating a real-world web application flow.


## 📂 Project Structure

plywright_end2end/
│── tests/ # Test files
│── pages/ # Page Object Model classes
│── utils/ # Helper functions (data generation, file handling)
│── conftest.py # Pytest fixtures (browser/page setup)
│── requirements.txt # Dependencies
│── README.md # Project documentation

## 🚀 Features
- **Playwright Sync API** for browser automation
- **Random email & mobile generation** to avoid test collisions
- **Page Object Model (POM)** for code reusability & maintainability
- **Data persistence** in `test_data.json` to share credentials between tests
- **Cross-browser support** (Chromium, Firefox, WebKit)
- **Full end-to-end flow**: Register → Login → Verify

---

## 🛠 Installation

### 1️⃣ Clone the Repository
git clone https://github.com/pankaj200298/plywright_end2end.git
cd plywright_end2end

###2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
###3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
playwright install

🧪 Running Tests
Run all tests
pytest -v
Run a specific test file
pytest tests/test_registration.py -v
Run with HTML report
pytest --html=reports/report.html --self-contained-html

💡 Best Practices
Keep locators inside POM classes, never in tests

Use fixtures for browser/page setup & teardown

Persist dynamic data to avoid hardcoding

Add assertions after each significant step

Store sensitive data in .env files

#📌 Author
**Pankaj Chanekar
**pankaj.chanekar98@gmail.com
