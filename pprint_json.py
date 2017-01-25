import json
import sys


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as f:
            return json.load(f)
    except OSError:
        print('Can\'t open the file `{}`'.format(filepath))
    except json.JSONDecodeError:
        print('Can\'t decode content of the file `{}`. Please check the file').format(filepath)
    sys.exit(1)


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python pprint_json.py <path to file>')
        sys.exit(1)
    pretty_print_json(load_data(sys.argv[1]))
