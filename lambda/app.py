import logging

# This is here because zappa and lambda really wants an end-point. The action is over in lambdametrics.py

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# @app.route('/', methods = ['GET', 'POST'])
def lambda_handler(event=None, context=None):
    logger.info('Lambda function invoked index()')

    return 'dummy endpoint hello'

if __name__ == '__main__':
    app.run(debug=True)


