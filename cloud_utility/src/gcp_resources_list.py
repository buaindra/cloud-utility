from google.oauth2 import service_account
import google.auth
from google.cloud import storage

class GCP_Resources(object):
    def __init__(self, project_id, credential_path=None):
        """
        project_id = google cloud project id
        credential_path = '/path/to/key.json'
        """
        self.project_id = project_id
        # json_acct_info = json.loads(function_to_get_json_creds())
        # credentials = service_account.Credentials.from_service_account_info(json_acct_info)
        if credential_path is not None:
            credentials = service_account.Credentials.from_service_account_file(credential_path)
            scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/cloud-platform'])
        else:
            credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
        #   credentials = GoogleCredentials.get_application_default()

        # credentials = service_account.Credentials.from_service_account_file(credential_path)
        self.storage_client = storage.Client(project=project_id, credentials=credentials)

    def all_resource_list(self):
        pass

    def list_buckets(self):
        bucket_list = []
        buckets = self.storage_client.list_buckets()
        for bucket in buckets:
            bucket_list.append(bucket.name)
        return bucket_list

    def list_blobs(self, bucket_name):
        blob_list = []
        blobs = self.storage_client.list_blobs(bucket_name)
        for blob in blobs:
            blob_list.append(blob.name)
        return blob_list




