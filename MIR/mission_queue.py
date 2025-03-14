from fastapi import APIRouter, Body, Path, Query, Request
from helpers import create_state, get_ip
from pydantic import BaseModel
from typing import List, Optional
import json

router = APIRouter()

# Define a Pydantic model for the payload
class MissionQueue(BaseModel):
    mission_id: str = None
    message: Optional[str] = None
    parameters: Optional[dict] = None
    priority: Optional[int] = None
    fleet_schedule_guid: Optional[str] = None
    description: Optional[str] = None
       
@router.get("/mission_queue", summary="GET /mission_queue", tags=["Mission_queue"])
def get_mission_queue(request: Request):
    shared_state = request.app.state.shared_state
    
    ip = get_ip(request)

    return shared_state[ip]["mission_queue"]



@router.post("/mission_queue", summary="POST /mission_queue", tags=["Mission_queue"])
def update_mission_queue(request: Request,
        mission: MissionQueue = Body(..., description="The details of the mission_queues"),
    ):
    shared_state = request.app.state.shared_state
    ip = get_ip(request) 
    mission_id_number = 0
    
    # First check so it doesnt already exist in the queue
    for i, data in enumerate(request.app.state.shared_state[ip]["mission_queue"]):
        if mission.mission_id == data["guid"]:
            del request.app.state.shared_state[ip]["mission_queue"][i]

    for data in request.app.state.shared_state[ip]["mission_queue"]:
        if mission.mission_id == data["guid"]:
            # it exists so just give a positive response
            return data
   
    # Find the mission with the mission_id and add it to the queue.
    for data in request.app.state.shared_state[ip]["missions"]:
        if mission.mission_id == data["guid"]:
            #data.status = "Queued"
            print(data)
            data["state"] = "Queued"
            data["id"] = len(request.app.state.shared_state[ip]["mission_queue"]) + 1 # List does not start at 0.
            data["url"] = "/v2.0.0/mission_queue/" + str(data["id"])
            del data["name"]
            request.app.state.shared_state[ip]["mission_queue"].append(data)
            return data

    # Not found and not added so just return an empty object.
    return {}

@router.delete("/mission_queue", summary="DELETE /mission_queue", tags=["Mission_queue"])
def delete_mission_queue(request: Request):
    shared_state = request.app.state.shared_state
    ip = get_ip(request)
    
    # Clear the mission queue
    shared_state[ip]["mission_queue"] = []
    
    return shared_state[ip]["mission_queue"]
