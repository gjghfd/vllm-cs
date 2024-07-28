import os
import sys
sys.path.append('/code/python')

from modelscope.hub.api import HubApi
from modelscope.hub.snapshot_download import snapshot_download

def handler(event, context):
    model_id = os.getenv('MODEL_ID', '')
    revision = os.getenv('MODEL_VERSION', '')
    cache_dir = os.getenv('MODELSCOPE_CACHE', '')
    sdk_token = os.getenv('MODELSCOPE_TOKEN', '')
    # login first.
    HubApi().login(sdk_token)
    if revision == "latest":
        revision = ""
    if len(revision) > 0:
        snapshot_download (model_id =model_id, 
                           revision =revision,
                           cache_dir = cache_dir)
    else:
         snapshot_download (model_id =model_id, 
                            cache_dir = cache_dir)
    print("download model scuccess!")
