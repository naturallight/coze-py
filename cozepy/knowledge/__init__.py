from typing import TYPE_CHECKING, Optional

from cozepy.auth import Auth
from cozepy.request import Requester
from cozepy.util import remove_url_trailing_slash

if TYPE_CHECKING:
    from .documents import AsyncDocumentsClient, DocumentsClient


class KnowledgeClient(object):
    def __init__(self, base_url: str, auth: Auth, requester: Requester):
        self._base_url = remove_url_trailing_slash(base_url)
        self._auth = auth
        self._requester = requester
        self._documents: Optional[DocumentsClient] = None

    @property
    def documents(self) -> "DocumentsClient":
        if self._documents is None:
            from .documents import DocumentsClient

            self._documents = DocumentsClient(base_url=self._base_url, auth=self._auth, requester=self._requester)
        return self._documents


class AsyncKnowledgeClient(object):
    def __init__(self, base_url: str, auth: Auth, requester: Requester):
        self._base_url = remove_url_trailing_slash(base_url)
        self._auth = auth
        self._requester = requester
        self._documents: Optional[AsyncDocumentsClient] = None

    @property
    def documents(self) -> "AsyncDocumentsClient":
        if self._documents is None:
            from .documents import AsyncDocumentsClient

            self._documents = AsyncDocumentsClient(base_url=self._base_url, auth=self._auth, requester=self._requester)
        return self._documents
