import uuid
from contextvars import ContextVar

from logger import logger

# we are using context variables to store request level context , as FASTAPI
# does not provide request context out of the box

# context_api_id stores unique id for every request
context_api_id: ContextVar[str] = ContextVar('api_id', default=None)
# context_log_meta stores log meta data for every request
context_log_meta: ContextVar[dict] = ContextVar('log_meta', default={})


# TODO: additional request context information
async def build_request_context():
    context_api_id.set(str(uuid.uuid4()))
    context_log_meta.set({'request_id': context_api_id.get()})
    logger.info(extra=context_log_meta.get(), msg="REQUEST_INITIATED")
