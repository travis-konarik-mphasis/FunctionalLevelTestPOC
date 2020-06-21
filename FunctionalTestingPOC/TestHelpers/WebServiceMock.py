from flask import Flask, request
import threading

app = Flask("TestApp")


class Context:
    validate = None
    process = None

    def set_validate(self, validate_handler):
        self.validate = validate_handler

    def set_process(self, process_handler):
        self.process = process_handler


_context = Context()


@app.route('/process')
def process():
    return _context.process()


@app.route('/validate')
def validate():
    return _context.validate()


@app.route('/kill')
def kill():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return 'Dead'


class Mock(object):
    def set_process(self, processCallBack):
        _context.process = processCallBack

    def set_validate(self, validateCallBack):
        _context.validate = validateCallBack

    def start(self):
        print("Starting")
        app.env = "development"
        app.debug = False
        app.use_reloader = False

        thread = threading.Thread(target=app.run)
        thread.daemon = True
        thread.start()
