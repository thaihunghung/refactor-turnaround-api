import os
import time
import json
import flask
import requests
from playwright.sync_api import sync_playwright

def setup_solver():
    os.makedirs("utils", exist_ok=True)
    files = {
        "solver.py": "https://raw.githubusercontent.com/thaihunghung/solver/refs/heads/main/solver.py",
        "page.html": "https://raw.githubusercontent.com/thaihunghung/solver/refs/heads/main/page.html"
    }
    for filename, url in files.items():
        with open(f"utils/{filename}", "w", encoding="utf-8") as f:
            f.write(requests.get(url).text)
            
setup_solver()
app = flask.Flask(__name__)
from utils import solver  # after setup

@app.route("/solve", methods=["POST"])
def solve_route():
    data = flask.request.json
    sitekey = data["sitekey"]
    invisible = data["invisible"]
    url = data["url"]
    proxy = data.get("proxy")

    with sync_playwright() as p:
        s = solver.Solver(p, proxy=proxy, headless=True)
        start = time.time()
        print(f"Solving captcha (proxy: {proxy})")
        token = s.solve(url, sitekey, invisible)
        print(f"Took {time.time() - start:.2f}s, Token: {token[:10]}")
        return build_response(token)
    

def build_response(token):
    return flask.jsonify({
        "status": "success" if token != "failed" else "error",
        "token": None if token == "failed" else token
    })

if __name__ == "__main__":
    app.run(port=5001, debug=False, use_reloader=False, threaded=False)
