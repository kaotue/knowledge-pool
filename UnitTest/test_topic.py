import unittest
import sys
import datetime
import dataclasses
import json

sys.path.append('../src')
from src import app, kp_topic


def get_base_request():
    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
        },
        "pathParameters": {"proxy": "accounts/self"},
        "httpMethod": "GET",
        "path": "/v1/api/topics",
    }


class MyTestCase(unittest.TestCase):
    now: datetime.datetime = datetime.datetime.now()

    def test_post_and_get(self):
        # post
        request = get_base_request()
        request['httpMethod'] = 'POST'
        request['path'] = '/v1/api/topics'

        topic = kp_topic.KpTopic()
        topic.type = '1'
        topic.q = 'value_q'
        topic.a = 'value_a'
        topic.is_public = '1'
        topic.tags = 'tags'

        request['body'] = json.dumps(dataclasses.asdict(topic))
        response = app.lambda_handler(request, '')

        self.assertEqual(response['statusCode'], 200)
        new_topic_id = json.loads(response['body']).get('result')
        self.assertIsNotNone(new_topic_id)


        # GET
        request = get_base_request()
        request['httpMethod'] = 'GET'
        request['path'] = f'/v1/api/topics/{new_topic_id}'

        response = app.lambda_handler(request, '')

        self.assertEqual(response['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()
