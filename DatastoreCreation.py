# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:44:57 2023

@author: acer
"""

from azureml.core import Workspace, Datastore

ws = Workspace.from_config(path="./config")

az_store = Datastore.register_azure_blob_container(workspace = ws,
                                                   datastore_name = "azure_sdk_blob_01",
                                                   container_name = "azuremlstb01blob",
                                                   account_name = "azuremlstb01",
                                                   account_key= "1hjdlWBM1oZU3BW0cc0q+YzHgEldkjGCrdTIbRALf2dqhtx3/I9yaZWPcUcTrR4uz4b0OL7TJUBu+AStKCGqYA==") 