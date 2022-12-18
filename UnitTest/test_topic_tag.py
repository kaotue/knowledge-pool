import unittest
import sys
import datetime
import dataclasses
import json
import pprint

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


def add_topic(topic):
    request = get_base_request()
    request['httpMethod'] = 'POST'
    request['path'] = '/v1/api/topics'
    request['body'] = json.dumps(topic.to_dict())
    response = app.lambda_handler(request, None)


class MyTestCase(unittest.TestCase):
    now: datetime.datetime = datetime.datetime.now()

    def test_tag(self):
        add_topic(kp_topic.KpTopic(**{'tag_1': 'a'}))
        add_topic(kp_topic.KpTopic(**{'tag_1': 'b', 'tag_2': 'b', 'tag_3': 'b'}))
        add_topic(kp_topic.KpTopic(**{'tag_1': 'b', 'tag_2': 'a', 'tag_3': 'c'}))

        # QUERY
        request = get_base_request()
        request['httpMethod'] = 'GET'
        request['path'] = '/v1/api/topics'
        request['queryStringParameters'] = {'tag': 'a'}
        response = app.lambda_handler(request, None)

        pprint.pprint(response)
        pprint.pprint(json.loads(response['body']))
        self.assertEqual(response['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()
