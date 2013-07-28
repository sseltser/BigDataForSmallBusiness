import pandas
import lxml
from lxml import etree
import os

file_name ="choose.html"


parser = etree.XMLParser(ns_clean=True,recover=True)
root = etree.parse(file_name,parser)

r = root.xpath('/html/body/div/form/div[4]/table[2]')
