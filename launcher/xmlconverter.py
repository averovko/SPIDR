__author__ = 'extrimal'

from lxml import etree


class XMLConverter():

    def getn(node):
        html = ''
        stylesheets = []
        if (node is not None and node.get('href') is not None):
            stylesheets.append(node.get('href'))

        if (node.tag == 'nav'):
            html += '<nav><ul class="menu">'
            for n in node:
                r_html, r_stylesheets = XMLConverter.getn(n)
                html += r_html
                stylesheets.extend(r_stylesheets)
            html += '</ul></nav>'

        if (node.tag == 'collection'):
            html += '<li><a href="#" class="submenu-link">{}</a><ul class="submenu">'.format(node.get('label'))
            for n in node:
                r_html, r_stylesheets = XMLConverter.getn(n)
                html += r_html
                stylesheets.extend(r_stylesheets)
            html += '</ul></li>'

        if (node.tag == 'view'):
            html += '<li><a href="../{}">{}</a></li>'.format(node.get('name'), node.text if node.text is not None else node.get('name'))

        return html, stylesheets

    def convert_navigation(xml_file):
        tree = etree.parse(xml_file)

        html, stylesheets = XMLConverter.getn(tree.getroot())

        return html, stylesheets