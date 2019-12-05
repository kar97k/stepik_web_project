from pprint import pformat
from cgi import parse_qsl, escape

def application(environ, start_response):
    
    output = b''
    d = parse_qsl(environ['QUERY_STRING'])

    if environ['REQUEST_METHOD'] == 'GET':
        if environ['QUERY_STRING'] != '':
            for ch in d:
                output +=  '='.join(ch)
                output += '\n'

    output_len = sum(len(line) for line in output)
    start_response('200 OK', [('Content-type', 'text/plain'),
                              ('Content-Length', str(output_len))])
    return output
