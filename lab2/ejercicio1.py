import matplotlib.pyplot as plt
import pandas as pd

#dataset 1: Ecommerce Dataset for Data Analysis

ecommerce = pd.DataFrame({
    'Categoria': ['Electrónica', 'Ropa', 'Decoración del hogar', 'Libros', 'Deporte', 'Belleza'],
    'Ventas': [15000, 12000, 8000, 9000, 5000, 7000]
})

colores = ["red", "yellow", "blue", "green", "Skyblue", "purple"]
plt.figure(figsize=(12,6))
plt.bar(ecommerce['Categoria'], ecommerce['Ventas'], color=colores)
plt.title('Venta de productos por categoria', fontsize=16)
plt.xlabel('Categoria de productos', fontsize=12)
plt.ylabel('Precio (en USD)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#https://www.kaggle.com/datasets/shrishtimanja/ecommerce-dataset-for-data-analysis
#gracias a esta grafica de barras podemos notas la altas ventas y ganancias que generan las cosas electronicas