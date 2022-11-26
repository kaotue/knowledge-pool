import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from usecases import get_topic
from usecases import post_topic

ROOT_PATH = f"/{os.environ.get('API_VERSION', 'v1')}/api"
app = APIGatewayRestResolver()


@app.get(f'{ROOT_PATH}/topics/new')
def post_topic():
    return post_topic.run(
        body=app.current_event.json_body,
        user_id=''
    )


@app.get(f'{ROOT_PATH}/topics/<id>')
def get_topic(id: str):
    return get_topic.run(id)


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
