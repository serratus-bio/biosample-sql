MAX_ITEMS_PER_WORKER = 1000
xml_file = 'data/head.xml'

def prepare_worker(start_byte):
    with open(xml_file, 'r') as f:
        _ = f.seek(start_byte, 0)
        if start_byte == 0:
            start_byte += len(next(f)) # skip <?xml ...
            start_byte += len(next(f)) # skip <BioSampleSet>

        count = 0
        n_bytes = 0
        for line in f:
            n_bytes += len(line)
            if line.startswith('</BioSample>'):
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
        prepare_worker(start_byte)

def invoke_worker(start_byte, end_byte):
    pass
    # from worker import handler
    # handler({'start_byte': start_byte, 'end_byte': end_byte}, None)

manage()
