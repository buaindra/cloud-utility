from google_storage_utility import Google_Storage_Utility as gsu

class GCP_Resources(object):
    def __init__(self, project_id, credential):
        self.project_id = project_id
        self.storage_obj = gsu(project_id=project_id, credential=credential)

    def all_resource_list(self):
        pass


