import pandas as pd
import matplotlib.pyplot as plt

# Dataset 2: Stock Market Dataset 
stock = pd.DataFrame({
    'Fecha': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Precio': [150, 152, 153, 151, 154, 156, 155, 157, 158, 159]
})

# Gráfico de Líneas
plt.figure(figsize=(10,6))
plt.plot(stock['Fecha'], stock['Precio'], marker='o', color='red', linestyle='--')
plt.title('Precio de las acciones a lo largo del tiempo', fontsize=16)
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Precio (en USD)', fontsize=20)
plt.grid(True)
plt.tight_layout()
plt.show()

#https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

#podemos notar en incremento en el precio de las acciones segun avanzan los meses, gracias a este grafico lineal