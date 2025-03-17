import xml.etree.ElementTree as ET
import json
import random
import matplotlib.pyplot as plt
import pandas as pd

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

df = pd.DataFrame({sofa["model"]: sofa["sales"].values() for sofa in sofas},
                  index=[f"Месяц {i + 1}" for i in range(12)])

df.plot(kind="bar", figsize=(12, 6), title="Продажи диванов по месяцам")
plt.xlabel("Месяцы")
plt.ylabel("Количество продаж")
plt.legend(title="Модели диванов")
plt.xticks(rotation=45)
plt.show()

print(df)
