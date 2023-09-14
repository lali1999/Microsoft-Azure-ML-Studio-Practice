# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 19:32:10 2023

@author: acer
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
# Loading the Azureml Dataset into the pandas dataframe.
# -----------------------------------------------------
df = az_dataset.to_pandas_dataframe()


# -----------------------------------------------------
# Uploading the dataframe to the azureml dataset
# -----------------------------------------------------
df_sub = df[["Married", "Gender", "Loan_Status"]]

az_ds_from_df = Dataset.Tabular.register_pandas_dataframe(
                dataframe=df_sub,
                target=az_store,
                name="Loan Dataset From Dataframe")
















