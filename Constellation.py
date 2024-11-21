from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

# Sample constellation data
constellations = [
    {'id': 1, 'name': 'Orion', 'hemisphere': 'Northern', 'main_stars': ['Betelgeuse', 'Rigel', 'Bellatrix'], 'area': 594, 'origin': 'Greek'},
    {'id': 2, 'name': 'Scorpius', 'hemisphere': 'Southern', 'main_stars': ['Antares', 'Shaula', 'Sargas'], 'area': 497, 'origin': 'Greek'},
    {'id': 3, 'name': 'Ursa Major', 'hemisphere': 'Northern', 'main_stars': ['Dubhe', 'Merak', 'Phecda'], 'area': 1280, 'origin': 'Greek'},
    {'id': 4, 'name': 'Cassiopeia', 'hemisphere': 'Northern', 'main_stars': ['Schedar', 'Caph', 'Ruchbah'], 'area': 598, 'origin': 'Greek'},
    {'id': 5, 'name': 'Crux', 'hemisphere': 'Southern', 'main_stars': ['Acrux', 'Mimosa', 'Gacrux'], 'area': 68, 'origin': 'Latin'},
    {'id': 6, 'name': 'Lyra', 'hemisphere': 'Northern', 'main_stars': ['Vega', 'Sheliak', 'Sulafat'], 'area': 286, 'origin': 'Greek'},
    {'id': 7, 'name': 'Aquarius', 'hemisphere': 'Southern', 'main_stars': ['Sadalsuud', 'Sadalmelik', 'Sadachbia'], 'area': 980, 'origin': 'Babylonian'},
    {'id': 8, 'name': 'Andromeda', 'hemisphere': 'Northern', 'main_stars': ['Alpheratz', 'Mirach', 'Almach'], 'area': 722, 'origin': 'Greek'},
    {'id': 9, 'name': 'Pegasus', 'hemisphere': 'Northern', 'main_stars': ['Markab', 'Scheat', 'Algenib'], 'area': 1121, 'origin': 'Greek'},
    {'id': 10, 'name': 'Sagittarius', 'hemisphere': 'Southern', 'main_stars': ['Kaus Australis', 'Nunki', 'Ascella'], 'area': 867, 'origin': 'Greek'}
]

# 1. View all constellations
@app.route('/constellations', methods=['GET'])
def get_all_constellations():
    return jsonify(constellations)

# 2. View a specific constellation by name
@app.route('/constellations/<name>', methods=['GET'])
def get_constellation(name): 
    constellation = next((c for c in constellations if c['name'].lower() == name.lower()), None)
    if constellation:
        return jsonify(constellation)
    else:
        return redirect(f'https://http.cat/404'), 404

# 3. Add a new constellation
@app.route('/constellations', methods=['POST'])
def add_constellation():
    new_constellation = request.get_json()
    new_constellation['id'] = len(constellations) + 1
    constellations.append(new_constellation)
    return jsonify(new_constellation), 201

# 4. Delete a constellation
@app.route('/constellations/<name>', methods=['DELETE'])
def delete_constellation(name):
    constellation = next((c for c in constellations if c['name'].lower() == name.lower()), None)
    if constellation:
        constellations.remove(constellation)
        return jsonify(constellation), 200
    else:
        return redirect(f'https://http.cat/404'), 404

# 5. Filter constellations by hemisphere and area (Query String)
@app.route('/constellations/filter', methods=['GET'])
def filter_constellations():
    hemisphere = request.args.get('hemisphere')
    area = request.args.get('area')
    filtered_constellations = constellations
    if hemisphere:
        filtered_constellations = [c for c in filtered_constellations if c['hemisphere'].lower() == hemisphere.lower()]
    if area:
        try:
            area_threshold = float(area)
            filtered_constellations = [c for c in filtered_constellations if c['area'] >= area_threshold]
        except ValueError:
            return redirect(f'https://http.cat/400'), 400

    return jsonify(filtered_constellations)

# 6. View the main stars of a constellation specified by name
@app.route('/constellations/<name>/main_stars', methods=['GET'])
def main_star(name):
    constellation = next((c for c in constellations if c['name'].lower() == name.lower()), None)
    if constellation:
        return jsonify(constellation['main_stars'])
    else:
        return redirect(f'https://http.cat/404'), 404

# 7. Partially update a constellation specified by name
@app.route('/constellations/<name>', methods=['PATCH'])
def update_star(name):
    constellation = next((c for c in constellations if c['name'].lower() == name.lower()), None)
    if constellation:
        data = request.get_json()
        if 'area' in data:
            constellation['area'] = data['area']
        if 'hemisphere' in data:
            constellation['hemisphere'] = data['hemisphere']
        return jsonify(constellation), 200
    else:
        return redirect(f'https://http.cat/404'), 404
# 8. For a constellation specified by name, view the image
# You might have to use an image generator API - try https://imagepig.com/

# 9. Add your own! Try to use query strings or path parameters.

# 10. Double check that all the endpoints return the appropriate status codes.
# For errors, display the status code using an HTTP Cat - https://http.cat/

if __name__ == '__main__':
    app.run(debug=True)