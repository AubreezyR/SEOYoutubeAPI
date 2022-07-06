* Setup instructions (e.g. libraries to install, environment variables, etc.)
* How to run your code
* An overview of how your code works

**Libraries to install**
  * sqlalchemy
  * pandas
  * googleapiclient.discovery
  *IPython


**How to run code**
  * Get an api key from https://console.cloud.google.com
  * create a key.txt file with your api key
  * Run program
  * Follow requested imput from program

**How code works**

  My program gathers information from google's Youtube
  API by sending a GET request with the users API key and requested channel name
  It then takes the information and creates a table for the user to see
