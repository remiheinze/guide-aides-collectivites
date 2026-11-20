# Le Guide des Aides aux Collectivités

Site statique en français destiné aux communes et intercommunalités pour explorer les aides publiques et accéder à des tutoriels pratiques.

## Publication GitHub Pages
1. Ouvrir **Settings → Pages**.
2. Dans **Build and deployment**, choisir **GitHub Actions**.
3. Le workflow `.github/workflows/pages.yml` publie automatiquement le site à chaque mise à jour de `main`.
4. L'URL sera affichée dans Settings → Pages.

## Données
Le site tente de lire les dispositifs depuis `https://aides-territoires.beta.gouv.fr/api/aids/?page=1`.
L'API est documentée à l'adresse https://aides-territoires.beta.gouv.fr/api/schema/?version=1.3. Le navigateur doit autoriser les requêtes cross-origin (CORS). Si ce n'est pas le cas, le site affiche un lien vers le portail officiel ; une fonction proxy/cache côté serveur sera à ajouter pour une exploitation fiable.

## À savoir
- Les résultats affichés correspondent à la première page renvoyée par l'API dans ce prototype.
- Les contenus et conditions peuvent évoluer : toujours vérifier auprès du financeur.
- Site indépendant, non affilié à Aides-territoires.
- Vérifier les licences et conditions de réutilisation des champs/contenus de chaque contributeur avant exploitation commerciale.

## Personnalisation
Modifier le titre, les textes et les tutoriels dans `index.html`.
