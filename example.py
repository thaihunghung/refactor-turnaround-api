import requests

data = {
    "sitekey": "3x00000000000000000000FF",
    "invisible": False,
    "url": "https://2captcha.com/demo/cloudflare-turnstile",
    "proxy": None
}

r = requests.post("http://127.0.0.1:5000/solve", json=data)

print("Status code:", r.status_code)
print("Response text:", r.text)

if r.headers.get("Content-Type") == "application/json" and r.text:
    token = r.json()["token"]
    print("Token:", token)
else:
    print("Không nhận được phản hồi JSON hợp lệ.")
