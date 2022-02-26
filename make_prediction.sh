#!/usr/bin/env bash

PORT=8000
echo "Port: $PORT"

# POST method predict
curl -d '{  
   "F1":{  
      "0":0
   },
   "F2":{  
      "0":6.575
   },
   "F3":{  
      "0":296.0
   },
   "F4":{  
      "0":15.3
   },
   "F5":{  
      "0":396.9
   },
   "F6":{  
      "0":4.98
   },
   "F7":{  
      "0":4.98
   },
   "F8":{  
      "0":4.98
   },
   "F9":{  
      "0":4.98
   },
   "F10":{  
      "0":4.98
   },
   "F11":{  
      "0":4.98
   },
   "F12":{  
      "0":4.98
   },
   "F13":{  
      "0":4.98
   }
}'\
     -H "Content-Type: application/json" \
     -X POST http://localhost:$PORT/predict
