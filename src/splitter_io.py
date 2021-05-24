class SplitterIo:
    def request_input_pdf(self):
        print('Insert the PDF input file path:')
        pdf_input = input()
        return pdf_input

    def request_output_pdf(self):
        print('Insert the PDF output file path: ')
        pdf_output = input()
        return pdf_output

    def request_pages(self):
        print('Insert the pages interval')
        pages = input()
        return pages

    def finish_succesfull(self):
        print('New PDF file created')
