# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:06:23 2023

@author: acer
"""

from azureml.core import Workspace, Datastore, Dataset

ws = Workspace.from_config(path="./config")

#listing all the workspaces withing the subscription.
ws_list = Workspace.list(subscription_id='9d99d193-c40a-4065-a70f-dc3c40c2a8e0')

ws_list = list(ws_list)

#accessing the default datastore.

az_default = ws.get_default_datastore()

#listing all datastores

store_list = list(ws.datastores)

#get the dataset by name

az_dataset = Dataset.get_by_name(ws, "Loan application by SDK")

#list all the datasets

ds_list = list(ws.datasets.keys())

for items in ds_list:
    print(items)