# 🏁 Utilisation

:::{important} Dans les exemples de commandes en mode script, *olvid-cli* peut être remplacé par n'importe quel moyen de lancer la CLI (docker ou python).
:::

:::{contents} Contenu
:local:
:depth: 2
:::

## Principe
La CLI Olvid implémente un certain nombre de commandes subdivisées en groupes de commandes.

Par exemple, le groupe de commande **identity** rassemble un ensemble de commandes qui permettent de gérer les identités présentes sur le daemon.
Parmi elles, les commandes **new**, **get** et **rm** qui permettent respectivement de créer, lister et supprimer les identités.

Voici des exemples de commandes valides :
```shell
identity new FirstName LastName
identity get
identity rm 1
```

A tout moment, vous pouvez obtenir la liste des groupes, des commandes et les usages associés en ajoutant `--help` à la fin de votre commande (même incomplète).

```shell
# list available command groups
--help
# list commands related to identties 
identity --help
# show identity new command usage
identity new --help
```

## Mode interactif / Mode script
En lançant la CLI sans passer d'argument, par défaut elle se lance en mode interactif.

Il est également possible d'exécuter une commande directement en la passant en argument. Par exemple :
```shell
olvid-cli identity get
```
Exécutera la commande *identity get* puis s'arrêtera automatiquement. C'est ce que l'on appellera le mode script pour la suite des exemples.

## Identité courante
La plupart des commandes de la CLI nécessitent de spécifier une identité à utiliser. Par exemple, lister les discussions ou envoyer un message doit être fait "en tant que" telle identité.

Pour cela, on va utiliser l'identifiant de l'identité en question (un nombre). La manière de passer cet identifiant varie en fonction du mode de fonctionnement actuel de la CLI.

:::{dropdown} Mode interactif
:open:

En mode interactif, la CLI sélectionne automatiquement, au lancement, la première identité disponible.
Elle affiche l'identité utilisée dans le prompt.

Il est cependant possible de changer l'identité utilisée à l'aide de la commande suivante.

```shell
# change current identity to 2
1 > identity current 2
# show current identity
2 > identity current
```
:::

:::{dropdown} Mode script
:open:

En mode script, si la commande le nécessite, on utilisera l'option *-i* pour spécifier l'identité à utiliser.
Par exemple, pour lister les messages de l'identité 1.

```shell
olvid-cli -i 1 message get 
```
:::{hint} l'option *-i* doit impérativement se trouver avant le debut de la commande, ici avant *message get*.
:::

## Lister des éléments
Tous les groupes de commandes liés à une entité (identité, discussion, message, ...) implémentent la commande `get` qui permet de lister les éléments associés.

Pour n'afficher que certains champs des entités, il est possible d'utiliser l'option *-f* ou *--fields* suivie d'une liste de nom de champs de l'entité en question séparée par des virgules.

Chaque commande `get` peut également implémenter ses spécificités, nous vous invitons donc à vérifier les options et arguments supplémentaires qu'elle pourrait implémenter à l'aide de l'option *--help*.

Voici quelques exemples de commandes liées à la liste des éléments :

```shell
# Show display name for every identity
1> identity get --fields display_name
# List id and body of 1st identity messages
1 > message get --fields id,body
```

## Gestion des clés client
Le groupe de commandes `key` permet de gérer les clés clients du daemon. Il ne nécessite pas d'identité courante puisque les clés clients sont globales.

Une clé client est soit associée à une identité, c'est le cas des clés client utilisées pour nos programmes, soit elle est administratrice, elle peut choisir quelle identité elle veut utiliser à chaque appel API.
C'est le cas de la clé client utilisée par la CLI.

Les clés client ont un nom associé.
Il n'est pas utilisé et a juste pour but d'aider à les gérer.

Voici des exemples de commandes liées à la gestion des clés clients :

```shell
# List client keys
key get 
# Create admin client key
key new key-name 0
# Create client key for identity 1
key new my-client-key 1
# Delete a client key (we pass the key, not it's name)
key rm 00000000-0000-0000-0000-000000000000
```

## Stockage
L'API de stockage du daemon permet de stocker des données arbitraires sous forme de clés-valeurs dans la base de données du daemon.

Ces éléments sont tous associés à une clé client non-administrateur.
Cela permet à la fois de scinder le stockage par client et de restaurer correctement les éléments stockés en cas de restauration de sauvegarde.

Pour accéder aux éléments de stockage à l'aide de la CLI, il faut donc spécifier la clé client à utiliser.

:::{dropdown} Mode interactif
:open:
```shell
# We specify that, from now, we want to use a different client key than the admin client key 
1 > key impersonate 00000000-0000-0000-0000-000000000000
# Now we can use storage api for this client key 
1 > storage get 
```
:::

:::{dropdown} Mode script
:open:
En mode script, on utilise l'option *-k* de manière similaire à l'option *-i*.
```shell
olvid-cli -k 00000000-0000-0000-0000-000000000000 storage get
```
:::

Le stockage du daemon contient deux types de stockage : un stockage global et un stockage par discussion. Dans le second cas, il est possible de stocker dans plusieurs discussions plusieurs valeurs pour une même clé.

Le stockage du daemon présente deux intérêts majeurs :

* simplicité d'usage et de déploiement : pas besoin de mettre en place un système de stockage côté client.
* résilience aux sauvegardes : le stockage du daemon est sauvegardé en utilisant le même mécanisme que le reste des données du daemon. Cela assure plus de robustesse, mais surtout il permet d'être résilient aux changements d'identifiants qui ont lieu lors d'une restauration de sauvegarde.

% todo ajouter un lien vers la documentation de l'API de stockage, il y aura peut-être du ménage à faire ici pour éviter les doublons.
