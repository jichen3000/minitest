import pandoc
import os

def convert_readme():
    pandoc.core.PANDOC_PATH = '/usr/local/bin/pandoc'

    doc = pandoc.Document()
    doc.markdown = open('README.md').read()
    f = open('README.txt','w+')
    f.write(doc.rst)
    f.close()

if __name__ == '__main__':
    convert_readme()