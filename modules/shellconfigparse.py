#!venv/bin/python3
# To use this, call parse(filename)
# Parse() returns a dictionary with the key/value pairs
# Assign a variable to the output of parse()
# For example:
#   data = parse('config.sh')
#   my_var = data['var']


def parse(file):
    """Parses shell config file for value

    Args:
        file (string): the config file to parse

    Returns:
        dict: a dict of key/value pairs from config
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

        return data


def deleteComments(string):
    """Deletes # comments

    Args:
        string (string): the string you want to delete comments from

    Returns:
        string: the string without comments
    """
    return string.partition('#')[0]


if __name__ == '__main__':
    parse('config.sh')