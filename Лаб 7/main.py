import xml.etree.ElementTree as ET
import random
import json
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np
from IPython.display import display

def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    sofas_data = []
    offers = root.find('shop').find('offers')
    for offer in offers.findall('offer'):
        name = offer.find('name').text
        price = int(offer.find('price').text)
        description = offer.find('description').text if offer.find('description') is not None else "Нет описания"
        sofas_data.append({"model": name, "price": price, "description": description})

    return sofas_data

def generate_sales_data(sofas_data):
    for sofa in sofas_data:
        sales = [int(50 + 30 * np.sin(2 * np.pi * i / 12) + random.randint(-5, 5)) for i in range(12)]
        sofa["sales"] = sales
    return sofas_data

def write_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def predict_future_sales(sales_data):
    predictions = []
    degree = 2
    for data in sales_data:
        X = np.array(range(1, 13)).reshape(-1, 1)
        y = np.array(data['sales'])

        seasonal_component = np.sin(2 * np.pi * X.flatten() / 12).reshape(-1, 1)
        X_with_seasonality = np.hstack([X, seasonal_component])

        poly = PolynomialFeatures(degree=degree)
        X_poly = poly.fit_transform(X_with_seasonality)

        model = LinearRegression()
        model.fit(X_poly, y)

        future_X = np.array([[13, np.sin(2 * np.pi * 13 / 12)]])
        future_X_poly = poly.transform(future_X)
        future_sales = max(0, round(model.predict(future_X_poly)[0]))

        y_pred = model.predict(X_poly)
        rmse = np.sqrt(mean_squared_error(y, y_pred))
        mae = mean_absolute_error(y, y_pred)

        data['predicted_sales'] = future_sales
        data['rmse'] = rmse
        data['mae'] = mae
        predictions.append(data)
    return predictions

def display_table(data):
    rows = []
    for sofa in data:
        row = {
            "Модель": sofa["model"],
            "Цена": sofa["price"],
            **{f"Месяц_{i + 1}": sale for i, sale in enumerate(sofa["sales"])},
            "Прогноз": sofa["predicted_sales"],
            "RMSE": sofa["rmse"],
            "MAE": sofa["mae"]
        }
        rows.append(row)
    df = pd.DataFrame(rows)
    display(df)

def main():
    xml_file = 'sofas.xml'
    json_file = 'sales.json'

    sofas_data = read_xml(xml_file)

    if not sofas_data:
        print("Ошибка: XML-файл пустой или содержит некорректные данные.")
        return

    sales_data = generate_sales_data(sofas_data)

    write_json(json_file, sales_data)

    predicted_data = predict_future_sales(sales_data)

    print("   Отображение таблицы данных   ")
    display_table(predicted_data)

if __name__ == "__main__":
    main()