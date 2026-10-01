# ⚙️ Installation
## Prérequis
### Dépendances
Avant de démarrer, assurez-vous d'avoir installé :
- **Docker Desktop**, ou Docker Engine + Compose v2.

Optionnel :
- Application Olvid (desktop ou mobile) pour rentrer en contact avec le bot
- Serveur SMTP disponible pour configurer les envois par e-mail.

### Télécharger le code
Clonez le dépot GitHub du projet :
```bash
git clone https://github.com/olvid-io/olvid-alerting-bot.git
cd olvid-alerting-bot
```

## Configuration
### Préparer le fichier `.env`
Copiez le fichier `.env.example` en `.env`, que vous compléterez au fil de l'installation ;
```bash
cp .env.example .env
```

### Créer l'identité Olvid
Pour mettre en place l'identité Olvid que le bot utilisera pour envoyer les messages
via Olvid, suivez les instructions du [Quickstart](/index).

### Générer les clés secrètes
L'application utilise trois chaînes de caractères aléatoires pour garantir la sécurité de l'application :
- Signature des cookies de connexion
- Clé pour la phase de setup (pour la création du premier compte administrateur)
- Clé admin du démon Olvid

Chacune de ces clés peut être générée grâce à la commande suivante :
```bash
openssl rand -base64 32
```
Puis, insérez les clés dans le fichier `.env` :
```
NUXT_SESSION_PASSWORD=...
ADMIN_KEY=...
OLVID_ADMIN_CLIENT_KEY=...
```

### Configuration du serveur mail (optionnel)
Pour utiliser les fonctionnalités e-mail de l'application (canal de sortie des alertes, invitation
et réinitialisation de mot de passe par mail), configurez les variables d'environnement 
du serveur SMTP.
```bash
SMTP_HOST=mail-server-hostname
SMTP_PORT=mail-server-port
SMTP_USER=mail-server-username
SMTP_PASSWORD=mail-server-password
SMTP_FROM=Alerting Bot <noreply-alert@yourdomain.com> # L'adresse mail peut être changée
```

### Build et déploiement
```bash
docker compose build app
```
Une fois le build terminé, le conteneur Docker est prêt à l'emploi. Vous pouvez désormais 
démarrer l'application avec la commande suivante :
```bash
docker compose up -d app
```
Pour utiliser les fonctionnalités Olvid de l'application, assurez-vous que le démon est
lancé. Si ce n'est pas le cas, vous pouvez le démarrer avec `docker compose up -d daemon`.
Si le démon est hors-ligne au lancement de l'application ou est éteint durant l'exécution, 
l'application tentera périodiquement de se reconnecter (le délai est configurable via
la variable d'environnement `UPDATER_TRY_AGAIN_DELAY`, la valeur par défaut étant 2000 ms).

## Créer le premier compte administrateur
Au démarrage, Olvid Alerting ne comporte aucun utilisateur :
- Ouvrez l'application : vous arriverez sur `/setup`
- Collez la clé `ADMIN_KEY` créée lors de la [génération des secrets](#générer-les-clés-secrètes).
Cela prouve que vous êtes bien à l'origine de la mise en place de l'application.
- Choisissez un canal (Olvid / Mail / Lien) et entrez un nom d'utilisateur pour recevoir un
lien d'activation de compte. 
- Utilisez le lien pour accéder au choix des méthodes d'authentification.

Les utilisateurs suivants seront ajoutés par un administrateur via la page `/users` 
(voir [Inviter des utilisateurs](/alerting-bot/guideline)).

