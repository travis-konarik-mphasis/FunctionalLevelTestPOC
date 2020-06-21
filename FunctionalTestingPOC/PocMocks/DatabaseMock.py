import copy


# {id: (id, batch_number)}
_batch = dict()

# {id: (id, batch_id, record_number, processing_status_id)}
_record = dict()

# {id: (id, record_id, processing_status_id, response_json)}
_response = dict()

# {id: (id, enum, description)}
_processing_status = dict()

_processing_statuses = {
    1: (1, "Process", "Ready To Be Processed"),
    2: (2, "Retry", "Ready To Be Rep-Processed"),
    3: (3, "Validated", "Valid, But Not Processed"),
    4: (4, "Invalid", "Invalid, Not Processed"),
    5: (5, "Error", "Processing Returned an Error"),
    6: (6, "Processed", "Processing Complete"),
    7: (7, "Complete", "Processing Results Uploaded"),
}


class DatabaseMock:

    @staticmethod
    def add_batch(batch):
        id_num = len(_batch) + 1
        _batch.update({id_num: (id_num,) + batch})
        return _batch[id_num]

    @staticmethod
    def add_record(record):
        id_num = len(_record) + 1
        _record.update({id_num: (id_num,) + record})
        return _record[id_num]

    @staticmethod
    def add_response(response):
        id_num = len(_response) + 1
        _response.update({id_num: (id_num,) + response})
        return _response[id_num]

    @staticmethod
    def get_processing_status_with_id(processing_status_id):
        return _processing_status[processing_status_id]

    @staticmethod
    def get_batch_with_id(batch_id):
        return _batch[batch_id]

    @staticmethod
    def get_record_with_id(record_id):
        return _record[record_id]

    @staticmethod
    def get_response_with_id(response_id):
        return _response[response_id]

    @staticmethod
    def get_responses_for_record(record_id):
        output = []
        for (key, value) in _response.items():
            if value[1] == record_id:
                output.append(value)

        return output

    @staticmethod
    def get_records_for_processing():
        output = []
        for (key, value) in _record.items():
            if value[3] == 1 or value[3] == 2:
                output.append(value)

        return output

    @staticmethod
    def update_record_status(record_id, processing_status_id):
        record = _record[record_id]
        new_record = record[0:3] + (processing_status_id,) + record[4:]
        _record[record_id] = new_record

    @staticmethod
    def reset_data():
        pass

    @staticmethod
    def init_schema():
        _processing_status.update(copy.deepcopy(_processing_statuses))

    @staticmethod
    def truncate_database():
        _batch.clear()
        _record.clear()
        _response.clear()
        _processing_status.clear()
