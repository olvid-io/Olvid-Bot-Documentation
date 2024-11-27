# 👩‍💻 Start coding

:::{important}
Examples below requires a running and accessible {term}`daemon` instance, and a valid {term}`client key` to be executed.

If you need to set up a daemon you might start with our [](/quickstart.md).

You also need to [set your client key 🔑](/quickstart.md#setup-client-key) in your program environment. 
:::

## Bots

### Notification Bot
Let's get started by creating a Bot that displays the content of basic notifications.

To write a Bot that runs in the background with minimal effort,
simply create a class that overrides the OlvidClient class and overrides the methods associated with the notifications you want to listen for.

Here is an example `main.py` file.

```python
import asyncio
from olvid import OlvidClient, datatypes

class NotificationBot(OlvidClient):
	async def on_message_received(self, message: datatypes.Message):
		print(f"=> {message.body}")
		# reply to message to trigger on_message_sent handler
		await message.reply(f"reply to: {message.body}")

	async def on_message_sent(self, message: datatypes.Message):
		print(f"<= {message.body}")
	
async def main():
	bot = NotificationBot()
	print("Starting ...")
	await bot.run_forever()

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

You can now run your program with:

```shell
python3 main.py
```

```{tip}
Don't worry if nothing seems to happen - that's normal!

To interact with your ChatBot, you need to send a message using Olvid.
```

### Command Chat Bot
We can start by writing a chatbot that responds to specific commands.

The simplest approach is to extend the OlvidClient class and use the @OlvidClient.command decorator.

You can copy and edit this code in a `main.py` file.

```python
import asyncio
from olvid import OlvidClient, datatypes

class ChatBot(OlvidClient):
	@OlvidClient.command(regexp_filter="!hi")
	async def hi_cmd(self, message: datatypes.Message):
		sender_contact: datatypes.Contact = await self.contact_get(contact_id=message.sender_id) 
		await message.reply(f"hi {sender_contact.display_name}")

	@OlvidClient.command(regexp_filter="!help")
	async def help_cmd(self, message: datatypes.Message):
		body: str = "Available commands:\n" 
		body += "!help: send this help message"
		body += "!hi: send a greeting message"
		body += "!"
		await message.reply(body)

async def main():
	bot = ChatBot()
	print("Starting ...")
	await bot.run_forever()

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```

To interact with your ChatBot, you need to send one of the commands you've implemented in Olvid. 
For instance, try sending `!help` to get started.

## Scripts

### Basic script example

```python
import asyncio
from olvid import OlvidClient

async def main():
	client = OlvidClient()
	
	######
	# TODO do your things here
	# As an example we print current identity
	print(await client.identity_get())
	
	await client.stop()

asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
```
