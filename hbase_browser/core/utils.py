# Method for encoding ints with base64 encoding
import base64
import struct


def encode(n):
    """
    Method for encoding ints with base64 encoding
    """
    data = struct.pack("i", n)
    s = base64.b64encode(data)
    return s


def decode(s):
    """
    Method for decoding ints with base64 encoding
    """
    data = base64.b64decode(s)
    n = struct.unpack("i", data)
    return n[0]


def is_successful(request):
    """
    Checks the request object to see if the call was successful
    """
    return 200 <= request.status_code <= 299