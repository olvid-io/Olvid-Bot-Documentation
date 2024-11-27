import asyncio
import os

from olvid import OlvidClient, tools

from ChatBot import ChatBot
from NonceHolder import NonceHolder
from WebhookServer import WebhookServer
from handler import get_webhook_handler
from logger import logger

# read env configuration
WEBHOOK_SERVER_HOST: str = os.getenv("WEBHOOK_SERVER_HOST", "0.0.0.0")
WEBHOOK_SERVER_PORT: int = int(os.getenv("WEBHOOK_SERVER_PORT", "8080"))
WEBHOOK_PUBLIC_URL: str = os.getenv("WEBHOOK_PUBLIC_URL", f"http://localhost:{WEBHOOK_SERVER_PORT}")


async def main():
	# create a nonce holder to store webhook nonce associated to discussions
	nonce_holder: NonceHolder = NonceHolder(webhook_public_url=WEBHOOK_PUBLIC_URL)

	# create server and start in background
	server: WebhookServer = WebhookServer(webhook_handler=get_webhook_handler(nonce_holder), server_host=WEBHOOK_SERVER_HOST, server_port=WEBHOOK_SERVER_PORT)
	await server.background_start()

	bots: list[OlvidClient] = [
		# create chatbot
		ChatBot(nonce_holder=nonce_holder),
		# create other pre-written bots
		# create a bot to automatically accept every invitation you receive
		tools.AutoInvitationBot(),
		# create a bot to delete every message when they have been handled.
		# This avoids database to grow indefinitely and improve performances
		tools.SelfCleaningBot()
	]

	logger.info("Ready to start !")
	logger.info(f"Webhook public url: {WEBHOOK_PUBLIC_URL}")

	# wait forever
	for bot in bots:
		await bot.wait_for_listeners_end()

	# clean before exit
	await server.background_stop()
	for bot in bots:
		await bot.stop()

if __name__ == '__main__':
	asyncio.run(main())
