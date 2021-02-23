from lambda_helpers import invoke_lambda
import boto3

s3 = boto3.resource('s3')
s3_object = s3.Object(bucket_name='serratus-public', key='notebook/210212_geo/victorlin/biosample_parse/biosample_set.xml')

WORKER_LAMBDA = 'biosample-upload-worker'
MAX_ITEMS_PER_WORKER = 10000
MINIMUN_REMAINING_TIME_MS = 10000

def handler(event, context):
    start_byte = event.get('start_byte', 0)
    end = s3_object.content_length
    while start_byte < end:
        if context.get_remaining_time_in_millis() < MINIMUN_REMAINING_TIME_MS:
            break
        start_byte = prepare_worker(start_byte)
    if start_byte < end:
        invoke_new_manager(context, start_byte)
    else:
        # final worker
        invoke_worker(start_byte, end)


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
    worker_bytes = 0
    biosample_bytes = 0
    for line in lines:
        # check first line
        if count == 0 and biosample_bytes == 0 and not line.startswith(b'<BioSample'):
            if line.startswith(b'</BioSampleSet>'):
                print('Exiting - reached the end of BioSampleSet.')
                raise SystemExit
            raise Exception(f'parse error: {line} does not start with "<BioSample"')
        biosample_bytes += len(line) + 1
        if line.startswith(b'</BioSample>'):
            worker_bytes += biosample_bytes
            biosample_bytes = 0
            count += 1
        if count == MAX_ITEMS_PER_WORKER:
            break

    end_byte = start_byte + worker_bytes
    print(f'Invoking worker with start,end=({start_byte},{end_byte})')
    invoke_worker(start_byte, end_byte)
    return end_byte


def invoke_worker(start_byte, end_byte):
    event = {'start_byte': start_byte, 'end_byte': end_byte}
    invoke_lambda(WORKER_LAMBDA, event)


def invoke_new_manager(context, next_start_byte):
    # invoke next manager instance
    next_event = {
        'start_byte': next_start_byte
    }
    invoke_lambda(context.function_name, next_event)
