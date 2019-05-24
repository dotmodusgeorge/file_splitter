import sys
from splitter import file_generator


def main():
    files = sys.argv
    files.pop(0)
    for file in files:
        file_generator(file)


main()
