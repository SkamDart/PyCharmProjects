def findDuplicate(self, paths):
    """
    :type paths: List[str]
    :rtype: List[List[str]]
    """
    content = defaultdict(set)
    duplicates = []

    for path in paths:
        directory, *files = path.split(' ')
        for file in files:
            left = file.find('(') + 1
            right = file.find(')')
            content_slice = slice(left, right)
            f_content = file[content_slice]
            f_name = file[:left - 1]
            absolute_path = '/'.join([directory, f_name])
            content[f_content].add(absolute_path)

    for c in content:
        entry = content[c]
        if len(entry) > 1:
            duplicates.append(list(entry))
    return duplicates
