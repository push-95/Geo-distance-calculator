# Python Backend Assignment

## Description
**Distance Calculator** is a web application built with Flask and python to calculate the geodesic distance between two points on the surface of the earth (there’s Mars in Texas) - which is, in other terms, specified by addresses (or mathematically, geographic coordinates). The app provides user with test boxes for two address entries, the distance between which you wish to calculate, and one for the API key (to make sure you're not a robot, JK). 

## Structure
```
imbellus
│   README.md
│   requirements.txt
│   app.py
│   dist_calc.py
│   test_dist_calc.py
│   PythonBackendAssignment.pdf
└───static
│   │   map.jpg 
└───templates
    │   calc.html
```

## Execution
All required packages will be installed by running:
```sh
$ pip install -r requirements.txt
```
You will need the API key to run, instructions to generate a key can be found at: `https://support.google.com/googleapi/answer/6158862?hl=en`

To run the web app:
```sh
$ python app.py
```
Then go to `http://localhost:5001/` on your web browser

To run the automated tests:
```sh
$ python test_dist_calc.py
```

## Technical Challenges

 - User Interface -- It is an integral part of any application. The current version of the app is very basic and although not a technical challenge per se, creating a better app design for better user experience requires more heuristic evaluation and consequently code.
 - Scalability -- When the app is deployed, load balancing between servers is critical in a multithreaded scenario. The architecture should give enough flexibility to change easily.
 - Performance -- After scaling to a larger audience or users, poor or unoptimised databases would result in delays while getting a response. Especially, when there are image or video files to be obtained with the responses, possibly in the next version of the app.
 - Security -- Web application security is another aspect that needs to be taken care of, such as denial of service attacks, safety of user data, database malfunctioning, unauthorized access to restricted parts of the website, etc. In the current case, the API key is used to authenticate user and the HTTP request to the geocoding API.
 - Cross-platform operation -- a web application should be robust enough to run satisfactorily run on different browsers and operating systems.

## Client-Server Interaction

A request to this app typically goes through the following process:
 - Local Processing: Browser extracts the "scheme"/protocol (http), host (www.localhost), and port number (:5001), (optional) resource path, and query strings that are specified in the form <protocol>://<host><:optional port>/<path/to/resource><?query>. In this case: http://localhost:5001
 - A click on the "Calculate Distance" button will trigger the browser to open a TCP connection to the IP address of localhost:5001 and here we need to send data to the server in the body of the request, so a HTTP POST request is sent.
 - With the entries in the text boxes on the webpage, corresponding objects of class Geocode (in dist_calc.py) are created. 
 - When the calc_dist() method is called, the google geocode API is queried via the geocode() method.
 - Geocoding sample request : https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY (for latitude/longitude lookup). This request consists of the url to https://maps.googleapis.com/maps/api/geocode/json? and additional parameters (address- 1600 Amphitheatre Parkway...) 
 - Response to the above request is a json file containing the actual address, latitude, longitude information, after API key authentication passes.
 - Once the response from the geocode endpoint is received, the json input is accordingly converted to the necessary (readable) format.
 - When the browser gets this response, it is rendered on the screen. The HTTP request is now done, and the TCP connection is closed.
 - A click on "Calculate Distance" will send a new request to the server.
 
## Why the problem is interesting

This part, in my opinion, deserves to be at the very end because what I found the most crucial all through developing this simple app is the learning outcome -- which is a product of trying to understand and analyse the possible technical challenges, flow of control through the process and the actual code for getting the app to work. A major reason why this problem is interesting is the underlying technologies that it employs in the solution. The hourglass-network stack model, IP sockets, HTTP client and web server interaction models and google geocode API were the highlights of the learning involved to solve this problem.