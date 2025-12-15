import pandas as pd
import matplotlib.pyplot as plt

data = {
    "product": ["A", "B", "C", "D"],
    "sales": [150, 200, 300, 180]
}

df = pd.DataFrame(data)

df.plot(x="product", y="sales", kind="bar")
plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
