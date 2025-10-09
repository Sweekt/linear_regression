import pandas as pd
import matplotlib.pyplot as plt

# Lecture du fichier CSV
data = pd.read_csv('data.csv')
data_sort = data.sort_values(by=['km'])
data_sort['approx'] = data_sort['km'] / 30

plt.scatter(data_sort['km'], data_sort['price'], color="green")      # Crée le graphique
plt.xlim(left=0)    # Affiche le zéro sur l'axe des x
plt.ylim(bottom=0)  # Affiche le zéro sur l'axe des y
plt.xlabel('km')
plt.ylabel('price')

plt.plot(data_sort['km'], data_sort['approx'], color="red")

plt.show()          # Ouvre la fenêtre et affiche le graphique