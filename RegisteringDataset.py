# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 17:00:21 2023

@author: acer
"""

from azureml.core import Workspace, Dataset, Datastore

ws = Workspace.from_config(path="./config")
az_store = Datastore.get(ws, "azure_sdk_blob_01")

csv_path = [(az_store, "./Loan Data/Loan Approval Prediction.csv")]

loan_dataset = Dataset.Tabular.from_delimited_files(path=csv_path)

loan_dataset = loan_dataset.register(ws, "Loan Dataset Azure SDK",
                                     description= "Loan application dataset",
                                     create_new_version= True)