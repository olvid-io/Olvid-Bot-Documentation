# 🦞 OpenClaw

:::{warning}
Cette intégration est encore en cours de développement, et pourrait changer sans préavis.

Pour vos remarques et suggestions, contactez nous par mail [bot@olvid.io](mailto:bot@olvid.io), ou rendez-vous sur notre dépôt GitHub: [openclaw-channel-olvid](https://github.com/olvid-io/openclaw-channel-olvid).   
:::

## Installation
Si vous avez déjà une instance [OpenClaw](https://docs.openclaw.ai/install) fonctionnelle, il suffit d'installer et configurer un daemon, puis d'installer et configurer notre plugin OpenClaw.  
Sinon rendez-vous sur la doc [d'installation d'OpenClaw avec docker](https://docs.openclaw.ai/install/docker).

:::{danger}
Prenez garde en installant et utilisant OpenClaw (et toute IA pouvant executer des commandes et du code). 
Voici nos recommandations minimales en termes de sécurité:
- installer OpenClaw dans un conteneur Docker.
- utiliser uniquement des modèles d'IA hébergés localement (ollama ou autre).
- utiliser le channel Olvid pour sécuriser vos échanges avec votre agent.
- ne pas utiliser de skills vulnérables aux "prompt injections" (c'est-à-dire qui utilisent de la donnée définie par un tiers, comme un mail). 
:::

### Daemon
Voici un fichier `docker-compose.yaml` pour installer un {term}`daemon` Olvid localement. Si OpenClaw est installé avec Docker, ajoutez simplement les services *daemon* et *cli* à votre fichier `docker-compose.yml` existant. 

```{code-block} yaml
  :substitutions:
services:
  daemon:
    image: olvid/bot-daemon:{{docker_version}}
    environment:
      - OLVID_ADMIN_CLIENT_KEY_CLI=SetARandomValue
    ports:
      - 50051:50051
    volumes:
      - ./daemon-data:/daemon/data
  cli:
    image: olvid/bot-python-runner:{{docker_version}}
    entrypoint: "olvid-cli"
    environment:
      - OLVID_ADMIN_CLIENT_KEY=SetARandomValue
      - OLVID_DAEMON_URL=http://daemon:50051
    stdin_open: true
    tty: true
    profiles: ["cli"]
```

Lançons maintenant notre daemon Olvid.
```shell
docker compose up -d daemon
```

On peut ensuite lancer l'invite de commande olvid en mode interactif.
```shell
docker compose run --rm cli
```

Vous pouvez ensuite créer votre bot avec la commande suivante, en suivant la procédure à l'écran.
```
identity new Claw Bot
```

Pour terminer et quitter la CLI Olvid utilisez la commande `exit` ou `ctrl+d`.

### Olvid Channel
On peut ensuite passer à l'installation et la configuration du plugin Olvid dans OpenClaw.
```shell
openclaw plugins install olvid-channel
openclaw plugins enable olvid-channel
openclaw channels add --channel olvid --url DAEMON_URL --token BOT_TOKEN 
```

⚠️ Il faut remplacer *DAEMON_URL* par http://daemon:50051 (ou http://localhost:50051 pour une installation en local) et BOT_TOKEN par la clé client créée auparavant.

C'est bon ! Si tout s'est bien passé les messages que vous envoyez dans Olvid à votre Bot sont transmis à votre agent OpenClaw. 🥳 

:::{note}
Si vous avez perdu votre clé client utilisez la commande suivante.
```shell
docker compose run --rm cli key get -f key
```
:::

## Sécuriser son installation 
[//]: # (TODO )

***Section en cours de rédaction***

- OpenClaw dans Docker: [https://docs.openclaw.ai/install/docker](https://docs.openclaw.ai/install/docker)
- Mise en place d'Ollama: [https://docs.ollama.com/integrations/openclaw#quick-setup](https://docs.ollama.com/integrations/openclaw#quick-setup)
- Installation du channel Olvid: [https://doc.bot.olvid.io/openclaw](https://doc.bot.olvid.io/openclaw)
- Configuration d'OpenClaw

### Configuration d'OpenClaw

Si votre instance OpenClaw est utilisée par plusieurs canaux ou utilisateurs utilisez l'option **per-account-channel** pour le champ *session.dmScope*.  
Cela permet de créer une session par discussion Olvid et de ne pas mélanger les contextes.  

[https://docs.openclaw.ai/gateway/security/index#secure-dm-mode-recommended](https://docs.openclaw.ai/gateway/security/index#secure-dm-mode-recommended)
