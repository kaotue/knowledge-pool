import os
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
import logic_get_topic
import logic_post_topic
import logic_put_topic
import logic_get_user
import logic_post_user
import logic_put_user

ROOT_PATH = f"/{os.environ.get('API_VERSION', 'v1')}/api"
app = APIGatewayRestResolver()


@app.get(f'{ROOT_PATH}/topics/<id>')
def get_topic(id: str):
    return logic_get_topic.run(id)


@app.post(f'{ROOT_PATH}/topics')
def post_topic():
    return logic_post_topic.run(
        body=app.current_event.json_body,
        login_user_id='kaotue'
    )


@app.put(f'{ROOT_PATH}/topics/<id>')
def put_topic(id: str):
    return logic_put_topic.run(
        body=app.current_event.json_body,
        topic_id=id,
        login_user_id='kaotue',
    )


@app.get(f'{ROOT_PATH}/users/<id>')
def get_user(id: str):
    return logic_get_user.run(id)


@app.post(f'{ROOT_PATH}/users')
def post_user():
    return logic_post_user.run(
        body=app.current_event.json_body,
        user_id='kaotue',
        login_user_id='kaotue'
    )


@app.put(f'{ROOT_PATH}/users/<id>')
def put_topic(id: str):
    return logic_put_user.run(
        body=app.current_event.json_body,
        user_id=id,
        login_user_id='kaotue',
    )


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
