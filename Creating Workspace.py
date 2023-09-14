# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:06:35 2023

@author: acer
"""

from azureml.core import Workspace

ws = Workspace.create(name = 'myworkspace',
                      subscription_id= '9d99d193-c40a-4065-a70f-dc3c40c2a8e0',
                      resource_group= 'AzureMLSDK_RG_01',
                      create_resource_group= True,
                      location= 'eastus')

ws.write_config(path="./config")