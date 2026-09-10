from pydantic import BaseModel


class ToolResponse(BaseModel):
    success: bool
    message: str
    data: dict | None = None
