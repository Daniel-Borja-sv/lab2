import pandas as pd
import matplotlib.pyplot as plt

# Dataset 3: Pokemon Dataset 
pokemon= pd.DataFrame({
    'Tipo': ['Water', 'Fire', 'Grass', 'Electric', 'Rock', 'Psychic', 'Dragon'],
    'Numero': [100, 80, 90, 60, 50, 40, 30]
})



# Gráfico Circular
colores = ['blue', 'red', 'green', 'yellow', 'gray', 'purple', 'orange']
plt.figure(figsize=(10,6))
plt.pie(pokemon['Numero'], labels=pokemon['Tipo'], autopct='%1.1f%%', 
        startangle=140, colors=colores)
plt.title('Tipos de pokemon', fontsize=16)
plt.tight_layout()
plt.show()

#https://www.kaggle.com/datasets/christofferms/pokemon-with-stats-and-image

#aqui vemos las estadisticas de los pokemos y el porcentaje de uso gracias a esta grafica de pastel