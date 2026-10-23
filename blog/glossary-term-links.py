#!/usr/bin/env python
# ----------------------------------------------------------------------------
# Copyright (c) 2026, Caporaso Lab (https://caplab.dev).
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

# MyST executable plugin (https://mystmd.org/guide/executable-plugins) that
# appends a link to each glossary term's own anchor (e.g.
# glossary/#term-breaking-change), so readers can copy a link to a term.

import json
import sys

NAME = 'glossary-term-links'


def add_links(node):
    # MyST assigns glossary term ids (html_id) during the document stage, so
    # this runs at the project stage, after they exist.
    # The theme prepends the site's base URL to link urls, so the url names
    # the glossary page (blog/glossary.md); the plugin input doesn't say
    # which page it is. (A crossReference node avoids that, but the theme
    # then shows a hover preview of the term's own definition.)
    if node.get('type') == 'definitionTerm' and node.get('html_id'):
        node['children'] += [
            {'type': 'text', 'value': ' '},
            {'type': 'link', 'url': f'/glossary#{node["html_id"]}',
             'children': [{'type': 'text', 'value': '#'}]}]
    for child in node.get('children', []):
        add_links(child)


if __name__ == '__main__':
    if '--transform' in sys.argv:
        ast = json.load(sys.stdin)
        add_links(ast)
        print(json.dumps(ast))
    else:
        print(json.dumps({'name': NAME, 'transforms': [
            {'name': NAME, 'doc': 'Link glossary terms to their anchors',
             'stage': 'project'}]}))
