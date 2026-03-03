import re
import json

# 1. Читаем файл
with open("raw.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

products = []
prices = []
date_time = ""
payment_method = ""

# 2. Проходим по строкам
for line in lines:
    line = line.strip()

    # Ищем дату
    if "Date" in line:
        date_time = line.split(":", 1)[1].strip()

    # Ищем способ оплаты
    elif "Payment" in line:
        payment_method = line.split(":", 1)[1].strip()

    else:
        # Ищем цену (число с точкой)
        match = re.search(r"\d+\.\d{2}", line)
        if match:
            price = float(match.group())
            prices.append(price)

            # Всё до цены — это название продукта
            product_name = line[:match.start()].strip()
            if product_name.lower() != "total":
                products.append(product_name)

# 3. Считаем сумму
total_amount = sum(prices)

# 4. Создаём структуру
result = {
    "products": products,
    "prices": prices,
    "total": total_amount,
    "date": date_time,
    "payment_method": payment_method
}

# 5. Красиво выводим
print(json.dumps(result, indent=4))