# {octicon}`webhook;1em;sd-text-primary` Webhook Server

You can find the code of our Webhook Server implementation [here](https://github.com/olvid-io/Olvid-Bot-Quickstart/tree/main/examples/bot_webhook).

### Setup
Clone our Quickstart repository.
```shell
git clone https://github.com/olvid-io/Olvid-Bot-Quickstart quickstart
cd quickstart/examples/bot_webhook
```

Start your daemon (see [](/quickstart.md) if necessary) and export your client key to environment (see [](/quickstart.md#setup-client-key)).

This Bot embeds an HTTP server to handle webhook entry points.
To set it up, you'll need to define the following environment variables:

WEBHOOK_SERVER_PORT: The port on which the Bot's HTTP server should listen.
WEBOOK_SERVER_HOST: The IP address to listen on.
WEBHOOK_PUBLIC_URL: The complete URL that allows access to the Bot's server.

Here is an example configuration to use in development.
```shell
export WEBHOOK_SERVER_PORT=8080
export WEBOOK_SERVER_HOST=0.0.0.0
export WEBHOOK_PUBLIC_URL=http://localhost:8080
```

```{warning}
By using `localhost` as your public url you will only be able to trigger webhook URL from your computer / server.

To trigger from anywhere in the world you will need to setup a reverse proxy exposed on the world (see [](#deploy))
```

### Run
Start bot with:

```shell
python3 main.py
```

### How to use it ?
When a new conversation is created (i.e., when a new contact is added or the Bot is added to a group), this Bot automatically sets up a webhook entry point.

This allows you to use this entry point to post messages and attachments directly into that specific conversation.

When you started your bot you can use help command to retrieve the webhook URL associated with a discussion. 
Simply post `!help` in this discussion.

Then you can use `curl` (or any other way) to make POST requests to this URL.

Here are a few example payloads as curl commands (replace WH_URL with the webhook URL provided by your bot).

```shell
export WH_URL=http://localhost:8080/...

# send a text message only
curl -X POST --data '{"text":"Hello"}' $WH_URL

# send an attachment publicly available
curl -X POST --data \
'{"attachments":[{"url":"https://olvid.io/assets/img/olvid-logo.png","filename":"olvid-logo.png"}]}' \
$WH_URL

# send an text message with a file attached as base64
curl -X POST --data \
'{"text":"Olvid is good for you","attachments":[{"payload":"VXNlIG9sdmlkCg==","filename":"file.txt"}]}' \ 
$WH_URL
```

### Deploy
Here is an example of nginx configuration file to set up a reverse proxy and serve your webhook entrypoints.

```nginx
server {
	server_name webhook.example.com;
	
	access_log /var/log/nginx/webhook-access.log;
	error_log /var/log/nginx/webhook-error.log;

	location / {
		proxy_pass http://localhost:8080;
		client_max_body_size 100M;
	}
}
```

Mind to change `WEBHOOK_PUBLIC_URL` env variable with your server_name. For example, in that case you might set WEBHOOK_PUBLIC_URL=https://webhook.example.com. 
