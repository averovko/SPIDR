__author__ = 'extrimal'

from lxml import etree


class XMLConverter():

    def getn(node):
        print (node.tag, node.keys(), node.get('name'), node.values())
        for n in node:
            XMLConverter.getn(n)

    def convert_navigation(xml_file):
        tree = etree.parse(xml_file)
        print(etree.tostring(tree.getroot(), pretty_print=True, method="xml"))

        XMLConverter.getn(tree.getroot())
#        for action, elem in 
        html = 'Navigation from {}'.format(xml_file)

        return html