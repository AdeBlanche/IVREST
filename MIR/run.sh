#!/bin/bash
URL=193.10.203.23
PORT=8000

echo ""
echo URL:     http://$URL:$PORT 
echo Swagger: http://$URL:$PORT/docs 
echo Redoc:   http://$URL:$PORT/redoc 
echo ""
python3.9 -m uvicorn app:app --host $URL --port $PORT --reload


