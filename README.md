# Search Location App

A Python desktop application built using Tkinter that allows users to search for any location, open it in Google Maps, and calculate the distance from their current location to the searched place.  

---

## Features
- Simple Tkinter GUI for easy use  
- Get approximate current location using IP geolocation  
- Search any location and open it directly on Google Maps  
- Calculates distance between current and searched location using geodesic formula  

---

## Requirements

Make sure you have:
- Python 3.8 or higher  
- pip (Python package manager)

Required Python libraries:
- `tkinter` (usually included with Python)
- `geopy`
- `geocoder`
- `requests`

You can install them with:

pip install geopy geocoder requests
Or use a requirements.txt file:

nginx
Copy code
geopy
geocoder
requests
Installation (Step-by-Step)
Clone the repository

bash
Copy code
git clone https://github.com/<your-username>/Search-Location-App.git
cd Search-Location-App
Create a virtual environment (recommended)

bash
Copy code
python -m venv venv
Activate the virtual environment

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS/Linux:

bash
Copy code
source venv/bin/activate
Install project dependencies

bash
Copy code
pip install -r requirements.txt
or manually:

bash
Copy code
pip install geopy geocoder requests
Run the application

bash
Copy code
python app.py
(Replace app.py with your actual main file name if it’s different.)

Folder Structure
arduino
Copy code
Search-Location-App/
├─ app.py                 # main script file
├─ requirements.txt
├─ README.md
└─ assets/                # optional: screenshots or icons
Notes
If tkinter is not installed, run:
Ubuntu/Debian: sudo apt-get install python3-tk

For accurate results, ensure your internet connection is active (needed for IP and geocoding services).

Works best with stable network for location retrieval and map loading.

License
This project is released under the MIT License.

Author
Vyshnavi Garlapati
Search Location App – Python Tkinter Project
