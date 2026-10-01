from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

next_id = 3

def find_event(event_id):
    #Helper: return the Event with this id, or None if not found.
    for event in events:
        if event.id == event_id:
            return event
    return None

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    global next_id
    data = request.get_json(silent=True)
 
    # TODO: Task 3 - Implement the Loop and Process Each Element
    if not data or not data.get("title"):
        return jsonify({"error": "Missing required field: title"}), 400

    # TODO: Task 4 - Return and Handle Results
    new_event = Event(next_id, data["title"])
    events.append(new_event)
    next_id += 1
    return jsonify(new_event.to_dict()), 201


# TODO: Task 1 - Define the Problem 
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event = find_event(event_id)
    if event is None:
        return jsonify({"error": f"Event with id {event_id} not found"}), 404
    # TODO: Task 3 - Implement the Loop and Process Each Element
    data = request.get_json(silent=True)
    if not data or not data.get("title"):
        return jsonify({"error": "Missing required field: title"}), 400
    # TODO: Task 4 - Return and Handle Results
    event.title = data["title"]
    return jsonify(event.to_dict()), 200

# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event = find_event(event_id)
    # TODO: Task 3 - Implement the Loop and Process Each Element
    if event is None:
            return jsonify({"error": f"Event with id {event_id} not found"}), 404
    # TODO: Task 4 - Return and Handle Results
    events.remove(event)
    return "", 204

if __name__ == "__main__":
    app.run(debug=True)