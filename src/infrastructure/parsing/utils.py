from itertools import chain

from lxml.etree import tostring


def stringify_children(node):
    parts = [node.text] + list(chain(*([c.text, tostring(c), c.tail] for c in node.getchildren()))) + [node.tail]
    parts = [str(p) for p in parts]
    return parts
