SIZES = {
    1000: '1k',
    5000: '5k',
    10000: '10k',
    20000: '20k',
    50000: '50k',
    100000: '100k'
}


def file_generator(filepath: str):
    _filename = _generate_name(filepath)

    with open(filepath, 'r') as file:
        data = file.read().splitlines()
        total_records = len(data)

        for key, value in SIZES.items():
            if total_records > key:
                with open(F'./out/{_filename}_{value}.csv', 'w') as tf:
                    tf.write('\n'.join(data[0:key]))

        with open(F'./out/{_filename}_full.csv', 'w') as tf:
            tf.write('\n'.join(data))


def _generate_name(path: str):
    try:
        split_path = path.split('.')
        return split_path[0]
    except Exception:
        return path
