from lambda_helpers import invoke_lambda
import boto3

s3 = boto3.resource('s3')
s3_object = s3.Object(bucket_name='serratus-public', key='notebook/210212_geo/victorlin/biosample_parse/biosample_set.xml')

WORKER_LAMBDA = 'biosample-upload-worker'
MAX_ITEMS_PER_WORKER = 1000


def handler(event, context):
    start_byte = event['start_byte']
    end = s3_object.content_length / 5000
    while start_byte < end:
        # print(start_byte)
        start_byte = prepare_worker(start_byte)
        print(start_byte / end)


def get_contents(start_byte, end_byte=None):
    if not end_byte:
        end_byte = ''
    return s3_object.get(Range=f'bytes={start_byte}-{end_byte}')['Body']


def prepare_worker(start_byte):
    f = get_contents(start_byte)
    lines = f.iter_lines()
    if start_byte == 0:
        start_byte += len(next(lines)) + 1 # skip <?xml ...
        start_byte += len(next(lines)) + 1 # skip <BioSampleSet>

    count = 0
    n_bytes = 0
    for line in lines:
        if n_bytes == 0 and not line.startswith(b'<BioSample'):
            raise Exception('parse error')
        n_bytes += len(line) + 1
        if line.startswith(b'</BioSample>'):
            count += 1
        if count == MAX_ITEMS_PER_WORKER:
            break

    end_byte = start_byte + n_bytes
    print(start_byte, end_byte)
    invoke_worker(start_byte, end_byte)
    return end_byte


def invoke_worker(start_byte, end_byte):
    event = {'start_byte': start_byte, 'end_byte': end_byte}
    invoke_lambda(WORKER_LAMBDA, event)
