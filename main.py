import json

from math import sqrt
from ai import get_advice

def calculate_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_direction(x, y, origin=(0, 0)):
    """Determine cardinal directions relative to the origin."""
    directions = []
    if y > origin[1]:
        directions.append("north")
    elif y < origin[1]:
        directions.append("south")
    if x > origin[0]:
        directions.append("east")
    elif x < origin[0]:
        directions.append("west")
    return " and ".join(directions)

def find_nearest_element(x, y, elements):
    """Find the nearest element to the given coordinates."""
    nearest = None
    min_distance = float("inf")
    for element in elements:
        ex, ey = element.get("data", {}).get("x", 0), element.get("data", {}).get("y", 0)
        if ex == x and ey == y:
            continue
        distance = calculate_distance(x, y, ex, ey)
        if distance < min_distance:
            min_distance = distance
            nearest = element
    return nearest, min_distance

def process_garden_data(json_data):
    """Generate positional phrases for each garden element."""
    scale = json_data.get("view", {}).get("scale", 1)  # Get scale from JSON
    origin_x, origin_y = 0, 0  # Define the origin as the center of the property or adjust as needed
    positional_phrases = []

    for element in json_data.get("elements", []):
        data = element.get("data", {})
        labels = data.get("labels", [])
        label = labels[0] if labels else "Unknown"
        x, y = data.get("x", 0), data.get("y", 0)
        width, height = data.get("width", 0), data.get("height", 0)

        # Convert coordinates to feet using the scale
        real_x = x * scale
        real_y = y * scale

        # Determine cardinal direction and position
        direction = get_direction(real_x, real_y, origin=(origin_x, origin_y))
        real_world_coords = f"{abs(real_x-origin_x):.1f} feet {'east' if real_x > origin_x else 'west'}, {abs(real_y-origin_y):.1f} feet {'north' if real_y > origin_y else 'south'}"

        # Find nearest element and distance
        nearest, distance = find_nearest_element(x, y, json_data["elements"])
        nearest_label = nearest.get("data", {}).get("labels", ["Unknown"])[0] if nearest and "labels" in nearest else None
        distance_in_feet = distance * scale
        nearby_info = f", approximately {distance_in_feet:.1f} feet from the {nearest_label}" if nearest_label else ""

        # Construct phrase
        phrase = (
            f"The {label} is located {real_world_coords} on the {direction} side of the property{nearby_info}."
        )
        positional_phrases.append(phrase)
    
    return positional_phrases


with open('save-data.json', 'r') as f:
    usda_zone = input(f"Which USDA zone are you?")

    json_data = json.load(f)

    phrases = process_garden_data(json_data)
    for phrase in phrases:
        print(phrase)

    advice = get_advice(",".join(phrases), usda_zone)
    print(advice)
