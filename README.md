### Welcome to Cloud Utility
A python based cloud utility for multiple cloud providers under one CLI/API

### Supported Cloud Platform
1. Google Cloud Platform

### Installation
```bash
pip install cloud_utility
```

### Python API
##### Example usage
```python
from google_storage_utility import Google_Storage_Utility as gsu
a = gsu("<google-project-id>")
```

### Errors Handling:
1. google.auth.exceptions.DefaultCredentialsError: Could not automatically determine credentials. Please set GOOGLE_APPLICATION_CREDENTIALS or explicitly create credent
ials and re-run the application. For more information, please see https://cloud.google.com/docs/authentication/getting-started
	* Please make sure you have setup environment variable "GOOGLE_APPLICATION_CREDENTIALS" with the google service account json key