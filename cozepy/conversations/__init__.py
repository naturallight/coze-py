from typing import Dict, List

from cozepy.auth import Auth
from cozepy.chat import Message
from cozepy.model import CozeModel
from cozepy.request import Requester


class Conversation(CozeModel):
    id: str
    created_at: int
    meta_data: Dict[str, str]


class ConversationsClient(object):
    def __init__(self, base_url: str, auth: Auth, requester: Requester):
        self._base_url = base_url
        self._auth = auth
        self._requester = requester
        self._messages = None

    def create(self, *, messages: List[Message] = None, meta_data: Dict[str, str] = None) -> Conversation:
        """
        Create a conversation.
        Conversation is an interaction between a bot and a user, including one or more messages.
        """
        url = f"{self._base_url}/v1/conversation/create"
        body = {
            "messages": [i.model_dump() for i in messages] if len(messages) > 0 else [],
            "meta_data": meta_data,
        }
        return self._requester.request("post", url, Conversation, body=body)

    def retrieve(self, *, conversation_id: str) -> Conversation:
        """
        Get the information of specific conversation.
        """
        url = f"{self._base_url}/v1/conversation/retrieve"
        params = {
            "conversation_id": conversation_id,
        }
        return self._requester.request("get", url, Conversation, params=params)

    @property
    def messages(self):
        if not self._messages:
            from .message import MessagesClient

            self._messages = MessagesClient(self._base_url, self._auth, self._requester)
        return self._messages