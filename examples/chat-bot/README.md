# Install

Clone repository:
```shell
git clone https://github.com/olvid-io/Olvid-Bot-Documentation
cd Olvid-Bot-Documentation/examples/chat-bot
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
When your bot is running you can send him messages in your Olvid application.

For example send: `!help` to list available commands, or send `!choose mountain sea countryside` to let the bot choose your future holiday destination.
