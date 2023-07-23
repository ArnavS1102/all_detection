import boto3
import sagemaker

from sagemaker import get_execution_role
from sagemaker.pytorch import PyTorchModel

class SAM:
    def __init__(self):
        

