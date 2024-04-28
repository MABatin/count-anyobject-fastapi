from typing import Optional, Any

from pydantic.main import BaseModel


class GenericResponseModel(BaseModel):
    """Generic response model for all responses"""
    api_id: Optional[str] = None
    error: Optional[str]
    message: Optional[str]
    data: Any = None
    status_code: Optional[int] = None
