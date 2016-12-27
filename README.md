# lambda-metrics
Experiment to log CloudWatch metrics from a Lambda

I am trying to make a practical template for logging some metrics to CloudWatch
from a scheduled Lambda function

Start by setting up your virtual environment as venv. Use myvirtualenvsetup.sh to see how.

You can install the required packages with the command(s) in pipinstall.sh .

Assuming you have a working Role you can deploy the lambda with
zappa deploy devops

and update changes with
zappa update devops

and get rid of it with
zappa undeploy devops

You can follow the action with
zappa tail devops

The Flask and app.py are there purely for cargo cult reasons. We don't ever invoke that.

You can invoke the function from the command line (in the command line context) with e.g.
python -c "import lambdametrics; lambdametrics.send_random()"
