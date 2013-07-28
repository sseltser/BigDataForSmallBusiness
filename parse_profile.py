import pandas
import lxml
from lxml import etree
import os

file_name ="profile2.html"

f = open(file_name)
file_content = f.read()
f.close()

root = etree.fromstring(file_content)

r = tree.xpath('/html/body/div/form/div[4]/table[2]')
