from PyPDF2 import PdfFileWriter, PdfFileReader

class Splitter:
    def __get_first_and_last_pages(self, pages: str):
        splitted_pages = pages.split('-')
        return int(splitted_pages[0]) - 1, int(splitted_pages[1]) - 1

    def __generate_output_pdf(self, pdf: PdfFileWriter, name: str):
        with open(name, 'wb') as new_pdf:
            pdf.write(new_pdf)
    
    def __create_new_pdf(self, input_pdf, initial_page: int, final_page: int):
        output_pdf = PdfFileWriter()
        for i in range(input_pdf.numPages):
            if i >= initial_page and i <= final_page:
                output_pdf.addPage(input_pdf.getPage(i))
        return output_pdf

    def split(self, input_name: str, output_name: str, pages: str):
        initial_page, final_page = self.__get_first_and_last_pages(pages)
        input_pdf = PdfFileReader(open(input_name, 'rb'))

        output_pdf = self.__create_new_pdf(input_pdf, initial_page, final_page)
        self.__generate_output_pdf(output_pdf, output_name)
