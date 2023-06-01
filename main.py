# Импортировать библиотеки
from pdf2docx import parse
from typing import Tuple

def convert_pdf2docx(input_file: str, output_file: str, pages: Tuple = None):
    """Преобразует PDF в DOCX"""
    if pages:
        pages = [int(i) for i in list(pages) if i.isnumeric()]
    result = parse(pdf_file=input_file,
                   docx_with_path=output_file, pages=10)
    summary = {
        "Исходный файл": input_file, "Страниц": str(pages), "Результат преобразования": output_file
    }
    # Печать сводки
    print("#### Отчет ########################################################")
    print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
    print("###################################################################")
    return result

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_pdf2docx(input_file, output_file)