import requests

from flask import abort
from FunctionalTestingPOC.TestHelpers.WebServiceMock import Mock


class WebServiceMockLib:
    _api_service_mock = None
    _process_json = "{}"
    _validate_json = "{}"

    def start_api_web_service(self):
        self._api_service_mock = Mock()
        self._api_service_mock.start()

    def init_process_endpoint(self):
        self._api_service_mock.set_process(self._init_process_callback)

    def init_validate_endpoint(self):
        self._api_service_mock.set_validate(self._init_validate_callback)

    def set_process_endpoint_to_return_json(self, json):
        self._process_json = json
        self._api_service_mock.set_process(self._process_json_callback)

    def set_process_endpoint_to_gateway_timeout(self):
        self._api_service_mock.set_process(self._process_gateway_timeout_callback)

    def set_validate_endpoint_to_return_json(self, json):
        self._validate_json = json
        self._api_service_mock.set_validate(self._validate_json_callback)

    def stop_api_web_service(self):
        requests.get('http://localhost:5000/kill')

    def _init_process_callback(self):
        raise Exception("Initialized process endpoint not overwritten, but called")

    def _process_json_callback(self):
        return self._process_json

    def _validate_json_callback(self):
        return self._validate_json

    def _process_gateway_timeout_callback(self):
        abort(504)

    def _init_validate_callback(self):
        raise Exception("Initialized validate endpoint not overwritten, but called")

