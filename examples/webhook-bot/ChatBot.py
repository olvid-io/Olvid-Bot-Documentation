import secrets

from olvid import OlvidClient, datatypes

from NonceHolder import NonceHolder


class ChatBot(OlvidClient):
	def __init__(self, nonce_holder: NonceHolder):
		super().__init__()
		self.nonce_holder: NonceHolder = nonce_holder

	####
	# notification handlers
	####
	@OlvidClient.command(regexp_filter="^!help")
	async def help_cmd(self, message: datatypes.Message):
		await self.post_help_message(discussion_id=message.discussion_id)

	async def on_discussion_new(self, discussion: datatypes.Discussion):
		await self.post_welcome_message(discussion=discussion)

	####
	# Create messages
	####
	async def post_welcome_message(self, discussion: datatypes.Discussion):
		greeting: str = secrets.choice(['Hi', 'Hello'])
		if discussion.is_contact_discussion():
			contact: datatypes.Contact = await discussion.get_contact()
			name: str = f"{' '.join([contact.details.first_name, contact.details.last_name])}"
		else:
			name: str = f"everyone"

		await self.message_send(discussion_id=discussion.id, body=f"{greeting} {name} 👋")
		await self.post_help_message(discussion_id=discussion.id)

	async def post_help_message(self, discussion_id: int):
		await self.message_send(discussion_id=discussion_id, body="Here is the webhook url to use to post in this discussion")
		await self.message_send(discussion_id=discussion_id, body=await self.nonce_holder.get_or_create_discussion_webhook_url(discussion_id=discussion_id))
