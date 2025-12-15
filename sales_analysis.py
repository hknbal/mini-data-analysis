import pandas as pd

data = {
    "product": ["A", "B", "C", "D"],
    "sales": [150, 200, 300, 180]
}

df = pd.DataFrame(data)

print("Toplam Satış:", df["sales"].sum())
print("Ortalama Satış:", df["sales"].mean())
