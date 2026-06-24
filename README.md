# Selenium-Python 🧪

A test automation framework built with **Selenium WebDriver** and **Python**, following the **Page Object Model (POM)** design pattern. Includes end-to-end tests, data-driven testing, and CI/CD integration with Jenkins.

---

## 🛠️ Tech Stack

- Python 3.x
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Jenkins (CI/CD)
- GitHub Actions (optional)

---

## 📁 Project Structure

```
Selenium-Python/
│
├── conftest.py              # Fixtures and browser setup
│
│
├── test_data/              # Test data files
│
│
├── tests/                   # Test files
│   ├── test_1.py
│   ├── test_2.py
│   └── test_e2e.py
│
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.x installed
- Google Chrome / Firefox / Edge installed
- pip package manager

### 1. Clone the repository

```bash
git clone https://github.com/y-srinath/Selenium-Python.git
cd Selenium-Python
```

### 2. Install dependencies

```bash
pip install selenium pytest pytest-html
```

### 3. Run tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest test_e2e.py

# Run tests on a specific browser
pytest --browser=chrome
pytest --browser=firefox

# Run only smoke tests
pytest -m smoke

# Run failed tests only
pytest --last-failed

# Run tests in parallel
pytest -n 4
```

---

🌐 Browser Support

| Browser | Supported |
| ------- | --------- |
| Chrome  | ✅        |
| Firefox | ✅        |
| Edge    | ✅        |

---

📊 Test Reports

HTML reports are generated in the `reports/` folder after each run:

```bash
pytest --html=reports/report.html
```

---

🔑 Key Features

- **Page Object Model** — separates test logic from page interactions for maintainability
- **Data-Driven Testing** — parameterized fixtures to run tests with multiple data sets
- **Cross-Browser Testing** — run tests on Chrome, Firefox, or Edge via command line
- **Custom Markers** — tag and filter tests with `@pytest.mark.smoke`, `@pytest.mark.regression`
- **CI/CD Ready** — integrated with Jenkins for automated test execution on every push

---

🧩 Example Test

```python
def test_e2e(browserInstance):
    driver = browserInstance
    wait = WebDriverWait(driver, 10)

    # Navigate to shop
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='shop']"))).click()

    # Add product to cart
    products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card h-100']")))
    for product in products:
        if product.find_element(By.XPATH, "div/h4/a").text == "Nokia Edge":
            product.find_element(By.XPATH, "div/button").click()
            break

    # Assert success
    success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success"))).text
    assert "Success! Thank you!" in success_message
```

---

👤 Author

**Srinath Yellepeddi**  
[GitHub](https://github.com/y-srinath)

---

📄 License

This project is for learning and practice purposes.
