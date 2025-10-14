import pandas as pd
import matplotlib.pyplot as plt

# Lecture du fichier CSV
data = pd.read_csv('data.csv')
theta = pd.read_csv('model.csv')

mu = sum(data['km']) / len(data['km'])
sigma = (sum((data['km'] - mu) **2) / len(data['km']))**0.5


data['approx'] = theta['theta0'].iloc[-1] + ((data['km'] - mu) / sigma) * theta['theta1'].iloc[-1]

print(data)

plt.scatter(data['km'], data['price'], color="green")      # Crée le graphique
plt.xlim(left=0)    # Affiche le zéro sur l'axe des x
plt.ylim(bottom=0)  # Affiche le zéro sur l'axe des y
plt.xlabel('km')
plt.ylabel('price')

plt.plot(data['km'], data['approx'], color="red")

plt.show()          # Ouvre la fenêtre et affiche le graphique
