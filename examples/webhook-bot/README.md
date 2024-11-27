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
When your bot is up and running you can send an `!help` command message in any discussion with the bot. 
When you retrieved the webhook URL associated with this discussion you can send a POST HTTP request using any tool.

Here are soms examples using the `curl` command. (replace ${WEBHOOK_URL} with the correct url).
```shell
# send a basic text message
curl -X POST --data '{"text":"Hello Olvid !"}' ${WEBHOOK_URL}
# send a text message with an attachment
curl -X POST --data '{"text":"Hello Olvid !","attachments":[{"payload":"VXNlIE9sdmlkICEK","filename":"olvid.txt"}]}' ${WEBHOOK_URL}
```

You can edit the **handler.py** file to change your webhook payload format.

You can also edit the **ChatBot** class to add commands or interactions when people get in touch or send messages to your bot. 

# Setup 
Environment variables used by our bot:
```shell
# ip address the webhook server listens on
WEBHOOK_SERVER_HOST=0.0.0.0
# port used by webhook server
WEBHOOK_SERVER_PORT=8080
# how to access your webhook server. This is used to send webhook url in olvid discussions.
WEBHOOK_PUBLIC_URL=http://localhost:${WEBHOOK_SERVER_PORT}
```
