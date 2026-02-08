from huggingface_hub.utils import RepositoryNotFoundError, HfHubHTTPError
from huggingface_hub import HfApi, create_repo
from google.colab import userdata
import os


repo_id = "bxpradhan/PIMA-Diabetes-Prediction"                         # enter the Hugging Face username here
repo_type = "dataset"

# Initialize API client
#api = HfApi(token=os.getenv("HF_TOKEN"))
api = HfApi(token=userdata.get('HF_Token'))

# Step 1: Check if the space exists
try:
    api.repo_info(repo_id=repo_id, repo_type=repo_type)
    print(f"Space '{repo_id}' already exists. Using it.")
except RepositoryNotFoundError:
    print(f"Space '{repo_id}' not found. Creating new space...")
    create_repo(repo_id=repo_id, repo_type=repo_type, private=False)
    print(f"Space '{repo_id}' created.")

# Debugging: Check if the folder_path is a directory before uploading
folder_to_upload = "self_paced_courses_1_mlops/data"
if not os.path.isdir(folder_to_upload):
    print(f"Error: The path '{folder_to_upload}' is not a directory or does not exist.")
else:
    print(f"Path '{folder_to_upload}' is a valid directory. Proceeding with upload.")

api.upload_folder(
    folder_path=folder_to_upload,
    repo_id=repo_id,
    repo_type=repo_type,
)
