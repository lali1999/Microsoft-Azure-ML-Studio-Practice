# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:37:09 2023

@author: acers
"""

# -----------------------------------------------------
# Importing required classes from Azureml.
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset


# -----------------------------------------------------
# Accessing  the Workspace, Datastore and Datasets.
# -----------------------------------------------------
ws                = Workspace.from_config("./config")
az_store          = Datastore.get(ws, 'azure_sdk_blob_01')
az_dataset        = Dataset.get_by_name(ws, 'Loan Applications Using SDK')
az_default_store  = ws.get_default_datastore()

# -----------------------------------------------------
# Uploading local files to storage
# -----------------------------------------------------

files_list = ["./data/test.csv", "./data/test2.csv"]

az_store.upload_files(files = files_list,
                      target_path="Loan Data/",
                      relative_root= "./data/",
                      overwrite = True)

# -----------------------------------------------------
# Uploading entire directory to Azure Storage
# -----------------------------------------------------

az_store.upload(src_dir="./data/",
                target_path="Loan Data/data",
                overwrite = True)