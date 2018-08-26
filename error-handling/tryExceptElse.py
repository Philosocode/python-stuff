""" TRY/FINALLY:
    I want exceptions to propagate up, but want to run
    clean up code when there are exceptions """

handle = open('/my/random/file.txt')
try:
    data = handle.read()
finally:
    handle.close()
    """ TRY/EXCEPT/ELSE:
        Make clear which exceptions will be handled by code, and which will
        propagate up. """


def load_json_key(data, key):
    try:
        result_dict = json.loads(data)  # May raise ValueError; handle this
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]  # May raise KeyError; propogate error


""" TRY/EXCEPT/ELSE/FINALLY:
    try: try sth. Except: handle error in try block. Else: error propogate
    Finally: cleanup code """

UNDEFINED = object()


def divide_json(path):
    handle = open(path, 'r+')
    try:
        data = handle.read()  # May raise UnicodeDecodeError
        op = json.loads(data)  # May raise ValueError
        value = (
            op['numerator'] / op['denominator'])  # May raise ZeroDivisionError
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)  # May cause IOError
        return value
    finally:
        handle.close()  # Always run
