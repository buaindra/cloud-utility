### Welcome to Cloud Utility
A python based cloud utility for multiple cloud providers under one CLI/API

### Supported Cloud Platform
1. Google Cloud Platform
	* Google Cloud Storage API

### Installation
```bash
pip install cloud_utility
```

### Prerequisite
1. Please make sure you have setup environment variable "GOOGLE_APPLICATION_CREDENTIALS" with the google service account json key inside your code
	```python
	import os
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/key.json"
	```
	
	```python
	from oauth2client.client import GoogleCredentials
	
	# Grab the application's default credentials from the environment.
    credentials = GoogleCredentials.get_application_default()
	```
	or, 
	explicitly set-up the environment variable:
		```bash
		export GOOGLE_APPLICATION_CREDENTIALS=key.json
		```
	
### How to use?
```python
from google_storage_utility import Google_Storage_Utility as gsu
a = gsu("<google-project-id>")
```
