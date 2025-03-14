from fastapi import Request

shared_state = {"base": {"state": 4}} # import this in the *_routers, user is saved based on ip.

def get_ip(request: Request):
    ip = request.headers.get("X-Forwarded-For", request.client.host).split(",")[0]
    shared_state = request.app.state.shared_state

    if not ip in shared_state:
        # Initialize this user
        shared_state[ip] = create_state()

    return ip





def create_state():
    return {
        "id" : "test",
        "missions": [
            {
                "guid": "b37eb3f1-bc82-11ef-b8ff-b46921171448",
                "url": "/v2.0.0/missions/b37eb3f1-bc82-11ef-b8ff-b46921171448",
                "name": "test"
            },
            {
                "guid": "2925dfad-bd23-11ef-9152-b46921171448",
                "url": "/v2.0.0/missions/2925dfad-bd23-11ef-9152-b46921171448",
                "name": "Missions of group C11"
            },
            {
                "guid": "1b8d7f05-bd25-11ef-9152-b46921171448",
                "url": "/v2.0.0/missions/1b8d7f05-bd25-11ef-9152-b46921171448",
                "name": "Mission37"
            },
            {
                "guid": "77b5c6ac-bd25-11ef-9152-b46921171448",
                "url": "/v2.0.0/missions/77b5c6ac-bd25-11ef-9152-b46921171448",
                "name": "Missions_Group_9"
            },
            {
                "guid": "97e9467c-bd26-11ef-9152-b46921171448",
                "url": "/v2.0.0/missions/97e9467c-bd26-11ef-9152-b46921171448",
                "name": "MH_GROUP_5"
            }
        ],
        "mission_queue": [
            {
                "id": 1,
                "guid": "b37eb3f1-bc82-11ef-b8ff-b46921171448",
                "url": "/v2.0.0/mission_queue/1",
                "state": "Aborted"
            },
            {
                "id": 2,
                "guid": "2925dfad-bd23-11ef-9152-b46921171448",
                "url": "/v2.0.0/mission_queue/2",
                "state": "Aborted"
            },
            {
                "id": 3,
                "guid": "1b8d7f05-bd25-11ef-9152-b46921171448",
                "url": "/v2.0.0/mission_queue/3",
                "state": "Aborted"
            },
        ],
        "status" : {
            "position": {
                "x": 19.59588050842285,
                "y": 9.746625900268555,
                "orientation": -14.020983695983887
            },
            "velocity": {
                "linear": 0,
                "angular": 0
            },
            "battery_time_remaining": 6598,
            "battery_percentage": 13.699999809265137,
            "moved": 6448.71,
            "mission_queue_id": "null",
            "mission_queue_url": "null",
            "mission_text": "Cameras are ready to stream",
            "distance_to_next_target": 0,
            "robot_name": "MiRanda",
            "robot_model": "MiR200",
            "serial_number": "",
            "session_id": "d17c9c55-7c9e-11ef-95eb-94c691a738d4",
            "state_id": 4,
            "state_text": "Pause",
            "mode_id": 7,
            "mode_text": "Mission",
            "joystick_web_session_id": "",
            "map_id": "427f263f-977d-11ef-b1a9-b46921171448",
            "unloaded_map_changes": "false",
            "safety_system_muted": "false",
            "joystick_low_speed_mode_enabled": "false",
            "mode_key_state": "idle",
            "uptime": 2383,
            "errors": "[]",
            "footprint": "[[0.6,-0.52],[0.6,0.52],[-0.6,0.52],[-0.6,-0.52]]",
            "user_prompt": "null",
            "allowed_methods": "null"
        },
        "registers" : [
            {
                "id": 1,
                "url": "/v2.0.0/registers/1",
                "value": 0,
                "label": "string"
            },
            {
                "id": 2,
                "url": "/v2.0.0/registers/2",
                "value": 0,
                "label": "PLC Register 2"
            },
            {
                "id": 3,
                "url": "/v2.0.0/registers/3",
                "value": 11,
                "label": "PLC Register 3"
            },
            {
                "id": 4,
                "url": "/v2.0.0/registers/4",
                "value": 0,
                "label": "hello"
            },
            {
                "id": 5,
                "url": "/v2.0.0/registers/5",
                "value": 0,
                "label": "PLC Register 5"
            },
            {
                "id": 6,
                "url": "/v2.0.0/registers/6",
                "value": 4,
                "label": "PLC Register 6"
            },
            {
                "id": 7,
                "url": "/v2.0.0/registers/7",
                "value": 0,
                "label": ""
            },
            {
                "id": 8,
                "url": "/v2.0.0/registers/8",
                "value": 0,
                "label": ""
            },
            {
                "id": 9,
                "url": "/v2.0.0/registers/9",
                "value": 0,
                "label": ""
            },
            {
                "id": 10,
                "url": "/v2.0.0/registers/10",
                "value": 0,
                "label": ""
            },
        ]
    }
