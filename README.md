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
1. Create and activate the virtual env first in Cloud-Shell/VM Instance
   ```bash
   # if pip not installed
   
   # install virtual env in
   python3 -m pip install virtualenv
   
   # create virtual environment
   python3 -m venv .env --system-site-packages
   
   # activate the virtual environment in unix/debian/linux
   source .env/bin/activate
   ```
2. Install the package from pypi
	```bash
	pip install cloud-utility
	```
 
3. Create Service Account on Google Cloud IAM
	```bash
   	gcloud config set project <project-id>
  	gcloud iam service-accounts create <service-account-name> --description="sa to access google apis" --display-name="cloud utility service-account"
 	```
 
4. Provide the role to that service account
   (*Note: Make sure you have "roles/iam.serviceAccountAdmin" permission)
	```bash
	gcloud projects add-iam-policy-binding <PROJECT_ID> --member="serviceAccount:<SERVICE_ACCOUNT_Name>@<PROJECT_ID>.iam.gserviceaccount.com" --role="roles/storage.admin"
 	```
 
5. Download the private key of the service account
   ```bash
   gcloud iam service-accounts keys create sa_key.json --iam-account=<my-iam-account>@<project-id>.iam.gserviceaccount.com --key-file-type="json"
   ```
6. Use Google_Storage_Utility (sample code snippet):
   1. Import Google_Storage_Utility
	```python
	#import the module
	from google_storage_utility import Google_Storage_Utility as gsu
	```
 	2. Initiate the obj of Google_Storage_Utility
	```python
	# initiate the obj of Google_Storage_Utility with project_id and credential_path
	storage_obj = gsu(project_id="<project-id>", credential_path="/home/sub-dir/sa_key.json")
	
	# initiate the obj of Google_Storage_Utility with project_id without credential key path
	storage_obj = gsu(project_id="<project-id>")
 	```
	
	3. Create gcs buckets
	```python
	# create new bucket with default options, will return bucket name
	out = storage_obj.gcp_create_bucket("<bucket name>") 
	
	# create new bucket with storage_class, location
	out = storage_obj.gcp_create_bucket("<bucket name>", storage_class="COLDLINE", location="us-east1") 
	```
 	
	4. List of buckets/prefixes/blobs:
	```python
	# get list of buckets
	out = storage_obj.gcp_list_buckets()
	print(f"buckets: {out}")

	# get list of prefix with levels and blobs
	out = storage_obj.gcp_blob_all_list("coherent-coder-346704")
	print(f"prefix: {out[0]}")
	print(f"blobs: {out[1]}")
	print(f"total blobs count: {len(out[1])}")
	```
