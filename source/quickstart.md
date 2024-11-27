# 🚀 Quickstart

## Prerequisite

In this installation guide we will use Docker and Python3.

You can install docker [here](https://docs.docker.com/engine/install/).

We will need at least Python3.10 to use [olvid-bot](https://pypi.org/project/olvid-bot/) module.
If your python install is older you will have to update it.

:::{hint}
On macOS, we recommend homebrew if you need a newer Python version.

```sh
brew install python3
```
:::

## Setup Daemon

### Start daemon

{term}`Daemon` is available as a docker image on [Docker Hub](https://hub.docker.com/r/olvid/bot-daemon).

Because we want our daemon to persist data we will setup our container using [docker compose](https://docs.docker.com/compose/).

Here is a minimal `docker-compose.yaml` file.

```yaml
services:
  daemon:
    image: olvid/bot-daemon
    environment:
      - OLVID_ADMIN_CLIENT_KEY_CLI=SetARandomValue
    ports:
      - 50051:50051
    volumes:
      - ./data:/daemon/data
```

It defines a service named daemon, that will run a container from our public [daemon image](https://hub.docker.com/r/olvid/bot-daemon).

Replace SetARandomValue with a random value.
This will let daemon start with an admin client key set to the value you pass.
We will pass the same value to the <project:#cli/cli> to grants admin permissions.
You can use `uuidgen` bash command to generate a secure random key.

We also opened the 50051 port (default gRPC port), and mounted a data volume to persist data on host file system.

Now you can start your daemon in the background.

```sh
docker compose up -d daemon
```

To check the daemon logs you can use this command.

```sh
docker compose logs -f daemon
```

### Setup CLI

To set up our daemon instance, we'll use the Olvid Command-Line Interface (CLI), which is embedded in our Python client module, available on `pip`.

First, install the olvid package:

```sh
pip3 install olvid-bot
```

:::{warning}
Currently CLI does not support Windows. To run CLI on windows use our docker image:
```shell
docker run -it --rm --env-file .env olvid/bot-python-runner
```
:::

Then set up the admin client key for CLI.
It's the client key you previously set in daemon environment.

This admin client key can be passed to CLI using a file or environment.

```{eval-rst}
.. dropdown:: :octicon:`command-palette;1em` Use .env file
    :open:

    Create an .env file.
    Remember to always run your Command-Line Interface (CLI) from the current working directory.

    .. code-block:: sh

        echo OLVID_ADMIN_CLIENT_KEY=MyAdminClientKey > .env
```

```{eval-rst}
.. dropdown:: :octicon:`command-palette;1em` Use environment

    You can also export your admin client key to environment every time you start a shell session.

    .. code-block:: sh

            export OLVID_ADMIN_CLIENT_KEY=MyAdminClientKey

```

### Start CLI

Now we can run the CLI in interactive mode.

```sh
olvid-cli
```

:::{hint}
:class: warning

If the `olvid-cli` binary is not available, you can start CLI with python:

```sh
python3 -m olvid-bot
```
:::

(initialize-daemon)=

### Initialize daemon

When we set up cli and launched daemon we can start CLI to initialize daemon.

The aim will be to create a new {term}`identity` that our bot will use.
We will also retrieve a client key to let our bot connect to daemon, and finally we will add bot to our Olvid contacts to exchange with him.

These three steps can be achieved with just one command: `identity new`.
Then you can follow the instructions on the screen.

Here is a full example with comments. User inputs start with a > and comments with a #.

```sh
# We create a new identity. LastName, Position, and Company are optional.
# These details can be updated later.
0 > identity new FirstName LastName Position Company

# A client key to connect using this identity is automatically created;
# you must keep it somewhere.
identity creation > Here is your client key to connect to daemon with this identity:
AAAAAAAA-BBBB-AAAA-AAAA-AAAAAAAAAAAA

# You can directly add this new identity to your contacts.
# This step is optional but necessary if you want to interact with your bot.
identity creation > Do you want to add this identity to your contacts ? (y/N)
>yes

# This is an invitation link for this new identity.
# You can open it in your browser and scan the QR code with your mobile application.
# You can also copy it and import it into your desktop application.
identity creation > Send an invitation to this invitation link: https://invitation.olvid.io/#........

# From now, CLI is waiting for a new invitation to arrive ...
# When your invitation arrives, the flow continues.
identity creation > Please enter sas code displayed on the other device

# Enter the four-digit code visible on your device.
> 0000

# Enter the following code in your device
identity creation > Please enter this sas code on the other device: 1111

# Flow is now complete
Now using identity: 1
You can now send messages to YOUR NAME in discussion 1
1 >
```

As you can see, the command prompt changed and is now prefixed with a 1 instead of a 0. This is because the CLI is now automatically using this new identity, designated by its ID: 1. Most commands you will run from now will be executed using this identity. For example if you list contacts using the contact get command you will see the contacts of this specific identity.

A daemon can host more than one identity. In that case, you'll need to change the identity in use with the identity current command.

To learn more about the CLI and its commands, see: [](cli/cli.md).

## Your first bot

### Setup client key
To allow your bot to authenticate when connecting to the daemon, it will need the client key that was displayed earlier. If you lost it, you can list registered client keys using the CLI: `olvid-cli key get`.

This client key can be passed to your using environment variables:

```{eval-rst}
.. dropdown:: :octicon:`command-palette;1em` Use .env file
    :open:

    Create an .env file (or edit your previous .env file).

    .. code-block:: sh

        echo OLVID_CLIENT_KEY=MyClientKey >> .env
```

```{eval-rst}
.. dropdown:: :octicon:`command-palette;1em` Use environment

    You can also export your client key to environment every time you start a shell session.

    .. code-block:: sh

        export OLVID_CLIENT_KEY=MyClientKey
```

### Echo bot

Now, let's write a minimalist bot in Python in a file named `main.py`.

```python
# we use coroutines to run code asynchronously
import asyncio
# elements we need in olvid-bot module
from olvid import OlvidClient, datatypes

# we write a class extending the OlvidClient base class
class MyFirstBot(OlvidClient):
    # we override this specific method, called every time our bot receives a message
    async def on_message_received(self, message: datatypes.Message):
        print(f"> {message.body}")
        # when a message arrives we post another message in this discussion with the same content
        await message.reply(body=message.body)

async def main():
    # create the bot
    bot: MyFirstBot = MyFirstBot()
    print("Bot is ready!")
    # In this case this method wait forever
    await bot.wait_for_listeners_end()

# A way to start your program in python asynchronous paradigm
asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

This code requires the [olvid-bot] package, which you previously installed using *pip*.
If not, you can install it with:

```sh
pip3 install olvid-bot
```

To start your bot, simply run:

```sh
python3 main.py
```

You will need your daemon to be up and running, and your client key to be set in your environment if that's the method you chose.

When your bot has started, you can send it a message from your mobile or your desktop app to check that everything is working properly.

Here is an example of what your are expecting.

```{eval-rst}
.. grid::

    .. grid-item-card::
        :width: 50%

        .. image:: _static/images/quickstart-echo-bot-discussion.png
            :alt: Olvid discussion with your echo bot.
            :align: center

```

Well done, you just created your first Olvid Bot 🤖 !

### Next Steps

```{eval-rst}
.. todo:: add reference to bot examples section
```

You can now check how to write more complex bots in [](/bots/bots.md).

If you want to deploy a production ready environment check [](/configuration.md) section to see more advanced deployment use cases.
