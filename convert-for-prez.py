import re

prez_files = ['2022-04-10-googles-pathways-language-model-and-chain-of-thought.md']


template = """# {title}
"""

for file in prez_files:
    with open('_posts/' + file, 'rt') as f:
        doc = f.read()

    doc_split = doc.split('---')
    header_str = doc_split[1]
    contents = doc_split[2]
    contents = re.compile(r'\n*{%.*?%}\n*', re.DOTALL).sub('', contents)
    header_dict = dict()
    for line in header_str.split('\n'):
        if len(line.strip()) > 0:
            key, value = line.split(': ')
            header_dict[key] = value

    contents = template.format(**header_dict) + contents

    with open('presentations/' + file + '.gen', 'wt+') as f:
        f.write(contents)
