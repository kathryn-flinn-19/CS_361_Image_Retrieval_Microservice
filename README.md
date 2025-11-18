# CS_361_Image_Retrieval_Microservice

Communication contract:

A. Requesting data from the microservice:
- Send a GET request to localhost:5000/requestImage to get a random image path

    Example (python):

          import requests
          response = request.get("localhost:5000/requestImage")
  
- Send a POST request with a JSON object specifying the image topic to localhost:5000/requestImage to get an image path of a specific topic

    Example  (python):
  
          import requests
          import json
          response = request.post("localhost:5000/requestImage", json={"topic": "dog"})

B. Receiving data from the microservice:
- After sending a GET request as shown above, the response will be stored in response so it can be used later. We can access the image path like so:
      Example (python):
  
        import requests
        import json
        response = request.get("localhost:5000/requestImage")
        path = (json.loads(response.json()))["path"]
        print(path)      
  
- After sending a POST request as shown above, we can get the response and access the image path as was shown in the GET example:
      Example (python):
  
        import requests
        import json
        response = request.post("localhost:5000/requestImage", json={"topic": "dog"})
        path = (json.loads(response.json()))["path"]
        print(path)

C. UML Sequence Diagram:
<img width="1438" height="1165" alt="Screenshot 2025-11-17 111739" src="https://github.com/user-attachments/assets/04e5ed52-2654-4551-ab72-0cc868bbda9f" />
