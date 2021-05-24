from splitter_io import SplitterIo
from splitter import Splitter

if __name__ == '__main__':
    io = SplitterIo()
    splitter = Splitter()

    input_name = io.request_input_pdf()
    print('-----')
    output_name = io.request_output_pdf()
    print('-----')
    pages = io.request_pages()

    splitter.split(input_name, output_name, pages)
    io.finish_succesfull()
