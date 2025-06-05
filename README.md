# turnaround-api (Refactored)

Cloudflare Turnstile solver API, based on [turnaround](https://github.com/Body-Alhoha/turnaround).  
Originally forked from [Euro-pol/turnaround-api](https://github.com/Euro-pol/turnaround-api).

> ✅ Refactored by **TRAN THAI HUNG**  
> For better maintainability, structure, and readability.

---

## Features

- Solve Cloudflare Turnstile challenges via API
- Based on Playwright automation
- Supports Chromium, Firefox, and WebKit
- Simple setup using Python + Flask

---

## Installing

### 1. Create Virtual Environment (Python 3.8 Recommended)

```bash
python3.8 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

```

### 2. Install Required Packages

```bash
pip install -r requirements.txt

```
### 3. Install Playwright Browsers

If this is your first time using Playwright, or you're inside a virtual environment:
```bash
python -m playwright install

```
To install Firefox in addition to default Chromium:
```bash
python -m playwright install firefox

```
### 4. Run the Server

```bash
python main.py


```