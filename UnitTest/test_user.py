import unittest
import sys
import datetime
import dataclasses
import json
import pprint

sys.path.append('../src')
from src import app, kp_user


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
        "path": "/v1/api/users",
    }


class MyTestCase(unittest.TestCase):
    now: datetime.datetime = datetime.datetime.now()

    def test_post_and_get_user(self):
        # POST
        request = get_base_request()
        request['httpMethod'] = 'POST'
        request['path'] = '/v1/api/users'

        user = kp_user.KpUser()
        user.name = 'test_user'

        request['body'] = json.dumps(user.to_dict())
        response = app.lambda_handler(request, None)

        self.assertEqual(response['statusCode'], 200)
        new_user_id = json.loads(response['body']).get('result')
        self.assertIsNotNone(new_user_id)

        # GET
        request = get_base_request()
        request['httpMethod'] = 'GET'
        request['path'] = f'/v1/api/users/{new_user_id}'

        response = app.lambda_handler(request, None)

        pprint.pprint(response)
        pprint.pprint(json.loads(response['body']))

        self.assertEqual(response['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()
