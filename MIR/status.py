from fastapi import APIRouter, Body, Query, Request
from helpers import create_state, get_ip
from pydantic import BaseModel
from typing import List, Optional
import json

router = APIRouter()

# Define a Pydantic model for the payload
class StatusPayload(BaseModel):
    map_id: Optional[str] = None
    mode_id: Optional[int] = None
    state_id: Optional[int] = None
    web_session_id: Optional[str] = None
    position: Optional[dict] = None
    serial_number: Optional[str] = None
    name: Optional[str] = None
    answer: Optional[str] = None
    guid: Optional[str] = None
    clear_error: Optional[bool] = None
    datetime: Optional[str] = None
       
@router.get("/status", summary="GET /status", tags=["Status"])
def get_status(request: Request):
    shared_state = request.app.state.shared_state
    
    ip = get_ip(request)

    return shared_state[ip]["status"]

@router.put("/status/", summary="PUT /status", tags=["Status"])
def update_status(request: Request,
        payload: StatusPayload = Body(..., description="The new values of the status")
    ):

    ip = get_ip(request)

    if payload.state_id == 3:
        request.app.state.shared_state[ip]["status"]["state_id"] = 3
        request.app.state.shared_state[ip]["status"]["state_text"] = "Ready"
    elif payload.state_id == 4:
        request.app.state.shared_state[ip]["status"]["state_id"] = 4
        request.app.state.shared_state[ip]["status"]["state_text"] = "Pause"
    else:
        return {"error": "Invalid state_id"}


    return request.app.state.shared_state[ip]["status"]

