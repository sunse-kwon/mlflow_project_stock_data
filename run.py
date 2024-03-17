import mlflow

experiment_name = "Bagging Regressor project"
entry_point = "Bagging"

mlflow.set_tracking_uri(
    # 'http://127.0.0.1:5000'
    # 'http://ec2-13-124-18-48.ap-northeast-2.compute.amazonaws.com:5000/'
    'http://ec2-13-124-158-12.ap-northeast-2.compute.amazonaws.com:5000/'
)

# import pdb; pdb.set_trace()
mlflow.projects.run(

    uri='.',
    experiment_name=experiment_name,
    entry_point=entry_point,
    env_manager='conda'
)
