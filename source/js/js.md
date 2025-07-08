# {fab}`js;js-logo-color` Client JavaScript

```{toctree}
:maxdepth: 2
:hidden:

🛠️ Installation<self>
advanced
browser
```

:::{admonition} Pré-requis
:class: note

Si vous n'avez pas installé de {term}`daemon`, merci de suivre la section [](/index).

Avant de commencer, vérifiez bien que vous avez une instance du daemon Olvid qui tourne, avec
une {term}`identité` créée dessus, et une {term}`clé client` valide pour vous connecter en utilisant cette identité.

Si vous souhaitez vérifier que votre daemon est fonctionnel et/ou récupérer une clé client perdue, utilisez la commande : `docker compose run --rm cli key get`
:::

Nous avons développé un module Node.js en typescript pour facilement créer des programmes qui intéragissent avec un daemon Olvid.

Voici la procédure de mise en place d'un programme de démonstration qui se connecte à votre instance de daemon et implémente les bases d'un chat bot.

## Installation
Créons tout d'abord notre répertoire de travail. 

```shell
mkdir -p olvid-bot
cd olvid-bot
```

On peut maintenant mettre en place le projet.
```shell
npm init -y
npm install @olvid/bot-node
mkdir -p src
touch .env src/main.ts
npm pkg set scripts.main="npx tsx src/main.ts"
```

## Configuration
Pour se connecter à un daemon, votre programme a besoin de connaitre l'adresse du daemon et la clé client à utiliser.
Pour cela, on utilise des variables d'environnement ou un fichier *.env*.

Remplacez la clé client par celle que vous avez créée lors de la mise en place de votre daemon, et l'adresse du daemon si nécessaire.
```shell
echo OLVID_DAEMON_TARGET=localhost:50051 > .env
echo OLVID_CLIENT_KEY=ReplaceWithYourClientKey >> .env
```

## Premier programme

Vous pouvez maintenant copier/coller le code suivant dans le fichier **src/main.ts**.

Le programme va afficher l'identité avec laquelle vous êtes connecté au daemon puis attendre que des messages arrivent.
Pour le moment il ne répond qu'à la commande *!ping* mais vous pouvez modifier le code pour adapter son comportement.

```typescript
import {OlvidClient, datatypes} from "@olvid/bot-node";
import {command, onMessageReceived, onMessageSent} from "@olvid/bot-node";

class ExampleBot extends OlvidClient {
    @command("^!ping")
    async help(message: datatypes.Message) {
        await message.reply(this, "pong")
    }
    
    @onMessageReceived()
    async messageReceived(message: datatypes.Message) {
        console.log("<", message.body);
    }
    @onMessageSent()
    async messageSent(message: datatypes.Message) {
        console.log(">", message.body);
    }
}

async function main() {
  let bot = new ExampleBot();
  console.log("Started bot as:", (await bot.identityGet()).displayName)
  await bot.runForever();
}
main().then()
```

Lancez votre programme à l'aide la commande suivante. (`CTRL+C` pour l'interrompre).
```shell
npm run main
```

% TODO enable
% (En cas de soucis n'hésitez pas à consulter notre section []&#40;/js/troubleshooting&#41;.)

Lorsque tout fonctionne vous pouvez utiliser ce programme comme base pour votre projet en le modifiant.

% TODO enable
% (Pour aller plus loin rendez-vous dans notre section []&#40;/js/advanced&#41;)
