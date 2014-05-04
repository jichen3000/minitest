import pypandoc

def convert_readme():
    output = pypandoc.convert('README.md', 'rst')
    with open('README.txt','w+') as the_file:
        the_file.write(output)


if __name__ == '__main__':
    convert_readme()