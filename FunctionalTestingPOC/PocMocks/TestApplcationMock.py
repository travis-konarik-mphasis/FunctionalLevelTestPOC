import requests

from FunctionalTestingPOC.PocMocks.DatabaseMock import DatabaseMock


class TestApplicationMock:
    @staticmethod
    def run():
        records = DatabaseMock.get_records_for_processing()
        for record in records:
            validate_request = requests.get('http://localhost:5000/validate')
            if validate_request.text == '{"Result": "Success"}':
                process_request = requests.get('http://localhost:5000/process')
                if process_request.status_code is 200:
                    DatabaseMock.update_record_status(record[0], 6)
                    response = (record[0], 6, process_request.text)
                    DatabaseMock.add_response(response)
                else:
                    DatabaseMock.update_record_status(record[0], 5)
                    response = (record[0], 5, '{"Result": "Error Processing", "Reason": "Continuous Gateway Timeout"}')
                    DatabaseMock.add_response(response)


