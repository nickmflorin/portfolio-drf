from collections import OrderedDict
from datetime import datetime
import json
import logging
from logging.handlers import SysLogHandler
import socket
import traceback


from . import global_ctx


BUILTIN_ATTRS = {'args', 'asctime', 'created', 'exc_info', 'exc_text',
                 'filename', 'funcName', 'levelname', 'levelno', 'lineno', 'module', 'msecs',
                 'message', 'msg', 'name', 'pathname', 'process', 'processName',
                 'relativeCreated', 'stack_info', 'thread', 'threadName', }


def fix_circular_refs(o, _seen=None):
    if _seen is None:
        _seen = set()

    if id(o) in _seen:
        # circular reference, remove it.
        return '<cycle>'

    _seen.add(id(o))

    res = o

    if isinstance(o, dict):
        res = {
            fix_circular_refs(k, _seen): fix_circular_refs(v, _seen)
            for k, v in o.items()}
    elif isinstance(o, (list, tuple, set, frozenset)):
        res = type(o)(fix_circular_refs(v, _seen) for v in o)

    # remove id again; only *nested* references count
    _seen.remove(id(o))
    return res


class SafeJSONEncoder(json.JSONEncoder):
    def default(self, o):
        return repr(o)

    def encode(self, o):
        return super().encode(fix_circular_refs(o))

    def iterencode(self, o, **kwargs):
        return super().iterencode(fix_circular_refs(o), **kwargs)


class JsonLogFormatter(logging.Formatter):
    """
    Log formatter that outputs machine-readable json.

    Adapted from:
    https://github.com/mozilla-services/python-dockerflow/blob/master/src/dockerflow/logging.py
    https://github.com/DanHoerst/json-log-formatter/blob/master/json_log_formatter/__init__.py
    """
    LOGGING_FORMAT_VERSION = "1"

    def __init__(self, fmt=None, datefmt=None, style="%", logger_name="json_logger"):
        parent_init = logging.Formatter.__init__
        parent_init(self, format, datefmt, style)
        self.logger_name = logger_name
        self.hostname = socket.gethostname()
        self.syslog_handler = SysLogHandler()

    def format(self, record):
        """
        Map from Python LogRecord attributes to JSON log format fields

        * usage - logger.info('My message', extra={'something': 'sick. tight.'})
        * from - https://docs.python.org/3/library/logging.html#logrecord-attributes
        * to -
            {
                'message': 'My message',
                'time': '2015-09-01T06:06:26.524448',
                'something': 'sick. tight.'
            }
        """
        data = OrderedDict({
            'logger': record.name,
            'level': self.syslog_handler.mapPriority(record.levelname),
            'time': datetime.utcnow().isoformat(),
        })

        message = record.getMessage()
        # Only include the 'msg' key if it has content and is not already a JSON blob.
        if message and not message.startswith("{") and not message.endswith("}"):
            data["msg"] = message

        data.update({
            'hostname': self.hostname,
        })

        if global_ctx.user:
            data['user_id'] = global_ctx.user.pk
        if global_ctx.remote_addr:
            data['remote_addr'] = global_ctx.remote_addr

        # Include any other custom attributes set on the record.
        data.update({
            attr_name: record.__dict__[attr_name]
            for attr_name in record.__dict__
            if attr_name not in BUILTIN_ATTRS
        })

        if global_ctx.trace_id:
            data['trace_id'] = global_ctx.trace_id
        if global_ctx.amzn_trace:
            data['amzn_trace'] = global_ctx.amzn_trace

        # If there is an error, format it for nice output.
        if record.exc_info is not None:
            data["error"] = repr(record.exc_info[1])
            data["traceback"] = safer_format_traceback(*record.exc_info)

        return json.dumps(data, cls=SafeJSONEncoder)


def safer_format_traceback(exc_typ, exc_val, exc_tb):
    """
    Format an exception traceback into safer string.

    We don't want to let users write arbitrary data into our logfiles,
    which could happen if they e.g. managed to trigger a ValueError with
    a carefully-crafted payload.  This function formats the traceback
    using "%r" for the actual exception data, which passes it through repr()
    so that any special chars are safely escaped.
    """
    lines = ["Uncaught exception:\n"]
    lines.extend(traceback.format_tb(exc_tb))
    lines.append("%r\n" % (exc_typ,))
    lines.append("%r\n" % (exc_val,))
    return "".join(lines)
