# {octicon}`broadcast;1em;sd-text-primary` Broadcast Bot

You can find the code of our Broadcast implementation [here](https://github.com/olvid-io/Olvid-Bot-Quickstart/tree/main/examples/bot_broadcast).

This bot is a very simple implementation and might be modified to feat your requirements.

This bot simply expose a POST webhook entrypoint and send the request content to every contact / group.

### Setup
Start your daemon (see [](/quickstart.md) if necessary) and export your client key to environment (see [](/quickstart.md#setup-client-key)).

Clone our Quickstart repository.
```shell
git clone https://github.com/olvid-io/Olvid-Bot-Quickstart quickstart
cd quickstart/examples/bot_broadcast
python3 main.py
```

Broadcast a message using curl (or any other http tool).
```shell
curl -X POST --data "Hello Olvid !" http://localhost:8080
```

% todo: finish writing documentation (check common parts with webhook server)
