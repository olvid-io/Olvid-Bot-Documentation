# 👹 Daemon

```{toctree}
:hidden:
:maxdepth: 2

self
tutorials
options
custom_client
```

# Daemon
Le daemon Olvid est le coeur de notre écosystème de bots. C'est sur lui que tout est basé.
C'est un programme qui embarque le moteur cryptographique d'Olvid et un serveur gRPC.
Les différentes méthodes gRPC implémentées permettent d'administrer le daemon et les identités Olvid qu'il contient.

Pour installer votre instance de daemon, rendez-vous dans notre section [](/index).

## Serveur gRPC

On peut distinguer deux types de méthodes (points d'entrée API) que le daemon expose :
- les [commandes](/reference/commands) : un client envoie une requête au daemon qui exécute l'action attendue avant de renvoyer une réponse.
- les [notifications](/reference/notifications) : un client s'inscrit pour recevoir un type de notification et le serveur lui enverra un message à chaque fois que nécessaire, tant que la connection reste ouverte.

Toutes les méthodes sont décrites dans la page [](/reference/reference).

Enfin, la page [](/reference/datatypes) décrit les structures de donnée de base utilisées par le daemon.

## Client

Nous avons choisi d'utiliser [protobuf](https://protobuf.dev/) et [gRPC](https://grpc.io/) pour permettre de facilement implémenter des clients capables de se connecter à notre daemon dans n'importe quel langage.

Pour faciliter la prise en main, nous avons déjà développé deux librairies en [python](/python/python) et [javascript](/js/js) qui permettent de commencer à écrire vos clients très rapidement.

Nous avons également développé des intégrations clé en main pour [](/n8n/n8n) et [](/openclaw/openclaw).

Si vous préférez utiliser un autre langage que ceux déjà supportés, il est possible d'utiliser les fichiers proto de description de notre api, disponibles sur notre repo [GitHub](https://github.com/olvid-io/Olvid-Bot-Protobuf).
Plus d'informations sont disponibles dans notre page [](/daemon/custom_client)
