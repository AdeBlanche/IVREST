from fastapi import APIRouter, Request
from helpers import get_ip

router = APIRouter()
       

@router.get("/missions", summary="Retrieve missions", tags=["Missions"])
def get_missions(request: Request):
    ip = get_ip(request)

    return request.app.state.shared_state[ip]["missions"]

