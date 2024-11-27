# Install

Clone repository:
```shell
git clone https://github.com/olvid-io/Olvid-Bot-Documentation
cd Olvid-Bot-Documentation/examples/broadcast-bot
```

Install dependencies:
```shell
pip3 install -r requirements.txt
```

If necessary set up your Olvid daemon follow our documentation tutorial : https://doc.bot.olvid.io.

When your daemon is ready to use, set up your bot client key.
If you forgot your client key you can use the command `key get` with **olvid CLI** to list your existing client keys. 

```shell
echo OLVID_CLIENT_KEY=....> .env
```

Your bot is now ready to be started with:
```shell
python3 main.py
```

It will run forever, until you stop it with CTRL+C.

This code is editable, and you can use it as a base your for your project.

If you face any trouble we have a [TROUBLESHOOTING](https://doc.bot.olvid.io/python/troubleshooting.html) page.

# Use
When your bot is up and running you can make him broadcast a message to all it's contacts and groups. Just send a valid HTTP POST request with any tool.

Here is an example using the `curl` command.

```shell
curl -X POST --data 'Hello Olvid !' http://localhost:8080/$WEBHOOK_NONCE 
```

You can edit the **webhook_handler** method to receive more complex payloads. For example, you can use a json payload to transmit more data, or you can send files to send as attachments.

You can also edit the **ChatBot** class to add commands or interactions when people get in touch or send messages to your bot. 

For a more complete and complexe approach you can check the **[Webhook Bot](../webhook-bot)** example.

# Setup 
Environment variables used by our bot:
```shell
# ip adress the webhook server listens on
SERVER_HOST=0.0.0.0
# port used by webhook server
SERVER_PORT=8080
# add a prefix in webhook url to make it "private"
WEBHOOK_NONCE=
# message sent by your bot when add it as a contact or in a group
WELCOME_MESSAGE='Hi 👋 !'
```
