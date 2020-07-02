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
                lines.append(yeetComments(line).rstrip())
            else:
                lines.append(yeetComments(line).rstrip().replace('"', ''))

        data = dict(s.split('=',1) for s in lines)

        return data[key]


def yeetComments(string):
    """Deletes # comments

    Args:
        string (string): the string you want to yeet comments from

    Returns:
        string: the string without comments
    """
    return string.partition('#')[0]
