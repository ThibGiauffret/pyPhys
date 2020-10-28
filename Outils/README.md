<h1>Outils pour la Physique-Chimie</h1>
<h2>Programme de régression linéaire simple avec Python</h2>

<p align="center">
    <img src="https://www.ensciences.fr/git/images/py_regression.png" alt="Illustration de la régression" width="400">
</p>

<h3>Principe de fonctionnement</h3>

<p>Les données sont entrées dans un fichier <em>data.csv</em>. Le script extrait les données (on précise le caractère qui sépare les colonnes). Ces données sont ensuite traitées pour calculer les paramètres de la régression.</p>

<p>Le principe se base principalement sur la fonction <em>stats.linegress</em> de <em>scipy</em>. Les valeurs retournées sont la pente, l'ordonnée à l'origine et le coefficient de corrélation.</p>

<p>Le tracé des points expérimentaux est effectué et superposé avec la régression. Les paramètres de régression sont affichés.</p>

<h3>Prise en main</h3>

- Entrer les données dans le fichier <em>data.csv</em>.
- Entrer les incertitudes associées pour tracer les barres d'erreurs.
- Au besoin, modifier les noms des axes et le titre.
