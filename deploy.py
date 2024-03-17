import mlflow.sagemaker
from mlflow.deployments import get_deploy_client

endpoint_name ="production-endpoint"
model_uri="s3://mlflow-project2-stock-price-prediction/1/d4191373f6ad4ceab8874c5f2eb66b0e/artifacts/BaggingRegressor"

config = {
    "execution_role_arn":"arn:aws:iam::785685275217:role/anything-needed-for-mlflow-deployment",
    "bucket_name":"mlflow-project2-stock-price-prediction",
    "image_url":"785685275217.dkr.ecr.ap-northeast-2.amazonaws.com/bagging:2.11.1",
    "region_name":"ap-northeast-2",
    "archive":False,
    "instance_type":"ml.m5.xlarge",
    "instance_count":1,
    "synchronous":True
    }


client = get_deploy_client("sagemaker")

client.create_deployment(
name=endpoint_name,
    model_uri=model_uri,
    flavor="python_function",
    config=config,
)