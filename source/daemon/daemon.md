# 👹 Daemon

```{toctree}
:hidden:
:maxdepth: 2

self
tutorials
configuration
custom_client
```

# Daemon
Le daemon Olvid est le coeur de notre écosystème de bots. C'est sur lui que tout est basé.
Il s'agit en fait d'un programme qui embarque le moteur cryptographique d'Olvid et un serveur gRPC.
Les différentes méthodes gRPC implémentées permettent d'administrer le daemon et les identités Olvid qu'il contient.

Pour installer votre instance de daemon, rendez-vous dans notre section [](/index).

## Serveur gRPC

On peut distinguer deux types de méthodes (points d'entrée API) que le daemon expose :
- les commandes : un client envoie une requête au daemon qui exécute l'action attendue avant de renvoyer une réponse.
- les notifications : un client s'inscrit pour recevoir un type de notification et le serveur lui enverra un message à chaque fois que nécessaire, tant que la connection reste ouverte.

Toutes les méthodes sont décrites dans le dossier [services](https://github.com/olvid-io/Olvid-Bot-Protobuf/tree/main/olvid/daemon/services/v1) du répertoire GitHub qui contient nos fichiers protobuf.
Les messages de requête et réponse des commandes sont décrits dans le dossier [command](https://github.com/olvid-io/Olvid-Bot-Protobuf/tree/main/olvid/daemon/command/v1).
Les messages de souscription et de notification sont regroupés dans le dossier [notification](https://github.com/olvid-io/Olvid-Bot-Protobuf/tree/main/olvid/daemon/notification/v1).

Enfin, le dossier [datatypes](https://github.com/olvid-io/Olvid-Bot-Protobuf/tree/main/olvid/daemon/datatypes/v1) regroupe un ensemble de messages qui décrivent les objets que le daemon utilise.
Ces messages sont donc utilisés dans de nombreux autres messages.

## Client

Nous avons choisi d'utiliser [protobuf](https://protobuf.dev/) et [gRPC](https://grpc.io/) pour permettre de facilement implémenter des clients capables de se connecter à notre daemon dans n'importe quel langage.

Pour faciliter la prise en main, nous avons déjà développé deux librairies en [python](/python/python) et [javascript](/js/js) qui permettent de commencer à écrire vos clients très rapidement.

Mais si vous préférez utiliser un autre langage, il est possible d'utiliser nos fichiers *.proto* pour générer un client gRPC dans un langage supporté.
Plus d'informations sont disponibles dans notre page [](/daemon/custom_client)
