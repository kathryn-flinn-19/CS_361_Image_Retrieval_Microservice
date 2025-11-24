import os
import random
from flask import Flask, request 

# checks if the topic exists in the image pool (i.e. if any of the image paths contain
# the topic) 
def topic_exists_in_pool(topic):
    path = "./image-microservice-image-pool"

    for img in os.listdir(path):
        if topic in img:
            return True
    
    return False


# chooses random image from the pool
def choose_random_image():
    images = []

    path = "./image-microservice-image-pool"

    for img in os.listdir(path):
        images.append(img)
    
    return random.choice(images)


# given that the topic exists in the image pool (must be predetermined before fxn is called),
# returns a random image from the pool with that topic
def choose_image_by_topic(topic):
    images_by_topic = []

    path = "./image-microservice-image-pool"

    # find all images with matching topic
    for img in os.listdir(path):
        if topic in img:
            images_by_topic.append(img)
    
    return random.choice(images_by_topic)


# the main function to call each time. checks if the topic exists and returns an image accordingly
def choose_image(topic):
    if topic == "random" or (not topic_exists_in_pool(topic)):
        return choose_random_image()
    else:
        return choose_image_by_topic(topic)
    
#Communication code:

app = Flask(__name__)

@app.route("/requestImage", methods = ["GET", "POST"])
def getImage():
    if(request.method == "GET"):
        return choose_image("random")
    elif(request.method == "POST"):
        return choose_image(
            request.get_json()["topic"]
        )
    return 1
        
if __name__ == "__main__":
    app.run(port=5209)