import sagemaker
from pprint import pprint
import sys

role = sagemaker.get_execution_role()
session = sagemaker.Session()

account = session.boto_session.client("sts").get_caller_identity()["Account"]
region = session.boto_session.region_name
#imagename = sys.argv[1]
#image = account + ".dkr.ecr." + region + ".amazonaws.com/" + imagename
image = sys.argv[1]
print image
print "Starting Training..."

model = sagemaker.estimator.Estimator(
    image_name=image,
    role=role,
    train_instance_count=int(sys.argv[2]),
    train_instance_type=sys.argv[3],
    sagemaker_session=session,
)

pprint(vars(model))
model.fit()
pprint(vars(model))

print "Deploying the model..."

predictor = model.deploy(int(sys.argv[4]), sys.argv[5], endpoint_name=sys.argv[6])
