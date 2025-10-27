# Flask Leaflet Integration Example Code
# Additional Resources: https://leafletjs.com/ https://openmaptiles.org/

from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    submitted_coords = None
    if request.method == "POST":
        latitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        if latitude and longitude:
            submitted_coords = {"latitude": latitude, "longitude": longitude}
            print(f"Received coordinates from map: lat={latitude}, lng={longitude}")
        else:
            print("Form submitted without coordinates.")
    return render_template(
        "index.html",
        title="Leaflet Example",
        message="This is an example app for using Leaflet through Python Flask.",
        submitted_coords=submitted_coords,
    )

if __name__ == "__main__":
    app.run(debug=True, port=5001)
