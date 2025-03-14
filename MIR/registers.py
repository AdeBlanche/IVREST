from fastapi import APIRouter, Body, Path, Query, Request
from helpers import create_state, get_ip
from pydantic import BaseModel
from typing import List, Optional
import json

router = APIRouter()

# Define a Pydantic model for the payload
class Register(BaseModel):
    value: int
    label: str

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
       
@router.get("/registers", summary="GET /registers", tags=["Registers"])
def get_registers(request: Request):
    shared_state = request.app.state.shared_state
    
    ip = get_ip(request)

    return shared_state[ip]["registers"]

@router.get("/registers/{id}", summary="GET /registers/{id}", tags=["Registers"])
def get_register(
        id: int,
        request: Request
    ):
    shared_state = request.app.state.shared_state
    ip = get_ip(request)

    for register in shared_state[ip]["registers"]:
        if register["id"] == id:
            return register

    return {"error": "No such register"}



@router.put("/registers", summary="PUT /registers/{id}", tags=["Registers"])
def update_status(
        request: Request,
        payload: StatusPayload = Body(..., description="the id")
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

@router.post("/registers/{id}", summary="POST /registers/{id}", tags=["Registers"])
def update_register(request: Request,
        id: int = Path(..., description="The id to add the new resource to"), 
        register: Register = Body(..., description="The details of the register"),
    ):
    shared_state = request.app.state.shared_state
    ip = get_ip(request) 

    # Prepa3ddre new register object
    new_register = dict(register)
    new_register["id"] = id
    new_register["url"] = "/v2.0.0/registers/" + str(id)

    for i, reg in enumerate(shared_state[ip]["registers"]):
        if reg["id"] == id:
            # Remove the old one
            del request.app.state.shared_state[ip]["registers"][i]

    # Add it as a new register since it does not exist
    request.app.state.shared_state[ip]["registers"].append(new_register)
    # Sort the registers by id
    request.app.state.shared_state[ip]["registers"] = sorted(request.app.state.shared_state[ip]["registers"], key=lambda x: x["id"])

    return new_register
