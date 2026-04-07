# 📋 Exemples

Cette section décrit des exemples de workflows ou d'intégration utilisant nos noeuds communautaires pour n8n.
La documentation pour chacun de ces noeuds est disponible dans les pages associeés: [Olvid](/n8n/olvid) et [Olvid Keycloak](/n8n/keycloak).  

Cette section ne propose pas d'implémentation pour des raisons techniques, mais présente des concepts qui sont facilement réalisables.
Elle a pour but de vous donner une idée de ce qui est réalisable et de stimuler la créativité.

## Olvid

### Chat Bot

Voici un workflow basique pour montrer à quoi peut ressembler une intégration avec Olvid.

Dans ce cas on transfère simplement le contenu du message utilisateur à un modèle Ollama, avant de renvoyer la réponse.
Mais on peut imaginer remplacer le module central par n'importe quel autre service ou flow plus complexe qui traitera une donnée utilisateur, avant de renvoyer le résultat.

```{figure} /_static/images/n8n-examples-chat-bot.png
:alt: Access Control menu tab
:align: center
```


### Validation

Le noeud *Olvid* inclut une action de type *Send and Wait for response* pour ajouter facilement une confirmation humaine dans vos workflows.

Le workflow suivant est une implémentation très basique du traitement d'une requête par un modèle d'AI locale (utilisant ollama). 
Une fois la requête traitée le résultat est envoyé dans Olvid et le flow attend un validation avant de continuer.

Le message de validation peut être envoyé dans la discussion d'origine ou dans une autre discussion.
Cela signifie que l'utilisateur peut valider lui-même l'action, ou un/des utilisateurs autres peuvent valider l'action avant que le flow ne continue.

Valider ou invalider une opération peut se faire de plusieurs manières, mais se résume souvent par le simple ajout d'une réaction 👍 ou 👎 au message de validation.

```{figure} /_static/images/n8n-examples-send-and-wait.png
:alt: Access Control menu tab
:align: center
```

### Sauvegarde de fichiers

La puissance de n8n réside dans son intégration avec de nombreux services. Il est très simple d'ajouter des noeuds vers d'autre des services que vous utilisez.

Le workflow suivant sauvegarde les photos envoyées à votre bot dans un dossier Nextcloud, en respectant une convention de nommage.

```{figure} /_static/images/n8n-examples-upload-file-nextcloud.png
:alt: Access Control menu tab
:align: center
```

## Keycloak
### Création d'utilisateur

Voici un exemple de flow pour faciliter l'intégration de nouveaux utilisateurs à votre annuaire.

Dans cet exemple, on utilise une commande envoyée à un bot dans Olvid, mais le flow pourrait être lancé par n'importe quel autre déclencheur n8n.

On crée un utilisateur dans Keycloak à partir des paramètres de la commande et on peut générer un *magic lien* dans la foulée, pour le renvoyer en réponse.
Pour rejoindre votre annuaire le nouvel utilisateur a juste à ouvrir ce lien dans Olvid ou scaner le QR code affiché dans un navigateur.

On peut aussi ajouter cet utilisateur à un ou des groupes lors de sa création pour qu'il les rejoigne automatiquement dès son arrivée dans l'annuaire.

```{figure} /_static/images/n8n-examples-create-keycloak-user.png
:alt: Access Control menu tab
:align: center
```
