# 🐍 Client Python

```{toctree}
:maxdepth: 2
:hidden:

🛠️ Installation<self>
tutorials
examples
troubleshooting
```

:::{admonition} Pré-requis
:class: note

Si vous n'avez pas installé de {term}`daemon`, merci de suivre la section [](/index).

Avant de commencer, vérifiez bien que vous avez une instance du daemon Olvid qui tourne, avec
une {term}`identité` créée dessus, et une {term}`clé client` valide pour vous connecter en utilisant cette identité.

Si vous souhaitez vérifier que votre daemon est fonctionnel et/ou récupérer une clé client perdue, utilisez la commande : `docker compose run --rm cli key get`
:::

## Installation
Nous avons développé une librairie Python qui permet d'interagir facilement avec votre daemon.
Elle est disponible à l'installation avec la commande `pip`.

```shell
pip3 install olvid-bot
```

:::{tip}
Le module `olvid-bot` nécessite une version de Python supérieure ou égale à 3.10.
Sur Mac OS, nous vous conseillons d'utiliser HomeBrew pour installer une version plus récente.
```shell
brew install python3
```
:::

## Configuration
Pour se connecter à un daemon, votre programme a besoin de connaitre l'adresse du daemon et la clé client à utiliser.
Pour cela, on utilise des variables d'environnement ou un fichier *.env*.

Remplacez la clé client par celle que vous avez créée lors de la mise en place de votre daemon, et l'adresse du daemon si nécessaire.

```shell
echo OLVID_DAEMON_URL=http://localhost:50051 > .env
echo OLVID_CLIENT_KEY=ReplaceWithYourClientKey >> .env
```

## Premier programme
Afin de vérifier que tout fonctionne correctement, vous pouvez copier/coller ce programme dans un fichier `main.py`.

```python
import asyncio
from olvid import OlvidClient

async def main():
    client = OlvidClient()
    print((await client.identity_get()).display_name)

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

Vous pouvez ensuite l'exécuter à l'aide de l'interpréteur Python.
```shell
python3 main.py
```

Si tout a bien été configuré, vous devriez voir s'afficher le nom d'usage de l'identité que vous avez créée sur le daemon.

Sinon, rendez-vous dans notre section [](/python/troubleshooting).

## Premier Bot

Pour commencer à coder votre premier bot, vous pouvez partir de l'exemple suivant.
Il se contente de répondre à chaque message avec le même message, mais il peut facilement être modifié et amélioré.

```python
import asyncio
from olvid import OlvidClient, datatypes, tools

class EchoBot(OlvidClient):
    async def on_message_received(self, message: datatypes.Message):
        await message.reply(client=self, body=message.body)

    async def on_discussion_new(self, discussion: datatypes.Discussion):
        await discussion.post_message(client=self, body="Hello 👋")

async def main():
    bot = EchoBot()
    await bot.enable_auto_invitation(accept_all=True)  # automatically accept presentation and group invitations
    await bot.run_forever()

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

## Et maintenant ?

Pour en apprendre plus sur l'utilisation de notre librairie Python rendez-vous dans notre section [](/python/tutorials).
Sinon rendez-vous dans la section [](/python/examples) pour déployer des projets clés en main.
