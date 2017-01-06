# lambda-metrics
Experiment to log CloudWatch metrics from a Lambda

I am trying to make a practical template for logging some metrics to CloudWatch
from a scheduled Lambda function

## Usage Notes
Start by setting up your virtual environment as venv. Use myvirtualenvsetup.sh to see how.

You can install the required packages with the command(s) in pipinstall.sh .

Assuming you have a working Role you can deploy the lambda with
`zappa deploy devops`

and update changes with
`zappa update devops`

and get rid of it with
`zappa undeploy devops`

You can follow the action with
`zappa tail devops`

The Flask and app.py are there purely for cargo cult reasons. We don't ever invoke that.

You can invoke the function from the command line (in the command line context) with e.g.
```
python -c "import lambdametrics; lambdametrics.send_random()"
```

## TODO

- Reduce logging (a lot)
- Improve handling of cases where load balancer could not get a reply from a real server
- Add "lambda_description" and "project_name" to zappa configuration
- Add some file exclusions to zappa configuration
- Clean out the app.py dummy file
- Got it to work with S3 Notifications, but should have a filter on keys. 
	Would be easy to do in the lambda itself, but I wonder if zappa can do this?
	Mostly looks like the filter should be in the lambda
- Consider separating out CloudWatchUtil (of course)
- Consider making the logfilter configurable with e.g. environment variables.
	Overall should probably consider configuration more carefully
- Add some exception handling. Esp if there is a useful way to notify datadog
- I'm keeping the pandas and numpy dependencies around for now despite everything
