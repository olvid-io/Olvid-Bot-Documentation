import asyncio
import os

from aiohttp import web
from olvid import OlvidClient, tools, datatypes

SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT: str = os.getenv("SERVER_PORT", "8080")
# set up a random nonce for a private webhook url
WEBHOOK_NONCE: str = os.getenv("WEBHOOK_NONCE", "")

WELCOME_MESSAGE: str = os.getenv("WELCOME_MESSAGE", "Hi 👋 !")

# An extensible ChatBot, sending Welcome messages
class ChatBot(OlvidClient):
	async def on_discussion_new(self, discussion: datatypes.Discussion):
		await discussion.post_message(WELCOME_MESSAGE)

async def webhook_handler(request: web.Request) -> web.Response:
	client = OlvidClient()
	body: str = await request.text()
	if not body.strip():
		return web.Response(status=400)
	print(f"Broadcasting message: {body}")

	async for discussion in client.discussion_list():
		await discussion.post_message(await request.text())
	return web.Response(status=200)


# main function: create bots and webhook server and wait forever for notifications
async def main():
	# create, configure and start the webhook server in the background
	application = web.Application()
	server_runner = web.AppRunner(application)
	# create webhook route (with or without WEBHOOK_NONCE)
	if WEBHOOK_NONCE:
		application.add_routes([web.post(f"/{WEBHOOK_NONCE}", webhook_handler)])
	else:
		application.add_routes([web.post("/", webhook_handler)])
	await server_runner.setup()
	site = web.TCPSite(server_runner, SERVER_HOST, int(SERVER_PORT))
	await site.start()

	# create a chatbot instance
	chatbot = ChatBot()
	print("Starting bot !")

	# we create a pre-written bot that will accept every incoming invitation
	tools.AutoInvitationBot()

	# wait forever
	await chatbot.run_forever()
	print("Ending program")

	# stop webhook server
	await server_runner.cleanup()

# manage asyncio event loop
asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
