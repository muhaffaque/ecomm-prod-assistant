import os
import pandas
from dotenv import load_dotenv
from typing import List
from langchain_core_documents import Document
from langchain_astradb import AstraDBVectoreStore
from product_assistant.utils.model_loader import ModelLoader
from product_assistant.utils.config_loader import load_config

class DataIngestion:
    """
    Class to handle data transformation and ingestion into AstraDB vector store
    """

    def __init__(self):
        pass

    def _load_env_variable(self):
        pass

    def _get_csv_path(self):
        pass

    def _load_csv(self):
        pass

    def transform_data(self):
        pass

    def store_in_vector_db(self):
        pass

    def run_pipeline(self):
        pass