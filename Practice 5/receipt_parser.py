import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()



price_pattern = r"\b\d+[.,]\d{2}\b"
prices = re.findall(price_pattern, text)

prices_float = [float(p.replace(",", ".")) for p in prices]
total = sum(prices_float)




date_match = re.search(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
date = date_match.group() if date_match else None




time_match = re.search(r"\b\d{2}:\d{2}:\d{2}\b", text)
time = time_match.group() if time_match else None




payment_match = re.search(r"(CASH|CARD|VISA|MASTERCARD)", text, re.IGNORECASE)
payment = payment_match.group() if payment_match else "Unknown"




products = re.findall(r"[A-Za-zА-Яа-я ]+(?=\s+\d+[.,]\d{2})", text)





data = {
    "date": date,
    "time": time,
    "products": products,
    "prices": prices_float,
    "total": round(total, 2),
    "payment_method": payment
}

print(json.dumps(data, indent=4, ensure_ascii=False))