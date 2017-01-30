import json
import sys


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python pprint_json.py <path to file>')
        sys.exit(1)
    json_data = load_data(sys.argv[1])
    if not json_data:
        print('Can\'t load the file {}'.format(sys.argv[1]))
        sys.exit(1)
    else:
        pretty_print_json(json_data)
