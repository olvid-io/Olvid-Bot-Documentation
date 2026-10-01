# 🧐 FAQ

**Ai-je besoin d'Olvid et du SMTP ?**
Non. Olvid fonctionne seul. Le SMTP fonctionne seul. Configurez le ou les canaux de votre 
choix selon votre cas d'usage.

**Une alerte peut-elle être envoyée via Olvid ET via mail ?**
Oui. Un *bundle* n'est associé qu'à un unique canal, mais une alerte peut comporter
plusieurs bundles. Ajoutez un bundle Olvid pour vos destinataires Olvid et un
bundle Mail pour votre mailing list, tous deux sur une même alerte.

**Que se passe-t-il lorsque le démon est hors ligne quand l'alerte est déclenchée ?**
L'envoi est marqué comme `Échec` dans le journal avec l'indication d'une erreur du démon.
L'alerte sera redéclenchée lors du prochain cycle pour les alertes Polling et Monitoring.

**L'application fonctionne-t-elle si le démon est déconnecté ?** 
Oui, mais toutes les fonctionnalités utilisant Olvid seront indisponibles (envoi de messages,
authentification par Olvid). Un indicateur dans le coin supérieur gauche affiche 
l'état actuel du démon. S'il est déconnecté ou n'était pas actif au démarrage de l'app,
cette dernière tente périodiquement de se reconnecter.

**Où sont stockées mes données ?**
SQLite, dans le volume Docker `alerting-db` (`docker compose down -v` permet de 
réinitialiser la base de données). L'état du démon est stocké dans le dossier monté
`./data`.

**Comment puis-je réinitialiser l'application ?**
`docker compose down -v` (supprime la base de données) + `rm -rf ./data/*` (supprime
l'état du démon). Au redémarrage, la phase de configuration initiale sera de nouveau activée.
