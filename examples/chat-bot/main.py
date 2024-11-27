import asyncio
import secrets

from olvid import datatypes, OlvidClient, tools

class ChatBot(OlvidClient):
	# send an help message
	@OlvidClient.command(regexp_filter="^!help")
	async def help(self, message: datatypes.Message):
		print("!help command")
		await message.reply(body=self.get_help_message())

	# add a ping command to check bot is working
	@OlvidClient.command(regexp_filter="^!ping")
	async def ping(self, message: datatypes.Message):
		print("!ping command")
		await message.reply("pong !")

	# add a choose command: we remove the !choose prefix, then we randomly choose one of the proposal
	@OlvidClient.command(regexp_filter="^!choose")
	async def choose(self, message: datatypes.Message, matched_body: str):
		body_without_command: str = message.body.removeprefix(matched_body).strip()
		choices: list[str] = body_without_command.split()
		final_choice: str = secrets.choice(choices)
		print(f"!choose command: {choices} -> {final_choice}")
		await message.reply("I chose: " + final_choice)

	# On new discussions we send a greeting and the help message to explain people how to use the bot.
	# on_discussion_new is triggered when a contact had been added or when the bot joined a group.
	async def on_discussion_new(self, discussion: datatypes.Discussion):
		print(f"on_discussion_new: {discussion.title}")
		await discussion.post_message("Hi 👋")
		await discussion.post_message(self.get_help_message())

	# We also listen for every new messages, if the message is an invalid message we send the help message.
	async def on_message_received(self, message: datatypes.Message):
		if message.body.startswith("!") and not self.is_message_body_a_valid_command(message.body):
			print(f"Invalid command: {message.body}")
			await message.reply(f"Invalid command: {message.body.split()[0]}")
			await message.reply(self.get_help_message())

	# help message is shared between methods so we use a common static method
	@staticmethod
	def get_help_message() -> str:
		return """
### Available commands:
**!ping**: check I am alive
**!choose A B**: let me choose for you between A and B. 
"""

# main function: create bots and wait forever for notifications
async def main():
	# create a chatbot instance
	chatbot = ChatBot()
	print("Starting bot !")

	# we create another pre-written bot that will accept every incoming invitation
	tools.AutoInvitationBot()

	# wait forever
	await chatbot.run_forever()
	print("Ending program")

# manage asyncio event loop
asyncio.set_event_loop(asyncio.new_event_loop())
asyncio.get_event_loop().run_until_complete(main())
