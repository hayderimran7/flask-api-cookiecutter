import json
import logging
import unittest

from {{cookiecutter.app_name}} import app


class APITestCases(unittest.TestCase):
    def setUp(self) -> None:
        logging.info("Setting up test cases.")
        self.app = app

    def tearDown(self) -> None:
        logging.info("Tearing down test cases.")

    def test_name(self) -> None:
        data = "HelloWorld"

        with self.app.test_client() as c:
            r = c.get(f"/{data}")

        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.loads(r.data), {"name": data})
        self.assertEqual(json.loads(r.data)["name"], data)

    def test_name_with_spaces(self) -> None:
        data = "Hello, World"

        with self.app.test_client() as c:
            r = c.get(f"/{data}")

        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.loads(r.data), {"name": data})
        self.assertEqual(json.loads(r.data)["name"], data)

    def test_name_with_emoji(self) -> None:
        data = "Hello from Singapore 😀🇸🇬"

        with self.app.test_client() as c:
            r = c.get(f"/{data}")

        self.assertEqual(r.status_code, 200)
        self.assertEqual(json.loads(r.data), {"name": data})
        self.assertEqual(json.loads(r.data)["name"], data)


if __name__ == '__main__':
    unittest.main()