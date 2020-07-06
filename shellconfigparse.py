#!venv/bin/python3

# *** Default file is config.sh ***
file = 'config.sh'


def selectFile(f):
    """Selects the file to parse in parse()

    Args:
        f (string): the file
    """
    file = f
    return file


def parse(key):
    """Parses shell config file for value

    Args:
        key (string): the key you want the value to

    Returns:
        string: the value of the key
    """
    with open(file, 'r') as f:
        lines = []
        data = {}
        for line in f:
            if 'TIMESTAMP' in line:
                lines.append(deleteComments(line).rstrip())
            else:
                lines.append(deleteComments(line).rstrip().replace('"', ''))

        data = dict(s.split('=',1) for s in lines)

        return data[key]


def deleteComments(string):
    """Deletes # comments

    Args:
        string (string): the string you want to delete comments from

    Returns:
        string: the string without comments
    """
    return string.partition('#')[0]

if __name__ == '__main__':
    selectFile('config.sh')
    parse('PI_UID')