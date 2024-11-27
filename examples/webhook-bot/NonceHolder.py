import uuid
from typing import Optional

from olvid import OlvidClient
from logger import logger


class NonceHolder(OlvidClient):
	def __init__(self, webhook_public_url: str):
		super().__init__()
		self._DISCUSSION_STORAGE_KEY: str = "bot_webhook-nonce"

		self.webhook_public_url: str = webhook_public_url

		self._initialized: bool = False

		self._nonce_by_discussion_id: dict[int, str] = {}
		self._discussion_id_by_nonce: dict[str, int] = {}

		self.add_background_task(self.init(), "BasicNonceHolder-load-from-storage")

	# load stored nonce from daemon storage to store them in memory
	async def init(self):
		if self._initialized:
			raise ValueError("BasicNonceHolder: trying to initialize an initialized instance")

		async for discussion in self.discussion_list():
			discussion_id: int = discussion.id
			nonce: str = await self.discussion_storage_get(key=self._DISCUSSION_STORAGE_KEY, discussion_id=discussion_id)
			self._nonce_by_discussion_id[discussion_id] = nonce
			self._discussion_id_by_nonce[nonce] = discussion_id

		self._initialized = True

	def get_discussion_id_associated_with_nonce(self, nonce: str) -> Optional[int]:
		if not self._initialized:
			raise ValueError("BasicNonceHolder not initialized")
		return self._discussion_id_by_nonce.get(nonce)

	def get_nonce_associated_to_discussion(self, discussion_id: int) -> Optional[str]:
		if not self._initialized:
			raise ValueError("BasicNonceHolder not initialized")
		return self._nonce_by_discussion_id.get(discussion_id)

	async def get_or_create_nonce_for_discussion(self, discussion_id: int) -> str:
		nonce = self.get_nonce_associated_to_discussion(discussion_id)
		if nonce:
			logger.debug(f"Found existing nonce for this discussion: {discussion_id} -> {nonce}")
			return nonce

		# create a nonce for this discussion and store it
		nonce = str(uuid.uuid4())
		self._discussion_id_by_nonce[nonce] = discussion_id
		self._nonce_by_discussion_id[discussion_id] = nonce
		logger.debug(f"Created new nonce for a discussion: {discussion_id} -> {nonce}")

		# save into storage
		await self.discussion_storage_set(key=self._DISCUSSION_STORAGE_KEY, value=nonce, discussion_id=discussion_id)

		return nonce

	async def get_or_create_discussion_webhook_url(self, discussion_id: int):
		nonce = await self.get_or_create_nonce_for_discussion(discussion_id=discussion_id)
		return f"{self.webhook_public_url}/{nonce}"
