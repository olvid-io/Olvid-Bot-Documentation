from __future__ import annotations

import json
from typing import Callable, Awaitable

from aiohttp import web

from logger import logger


class WebhookServer(web.Application):
	def __init__(self, webhook_handler: Callable[[dict, str], Awaitable[web.Response]], server_host: str = "0.0.0.0", server_port: int = 8080):
		# we must improve request max size if we want to attachments in requests
		super().__init__(client_max_size=100 * 1000 * 1000)

		self.server_host: str = server_host
		self.server_port: int = server_port

		# we need a runner to let server run on background while our bot is listening for notifications
		self.runner = web.AppRunner(self)

		# method called after a proper bot_webhook entrypoint call
		self.webhook_handler: Callable[[dict, str], Awaitable[web.Response]] = webhook_handler

		# set bot_webhook handler
		self.add_routes([web.post(f"/{{nonce}}", self._webhook_handler_wrapper)])

		# set ping route
		self.add_routes([web.get(f"/ping", self.ping_handler)])

	async def background_start(self):
		await self.runner.setup()
		site = web.TCPSite(self.runner, self.server_host, self.server_port)
		await site.start()

	async def background_stop(self):
		await self.runner.cleanup()

	async def _webhook_handler_wrapper(self, request: web.Request):
		# get nonce
		nonce = request.match_info.get("nonce")

		# read body
		if not request.can_read_body:
			logger.error(f"No payload sent")
			return web.Response()
		body: bytes = await request.read()

		# parse body as json
		try:
			json_body: dict = json.loads(body.decode())
		except json.JSONDecodeError:
			logger.error(f"Invalid payload received: {body}")
			return web.Response()

		return await self.webhook_handler(json_body, nonce)

	# noinspection PyUnusedLocal
	@staticmethod
	async def ping_handler(request: web.Request):
		return web.Response(text="pong")
