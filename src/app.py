import os
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
import logic_post_topic
import logic_get_topic

ROOT_PATH = f"/{os.environ.get('API_VERSION', 'v1')}/api"
app = APIGatewayRestResolver()


@app.post(f'{ROOT_PATH}/topics')
def post_topic():
    return logic_post_topic.run(
        body=app.current_event.json_body,
        user_id='kaotue'
    )


@app.get(f'{ROOT_PATH}/topics/<id>')
def get_topic(id: str):
    return logic_get_topic.run(id)


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
