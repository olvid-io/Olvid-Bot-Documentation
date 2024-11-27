# 🌱 Exemples

Dans cette page, nous vous proposons des exemples de projets qui ont été réalisés à l'aide du module Python *olvid-bot*.
Leur code est accessible et modifiable pour correspondre à vos besoins.

:::{contents}
:local:
:depth: 1
:::

## 🤖 Chat Bot

Un exemple simple et modifiable qui permet de découvrir l'univers des bots Olvid.

On va mettre en place un système de commandes. Le bot attend des messages spécifiques commençant par le caractère *!*.
Chaque commande déclenche une action et/ou une réponse différente.

Vous pouvez utiliser ou modifier notre [Chat Bot](https://github.com/olvid-io/Olvid-Bot-Documentation/tree/main/examples/chat-bot) d'exemple.


## {octicon}`webhook;1em;sd-text-primary` Serveur Webhook

Le cas d'usage que nous avons rencontré le plus souvent lors de la mise en place de bots Olvid ce sont les bots d'alerte.
Une des manières les plus simples et universelles de faire cela c'est d'utiliser un système de [webhook](https://fr.wikipedia.org/wiki/Webhook).

On va retrouver beaucoup de systèmes différents pour gérer et paramétrer nos webhooks, en voici quelques une.

### {octicon}`broadcast;1em;sd-text-primary` Bot de diffusion

Le cas le plus simple, c'est ce que nous appelons un bot de diffusion.
Il écoute sur une URL donnée, et lorsqu'il reçoit une alerte, il envoie un message à tous ses contacts et dans tous ses groupes.

Le code de notre bot de diffusion est accessible ici : [Broadcast Bot](https://github.com/olvid-io/Olvid-Bot-Documentation/tree/main/examples/broadcast-bot).

Sa simplicité permet d'avoir un code très court et c'est un très bon exemple pour débuter.

### {octicon}`webhook;1em;sd-text-primary` Webhook par discussion

Dans certains cas de figure, on voudra plutôt avoir une URL de webhook qui permet de poster un message dans une discussion donnée.
Dans ce cas, il faut créer puis stocker pour chaque discussion une URL unique.
Lorsque cette URL est appelée, on envoie le message dans la discussion associée.

C'est ce type de modèle qui est utilisé dans la messagerie Slack par exemple.

Le code est disponible ici : [Webhook Bot](https://github.com/olvid-io/Olvid-Bot-Documentation/tree/main/examples/webhook-bot).
