import asyncio
import os

from olvid import OlvidClient, datatypes

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

	# create chatbot
	chat_bot: ChatBot = ChatBot(nonce_holder=nonce_holder)

	# configure daemon to auto accept invitations and delete message history
	settings: datatypes.IdentitySettings = await chat_bot.settings_identity_get()
	settings.invitation = datatypes.IdentitySettings.AutoAcceptInvitation(True, True, True, True)
	settings.message_retention = datatypes.IdentitySettings.MessageRetention(discussion_count=5, clean_locked_discussions=True)
	settings.keycloak = datatypes.IdentitySettings.Keycloak(auto_invite_new_members=True)
	await chat_bot.settings_identity_set(settings)

	logger.info("Ready to start !")
	logger.info(f"Webhook public url: {WEBHOOK_PUBLIC_URL}")

	# wait forever
	await chat_bot.wait_for_listeners_end()

	# clean before exit
	await server.background_stop()
	await chat_bot.stop()

if __name__ == '__main__':
	asyncio.run(main())
