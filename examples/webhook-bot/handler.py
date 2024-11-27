import base64
import os

import aiohttp
from aiohttp import web
from olvid import datatypes

from logger import logger
from NonceHolder import NonceHolder


#####
# TODO edit this function to change how webhook payload is handled
#####
async def handler(discussion: datatypes.Discussion, json_payload: dict) -> web.Response:
	try:
		# check payload validity
		if not json_payload.get("text") and not json_payload.get("attachments"):
			logger.error(f"Invalid payload received: {json_payload}")
			return web.Response(status=400)

		# add attachments to draft
		filenames_with_attachments: list[tuple[str, bytes]] = []
		if json_payload.get("attachments"):
			for attachment in json_payload.get("attachments"):
				attachment_b64 = attachment.get("payload")
				filename = attachment.get("filename")
				if attachment_b64 and filename:
					filenames_with_attachments.append((filename, base64.b64decode(attachment_b64)))
				else:
					logger.error(f"Invalid attachment received: {attachment}")

		message_body = json_payload.get("text")
		await discussion.post_message(body=message_body, attachments_filename_with_payload=filenames_with_attachments)
		return web.Response(status=200)
	except Exception as e:
		logger.exception("Cannot parse json payload")
		return web.Response(status=400)


def get_webhook_handler(nonce_holder: NonceHolder):
	# prepare webhook handler to set to server
	async def webhook_handler(json_payload: dict, nonce: str) -> web.Response:
		# check nonce is valid and associated to a discussion
		discussion_id: int = nonce_holder.get_discussion_id_associated_with_nonce(nonce)
		if not discussion_id:
			logger.error(f"Invalid nonce called: {nonce}")
			return web.Response(status=404)

		# retrieve associated discussion
		discussion: datatypes.Discussion = await nonce_holder.discussion_get(discussion_id=discussion_id)

		return await handler(discussion=discussion, json_payload=json_payload)
	return webhook_handler
