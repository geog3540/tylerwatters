import json

# Open the GeoJSON file
with open('conusFile.geojson') as file:
    data = json.load(file)

# Iterate over the features and update the fields
for feature in data['features']:
    feature['properties']['STATEFP'] = int(feature['properties']['STATEFP'])
    feature['properties']['GEOID'] = int(feature['properties']['GEOID'])

# Write the updated GeoJSON to a new file
with open('conusFileCorrected.geojson', 'w') as file:
    json.dump(data, file)
