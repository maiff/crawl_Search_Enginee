import logging
import os
import inspect
import hashlib


def get_current_function_name():
    return inspect.stack()[1][3]


def notBeNone(args, funtion_name):
    logging.error('%s can\'t be none in [%s]', args, funtion_name)


def save_file(path=None, name=None, content = None):
    if path is None or name is None:
        notBeNone('path or name', get_current_function_name())
    else:
        filename = os.path.join(path, name)
        with open(filename, 'wb') as f:
            f.write(content)


def md5(_str=None):
    if _str is None:
        notBeNone('_str', get_current_function_name())
    else:
        m = hashlib.md5()
        m.update(_str)
        return m.hexdigest()


def isHasHttpOrHttps(_str=None):
    if _str is None:
        notBeNone('_str', get_current_function_name())
    if _str[:5] == 'http:' or _str[:6] == 'https:':
        return  True
    return False



