# 🚨 Olvid Alerting

**Olvid Alerting** est un bot qui surveille des sources distantes pour envoyer des 
alertes via Olvid ou mail. Il se présente sous la forme d'une application web
Nuxt auto-hébergée qui permet la configuration simple des alertes et s'occupe 
d'envoyer les messages à travers une identité bot Olvid et/ou un serveur SMTP.

Olvid Alerting supporte actuellement 3 sources :
- Polling XML / JSON : Récupère périodiquement des données XML ou JSON, les lit
et envoie une alerte lorsque certains critères sont respectés (une valeur surveillée
change, un seuil est dépassé...)
- Monitoring : Effectue périodiquement une requête HTTP sur une URL donnée et envoie
une alerte en fonction de la réponse (code spécifique, plage de codes, pas de réponse
du serveur...)
- Webhook : Expose une URL Webhook pour permettre à des applications tierces comme 
GitHub, Grafana ou Sentry de déclencher une alerte via une requête POST.

Olvid Alerting intègre aussi une méthode d'authentification par Olvid sans mot de passe,
en ajoutant une réaction à un message envoyé par le bot sur la discussion associée
à l'utilisateur Olvid Alerting.

## Architecture
Le bot utilise Docker Compose pour créer deux conteneurs :
- **daemon** : Le [démon Olvid](/daemon/daemon) utilisé pour envoyer des messages et
communiquer avec les utilisateurs via Olvid. Pour plus de détails sur le fonctionnement
du démon, voir [Quickstart](/index).
- **app** : Une application Nuxt intégrant une interface Web pour la configuration des alertes
et une partie serveur communiquant avec le démon et stockant les données dans une base de données
SQLite.

Le bot peut être déployé dans un réseau interne, mais pour permettre l'usage des Webhooks,
il est préférable d'utiliser un reverse proxy pour rediriger les requêtes externes vers l'application.
Par défaut, Docker publie sur le port `:3000`.

Pour démarrer l'installation, voir [Installation](/alerting-bot/installation).

## Fonctionnalités
- Création d'alertes Polling, Monitoring ou Webhook et configuration de l'intervalle
de récupération et des conditions de déclenchement.
- Éditeur de script pour créer des messages dynamiques en utilisant le Markdown Olvid
ou HTML pour les mails.
- Envoi de messages dans des discussions Olvid 1-to-1 ou de groupe, et envoi de mails.
- Gestion des utilisateurs avec plusieurs profils.
- Authentification sécurisée via Olvid