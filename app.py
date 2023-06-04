from flask import Flask, request, jsonify
from recommender import recommend_destination

app = Flask(__name__)
@app.route('/recommend', methods=['POST'])
def recommend():
    json_data = request.get_json()
    starting_point = json_data['startingPoint']
    distance_types = json_data['distanceTypes']
    difficulty = json_data['difficulty']
    scenery = json_data['scenery']
    
    route_coordinates, distance, duration, name = recommend_destination(starting_point, distance_types, difficulty, scenery)
    coordinates_list = [coord.replace('[', '').replace(']', '') for coord in route_coordinates]
    coordinates_list = [coord.replace('),', ');') for coord in coordinates_list]
    coordinates_list = [coord.replace(')', '').replace('(', '') for coord in coordinates_list]

    response = []
    for i in range(len(route_coordinates)):
        route_data = {
            'distance': distance[i],
            'duration': duration[i],
            'routeCoordinates': coordinates_list[i],
            'routeName': name[i]
        }
        response.append(route_data)

    return jsonify(response)
    
if __name__ == '__main__':
    app.run(debug=True)