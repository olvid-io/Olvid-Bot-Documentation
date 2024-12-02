# 👩‍🔧 Dépannage

## Erreurs courantes
:::{contents}
:local: true
:depth: 3
:::

### **Cannot connect to server**
:::{card} 
La CLI n'a pas réussi à se connecter au daemon. Vérifiez que l'adresse du daemon est valide et que le port 50051 est exposé.

Pour cela, vérifiez la présence des lignes suivantes dans le service *daemon* du fichier *docker-compose.yaml* de votre daemon.
```yaml
  ports:
  - 50051:50051
```
En cas d'absence, ajoutez-les et appliquez la nouvelle configuration avant de relancer la CLI.
```shell
docker compose up -d daemon
```
:::

### **Invalid client key**
:::{card}
Deux causes possibles pour ce message d'erreur. La CLI n'a pas pu accéder à la clé admin, ou celle-ci n'est pas la bonne.

Dans votre fichier *docker-compose.yaml*, vérifiez la présence d'une variable d'environnement qui commence par *OLVID_ADMIN_CLIENT_KEY*.

Copiez sa valeur et utilisez-la comme valeur de la variable d'environnement *OLVID_ADMIN_CLIENT_KEY* dans la section [précédente](/cli/cli).

Pour plus de détails sur les clés d'administration du daemon, rendez-vous [ici](/daemon/daemon).
% TODO remplacez par un lien vers la configuration des clés admin dans le daemon.
:::

### **Command not found: olvid-cli**
:::{card}
Le binaire `olvid-cli` n'a pas été ajouté dans votre *PATH*. Utilisez plutôt Python ou Docker pour lancer la CLI (cf [](/cli/cli)).

```shell
python3 -m olvid-bot
```
:::
