import xml.etree.ElementTree as ET
import json
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xml_file = "sofas.xml"
tree = ET.parse(xml_file)
root = tree.getroot()

sofas = []
for offer in root.findall(".//offer"):
    model = offer.find("name").text
    price = int(offer.find("price").text)

    sales = {f"Месяц {i + 1}": random.randint(5, 50) for i in range(12)}

    sofas.append({
        "model": model,
        "price": price,
        "sales": sales
    })

json_file = "sales.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump({"sofas": sofas}, f, ensure_ascii=False, indent=4)

print(f"Данные сохранены в {json_file}")


def calculate_avg(sales):
    return np.mean(sales)

def calculate_msd(sales):
    return np.std(sales, ddof=1)

def forecast_next_month(avg, msd):
    return round(random.normalvariate(avg, msd), 1)

def calculate_confidence_interval(avg, msd, n=12, confidence=0.95):
    z_score = 1.96
    margin_of_error = z_score * (msd / np.sqrt(n))
    lower_bound = avg - margin_of_error
    upper_bound = avg + margin_of_error
    return lower_bound, upper_bound

forecast_data = {}
reliability_check = {}

for sofa in sofas:
    model = sofa["model"]
    sales = list(sofa["sales"].values())

    avg = calculate_avg(sales)
    msd = calculate_msd(sales)

    forecast = forecast_next_month(avg, msd)

    forecast_data[model] = sales + [forecast]
    reliability_check[model] = {
        "Прогноз": forecast
    }

df_forecast = pd.DataFrame(forecast_data, index=[f"Месяц {i + 1}" for i in range(13)])

print("\nТаблица прогнозов продаж на 13-й месяц:")
print(df_forecast)

print("\nАнализ достоверности прогнозов:")
for model, data in reliability_check.items():
    print(f"Модель: {model}")
    print(f"  Прогноз: {data['Прогноз']}")


plt.figure(figsize=(14, 8))

df_forecast_T = df_forecast.T

colors = ['blue','orange','green']

df_forecast_T.plot(kind="bar", figsize=(14, 8), color=colors, width=0.8)

plt.title("Продажи диванов по месяцам с прогнозом на 13-й", fontsize=16)
plt.ylabel("Количество продаж", fontsize=14)
plt.xlabel("Модели диванов", fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend([f"Месяц {i + 1}" for i in range(12)] + ["Прогноз (13-й месяц)"], title="Месяцы", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()



