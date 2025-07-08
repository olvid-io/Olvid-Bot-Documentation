# 👩‍🏫 Tutoriels

Dans cette page, nous essayons d'expliquer comment réaliser un certain nombre d'actions avec notre librairie Python.
Idéalement, il vaut mieux la suivre étape par étape afin de suivre le cheminement, mais si vous vous sentez à l'aise, vous pouvez essayer d'accéder directement à la section qui vous intéresse.

:::{contents}
:local:
:depth: 2
:::

## Les bases

### OlvidClient
Pour interagir avec le {term}`daemon`, il vous faudra systématiquement créer une instance de la classe **OlvidClient**.
Il peut s'agir de la classe d'origine ou d'une classe enfant.

Cette classe va automatiquement récupérer une clé client en utilisant l'environnement ou un fichier `.env`. (cf. [](/python/python.md#configuration))

Grâce à ce client, on pourra notamment exécuter des commandes et mettre en place des listeners de notifications.

Voici à quoi ressemble un fichier *main.py* de base contenant la création d'un client Olvid et l'exécution d'une commande (afficher l'identité courante).
Cette structure est à utiliser dans chacun des exemples de code de cette page, il suffit de remplacer le contenu de la fonction `main` par le code de votre choix.

```python
import asyncio
from olvid import OlvidClient, datatypes

async def main():
    client = OlvidClient()
    
    # code to replace
    print(await client.identity_get())

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

### Commande
Toutes les méthodes gRPC de commandes exposées par le daemon sont facilement accessibles grâce à des méthodes de la classe **OlvidClient**.
Par exemple, pour envoyer un message (méthode `MessageSend` en gRPC), on utilisera la méthode `message_send` de notre instance d'OlvidClient.

Dans le cas où nous connaissons l'identifiant de la discussion dans laquelle poster, cela donnerait :
```python
from olvid import OlvidClient

client = OlvidClient()
client.message_send(discussion_id=1, body="Use Olvid !")
```

### Notification
La classe **OlvidClient** implémente également des méthodes qui permettent de facilement écouter les notifications émises par le daemon.
Ces méthodes commencent toutes par le préfixe `on_` et doivent être redéfinies dans une classe fille d'OlvidClient.

Par exemple, pour afficher dans le terminal quand un message est reçu et lorsqu'une réaction est ajoutée, on peut faire :
```python
import asyncio
from olvid import OlvidClient, datatypes

class Bot(OlvidClient):
    async def on_message_received(self, message: datatypes.Message):
        print(f"Message received: {message.body}")

    async def on_message_reaction_added(self, message: datatypes.Message, reaction: datatypes.MessageReaction):
        print(f"Reaction added: {reaction.reaction}")

async def main():
    bot = Bot()
    await bot.run_forever()

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

## Conseils et astuces
### AutoInvitationBot
Pour rendre plus facile la mise en relation avec un bot, il est possible de mettre en place un autre bot, déjà écrit, qui acceptera toutes les invitations reçues.

Il suffit de créer un bot *AutoInvitationBot* du module `olvid.tools`. Il va automatiquement s'enregistrer pour recevoir les notifications de nouvelles invitations et les accepter.

:::{note}
Un *AutoInvitationBot* ne peut accepter que les présentations et les invitations de groupe. 
Il ne peut pas accepter automatiquement les invitations directes avec échange de SAS code. 
:::

Voici un programme qui lance une instance de l'AutoInvitationBot en tâche de fond.
Il est tout à fait possible de lancer plusieurs bots en parallèle.

```python
import asyncio
from olvid import OlvidClient, datatypes, tools

class Bot(OlvidClient):
    async def on_message_received(self, message: datatypes.Message):
        print(f"Message received: {message.body}")

async def main():
    bot = Bot()
    tools.AutoInvitationBot()
    await bot.run_forever()

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

## Divers
### Envoyer un message éphémère
Les points d'entrée API `messageSend` et `messageSendWithAttachments` permettent de spécifier l'éphéméralité du message à envoyer.
On utilisera pour cela l'objet *olvid.datatypes.MessageEphemerality*.

Voici un exemple en python. Il est possible de spécifier les paramètres `read_once`, `visibility_duration` et `existence_duration` de manière indépendante.
Les durées d'existence et de visibilité sont en secondes.

```python
import asyncio

from olvid import datatypes, OlvidClient

async def main():
    client = OlvidClient()
    async for discussion in client.discussion_list():
        await client.message_send(
            discussion_id=discussion.id,
            body="Self-destruct message",
            ephemerality=datatypes.MessageEphemerality(
                visibility_duration=10,
                existence_duration=60,
                read_once=True
            )
        )

asyncio.run(main())
```

## Utilisation avancée
### Listener
Pour une implémentation plus fine de l'écoute des notifications, il est possible d'utiliser la notion de *Listener*.
Un listener est une souscription d'une fonction callback à un type de notification.
Cette fonction sera appelée à chaque fois qu'une notification de ce type est reçue.

Chaque type de notification a sa propre classe dans le module `olvid.listeners`.

Dans cet exemple, la méthode `reply_to_message` sera appelée à chaque fois qu'un message arrive.

```python
import asyncio
from olvid import OlvidClient, datatypes, listeners

async def reply_to_message(message: datatypes.Message):
    await message.reply(f"Reply to: {message.body}")

async def main():
    client = OlvidClient()
    listener = listeners.MessageReceivedListener(handler=reply_to_message)
    client.add_listener(listener)
    await client.run_forever()

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

#### Listener: expiration
Par défaut, un listener écoute les notifications pour toujours, mais il est possible d'utiliser l'argument `count` pour n'écouter qu'un certain nombre de notifications.
Dans ce cas, lorsque que *count* notifications ont été traitées, le listener est arrêté.

Dans cet exemple, on répond au prochain message reçu puis le programme s'arrête.

```python
import asyncio
from olvid import OlvidClient, datatypes, listeners

async def reply_to_message(message: datatypes.Message):
    await message.reply(f"Reply to: {message.body}")

async def main():
    client = OlvidClient()
    # added count parameter set to 1
    listener = listeners.MessageReceivedListener(handler=reply_to_message, count=1)
    client.add_listener(listener)
    
    # wait_for_listeners_end: returns when all listeners are finished
    await client.wait_for_listeners_end()
    
    print("Program end")

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

#### Listener : filtrage

Les listeners permettent également de filtrer les notifications à traiter. 
Pour cela, on peut ajouter une ou plusieurs fonctions de filtrage à notre listener.
Les différentes formes de filtrage dépendent du type de notification et sont défini dans les messages du type *MessageReceivedNotificationSubscription* (cf [description protobuf](https://github.com/olvid-io/Olvid-Bot-Protobuf/tree/main/olvid/daemon/notification/v1) de l'API du daemon).

Par exemple, on peut vouloir traiter uniquement les messages envoyés par un certain contact.

```python
import asyncio
from olvid import OlvidClient, datatypes, listeners

CONTACT_ID: int = 1

async def reply_to_message(message: datatypes.Message):
    await message.reply(f"Reply to: {message.body}")

async def main():
    client = OlvidClient()
    # only notifications matching check_sender_id will be handled 
    listener = listeners.MessageReceivedListener(handler=reply_to_message, filter=datatypes.MessageFilter(sender_contact_id=CONTACT_ID))
    client.add_listener(listener)
    
    await client.wait_for_listeners_end()
    
asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

#### Listener avancé

Il est tout à fait possible de combiner le filtrage et l'expiration. 

Ici, on l'utilise pour effectuer une action et quitter le programme quand le message que l'on vient d'envoyer arrive sur le téléphone de son destinataire.

```python
import asyncio
from olvid import OlvidClient, datatypes, listeners

DISCUSSION_ID: int = 1

def get_message_id_checker(message_id: datatypes.MessageId):
  def checker(message: datatypes.Message):
      return message.sender_id == message_id
  return checker

async def main():
    client = OlvidClient()
    
    # send a message
    message = await client.message_send(discussion_id=DISCUSSION_ID, body="Hello there !")
    
    # add a listener to do something when message had been delivered, then program will exit 
    listener = listeners.MessageDeliveredListener(
        handler=lambda m: print("Message delivered"),
        checkers=[get_message_id_checker(message.id)],
        count=1
    )
    client.add_listener(listener)
    
    await client.wait_for_listeners_end()
    
    print("Program end")

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```
