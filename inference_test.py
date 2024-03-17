from data import x_test, y_test
import boto3
import json


endpoint_name = "production-endpoint"
region = "ap-northeast-2"

sm = boto3.client("sagemaker", region_name=region)
smrt = boto3.client("runtime.sagemaker", region_name=region)


test_data_json = json.dumps({"instances": x_test.tolist()})


prediction = smrt.invoke_endpoint(
    EndpointName=endpoint_name,
    Body=test_data_json,
    ContentType="application/json"
)

prediction = prediction['Body'].read().decode("ascii")

print(prediction)