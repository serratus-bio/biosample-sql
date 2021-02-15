from download import get_contents
from worker import handler

MAX_ITEMS_PER_WORKER = 1000

def prepare_worker(start_byte):
    f = get_contents(start_byte)
    lines = f.iter_lines()
    if start_byte == 0:
        start_byte += len(next(lines)) + 1 # skip <?xml ...
        start_byte += len(next(lines)) + 1 # skip <BioSampleSet>
        print(start_byte)

    count = 0
    n_bytes = 0
    for line in lines:
        if n_bytes == 0:
            if not line.startswith(b'<BioSample'):
                raise Exception('parse error')
        n_bytes += len(line) + 1
        if line.startswith(b'</BioSample>'):
            count += 1
        if count == MAX_ITEMS_PER_WORKER:
            break

    end_byte = start_byte + n_bytes
    invoke_worker(start_byte, end_byte)
    return end_byte

def manage():
    start_byte = 0
    while start_byte < 10000000:
        print(start_byte)
        start_byte = prepare_worker(start_byte)

def invoke_worker(start_byte, end_byte):
    pass
    # handler({'start_byte': start_byte, 'end_byte': end_byte}, None)

manage()
