from networksecurity.components.data_ingestion import DataIngestion

from networksecurity.exceptation.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig , TrainingPipelineConfig



from networksecurity.entity.artifact_entity import DataValidationArtifact , DataIngestionArtifact
from networksecurity.components.data_validation import DataValidation 


 

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Initiate the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
        
        datavalidationconfig= DataValidationConfig(trainingpipelineconfig)
        datavalidation=DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the data Validation")
        data_validation_artifact= datavalidation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)


        
    except Exception as e:
           raise NetworkSecurityException(e,sys)