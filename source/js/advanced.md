# 👩‍💻 Développement

Nous allons essayer d'expliquer le fonctionnement et l'utilisation de notre paquet npm **@olvid/bot-node**.
 Idéalement, il vaut mieux la suivre étape par étape afin de suivre le cheminement, mais si vous vous sentez à l'aise, vous pouvez essayer d'accéder directement à la section qui vous intéresse.

:::{admonition} À propos de ***@olvid/bot-web***
Le paquet ***@olvid/bot-web*** est très similaire dans son usage mais possède certaines contraintes. (voir [](/js/browser.md))
- il n'utilise pas gRPC directement, il doit donc utiliser un proxy cf: [](/js/browser.md#daemon-et-proxy)
- il n'a pas accès à l'environnement, il faut donc passer l'url du serveur et la clé client lors de la création d'un *OlvidClient* ([ou la passer par d'autre moyens](/js/browser.md#clé-client))
- l'envoi de fichier ne fonctionne pas donc certaines méthodes comme *sendMessageWithAttachments* ne sont pas implémentées.

Vous pouvez facilement adapter le code présent dans cette page, mais il ne fonctionnera pas tel quel.
:::

:::{contents}
:local:
:depth: 2
:::

## Les bases

### OlvidClient
Pour interagir avec le {term}`daemon`, il vous faudra systématiquement créer une instance de la classe **OlvidClient**.
Il peut s'agir de la classe d'origine ou d'une classe enfant.

En node cette classe va automatiquement récupérer une clé client en utilisant l'environnement ou un fichier `.env`. (cf. [](/js/js.md#configuration))

Grâce à ce client, on pourra notamment exécuter des commandes et réagir à des notifications.

Voici à quoi ressemble un fichier *main.ts* de base contenant la création d'un client Olvid et l'exécution d'une commande (afficher l'identité courante).
Cette structure est à utiliser dans chacun des exemples de code de cette page, il suffit de remplacer le contenu de la fonction `main` par le code de votre choix.

```typescript
import { OlvidClient, datatypes } from "@olvid/bot-node";

async function main() {
    const client = new OlvidClient();
    const identity: datatypes.Identity = await client.identityGet();
    console.log(identity)
}

main().then();
```

### Commande
Toutes les méthodes gRPC de commandes exposées par le daemon sont facilement accessibles grâce à des méthodes de la classe **OlvidClient**.
Par exemple, pour envoyer un message (méthode `MessageSend` en gRPC), on utilisera la méthode `messageSend` de notre instance d'OlvidClient.

Dans le cas où nous connaissons l'identifiant de la discussion dans laquelle poster, cela donnerait :
```typescript
import { OlvidClient, datatypes } from "@olvid/bot-node";

async function main() {
    const client = new OlvidClient();
    await client.messageSend({discussionId: 1, body: "Use Olvid !"});
    console.log(identity)
}

main().then();
```

### Notification
La classe **OlvidClient** permet de facilement écouter les notifications émises par le daemon.
Ces méthodes commencent toutes par le préfixe `on` et permettent d'ajouter une fonction de rappel qui sera executé à chaque nouvelle notification.

Par exemple, pour afficher dans le terminal quand un message est reçu et lorsqu'une réaction est ajoutée, on peut faire :
```typescript
import { OlvidClient, datatypes } from "@olvid/bot-node";

async function main() {
    const client = new OlvidClient();
    client.onMessageReceived({
        callback: (message: datatypes.Message) => {
            console.log("Message received:", message.body);
        }
    })
    client.onMessageReactionAdded({
        callback: (message: datatypes.Message, reaction: datatypes.MessageReaction) => {
            console.log("Reaction added:", reaction.reaction);
        }
    })
    
    await client.runForever();
}

main().then();
```

## Utilisation avancée
### Filtrage des éléments
Pour accéder à des éléments précis de la base donnée on peut appliquer un filtre lors des commandes de type ***List***.

Voici des exemples de filtres possibles, les différents filtres sont définis dans la description protobuf de l'API du daemon ([ici](https://github.com/olvid-io/Olvid-Bot-Protobuf/tree/main/olvid/daemon/datatypes/v1)).

```typescript
import {datatypes, OlvidClient} from "@olvid/bot-node";

async function main() {
    const client = new OlvidClient();

    /*
     ** list one to one discussions
     */
    let otoDiscussionFilter = new datatypes.DiscussionFilter({
        type: datatypes.DiscussionFilter_Type.OTO
    });
    for await (const discussion of client.discussionList({filter: otoDiscussionFilter})) {
        console.log(`OneToOne discussion: ${discussion.id} - ${discussion.title}`)
    }
    
    /*
    ** list messages in a specific discussion with reactions 
     */
    const messageFilter = new datatypes.MessageFilter({
        discussionId: 1n,
        hasReaction: datatypes.MessageFilter_Reaction.HAS
    })
    const filteredMessages = await Array.fromAsync(client.messageList({filter: messageFilter}));
    console.log("Message with reactions in discussion", filteredMessages)
}

main().then();
```

### Filtrage des notifications
Pour une implémentation plus fine de l'écoute des notifications, on peut utiliser un système de filtrage.
Les différentes formes de filtrage dépendent du type de notification et sont définis dans les messages du type *MessageReceivedNotificationSubscription* (cf [description protobuf](https://github.com/olvid-io/Olvid-Bot-Protobuf/tree/main/olvid/daemon/notification/v1) de l'API du daemon).

#### *count*
Toutes les notifications peuvent être programmées pour n'être reçu qu'un nombre défini de fois à l'aide de l'argument count.
   
#### *filter*
La plupart des notifications possèdent un ou plusieurs attributs *filter*.
Si un filtre est spécifié une notification doit correspondre à l'ensemble des critères renseignés pour être envoyée.  

#### Exemple

Par exemple, on peut répondre uniquement au prochain message qui contient *hello* puis quitter le programme.
Pour cela, on construit un objet de type ***MessageFilter*** qui n'acceptera que les messages contenant le terme "hello" (*bodySearch*), et on spécifie qu'on ne veut traiter qu'une seule notification (*count* à 1).

```typescript
import { OlvidClient, datatypes, tools } from "@olvid/bot-node";

async function main() {
    const client = new OlvidClient();

    client.onMessageReceived({
        callback: async (message: datatypes.Message) => {
            await client.messageSend({
                discussionId: message.discussionId,
                body: "Hello World !",
            })
        },
        filter: new datatypes.MessageFilter({bodySearch: "hello"}),
        count: 1n
    })
    await client.waitForCallbacksEnd();
}

main().then();
```

:::{tip}
Dans les filtres, les champs de type string se terminant en **search** sont interprétés par un moteur de regexp pour une plus grande polyvalence.
:::

### Raccourcis
Les classes de base du module ***datatypes*** (*Message*, *Discussion*, *Attachment*, ...) implémentent des méthodes de raccourci pour avoir un code plus condensé et agréable à écrire.

Voici des exemples de méthodes, la liste exhaustive est définie dans le code source des classes, ou est accessible [ici](https://github.com/olvid-io/Olvid-Bot-Js-Client/tree/main/node/src/enhancer/olvid/daemon/datatypes/v1).

```typescript
import { OlvidClient, datatypes, tools } from "@olvid/bot-node";

async function main() {
    const client = new OlvidClient();

    client.onMessageReceived({
        callback: async (message: datatypes.Message) => {
            // easily reply to a message, and access to it's sender details
            const senderContact: datatypes.Contact = (await message.getSenderContact(client))
            await message.reply(
                client,
                `Hello ${senderContact.displayName} ! 👋`
            );
            
            // save attachments on disk if there are some
            if (message.attachmentsCount) {
                (await message.getAttachments(client)).forEach((attachment) => {
                    attachment.save(client, "./attachments")
                })
            }
        }
    })

    // post a message in a discussion and wait for message to be uploaded on server
    const discussion = (await Array.fromAsync(client.discussionList()))[0]
    const sentMessage = await discussion.postMessage(client, "Hello there");
    await sentMessage.waitFor.messageToBeUploaded(client);
    
    await client.runForever();
}

main().then();
```

### Décorateurs
Nous avons mis en place des décorateurs qui permettent de facilement écouter des notifications et mettre en place des commandes pour ChatBot.
Ils permettent d'écrire du code plus joli pour les programmes de type *Bot* qui tournent à l'infini.

Pour les utiliser, il faut sous-classer la classe OlvidClient, comme dans l'exemple suivant.

```typescript
import { OlvidClient, datatypes, onDiscussionNew, command } from "@olvid/bot-node";

class MyBot extends OlvidClient {
    @onDiscussionNew()
    async discussionNew(discussion: datatypes.Discussion) {
        await discussion.postMessage(this, `Hello ${discussion.title}} !`)
        // post help message when a new discussion is created
        await discussion.postMessage(this, this.getHelpMessage())
    }
    
    @command("!help")
    async help(message: datatypes.Message) {
        await message.reply(this, this.getHelpMessage())
    }

    @command("!ping")
    async ping(message: datatypes.Message) {
        await message.reply(this, "pong")
    }

    getHelpMessage() {
        return "### Available commands\n- *!help*\n- *!ping*"
    }
}

async function main() {
    const bot = new MyBot();
    await bot.runForever();
}

main().then();
```

## Conseils et astuces
### AutoInvitationBot
Pour rendre plus facile la mise en relation avec un bot, il est possible de mettre en place un autre bot, déjà écrit, qui acceptera toutes les invitations reçues.

Il suffit de créer un bot *AutoInvitationBot* du module `tools`. Il va automatiquement s'enregistrer pour recevoir les notifications de nouvelles invitations et les accepter.

:::{note}
Un *AutoInvitationBot* ne peut accepter que les présentations et les invitations de groupe. 
Il ne peut pas accepter automatiquement les invitations directes avec échange de SAS code. 
:::

Voici un programme qui lance une instance de l'AutoInvitationBot en tâche de fond.
Il est tout à fait possible de lancer plusieurs instances de bots en parallèle.

```typescript
import { OlvidClient, datatypes, tools } from "@olvid/bot-node";

async function main() {
    const client = new OlvidClient();
    client.onMessageReceived({
        callback: (message: datatypes.Message) => {
            console.log("Message received:", message.body);
        }
    })

    const invitationBot = new tools.AutoInvitationBot();

    await client.runForever();
}

main().then();
```

## Divers
### Envoyer un message éphémère
Les points d'entrée API `messageSend` et `messageSendWithAttachments` permettent de spécifier l'éphéméralité du message à envoyer.
On utilisera pour cela l'objet *datatypes.MessageEphemerality*.

Voici un exemple en typescript. Il est possible de spécifier les paramètres `read_once`, `visibility_duration` et `existence_duration` de manière indépendante.
Les durées d'existence et de visibilité sont en secondes.

```typescript
import { OlvidClient, datatypes, tools } from "@olvid/bot-node";

async function main() {
    const client = new OlvidClient();
    
    for await (const discussion of client.discussionList()) {
        await client.messageSend({
            discussionId: discussion.id,
            body: "Self destruct-message",
            ephemerality: new datatypes.MessageEphemerality({
                visibilityDuration: 10n,
                existenceDuration: 60n,
                readOnce: true
            })
        })
    }
}

main().then();
```
