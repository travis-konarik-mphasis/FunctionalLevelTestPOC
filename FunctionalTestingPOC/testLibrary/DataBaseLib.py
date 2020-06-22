from FunctionalTestingPOC.PocMocks.DatabaseMock import DatabaseMock


class DataBaseLib:
    def __init__(self):
        self._database = DatabaseMock()

    def create_batch_in_database(self, batch_number):
        batch = (batch_number,)
        return DatabaseMock.add_batch(batch)

    def add_record_to_batch(self, batch_id, record_number, processing_status_id):
        record = (batch_id, record_number, processing_status_id)
        return DatabaseMock.add_record(record)

    def get_record(self, record_id):
        return DatabaseMock.get_record_with_id(record_id)

    def get_responses_for_record(self, record_id):
        return DatabaseMock.get_responses_for_record(record_id)

    def init_database(self):
        DatabaseMock.init_schema()

    def truncate_database(self):
        DatabaseMock.truncate_database()

