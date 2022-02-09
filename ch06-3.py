# 임의의 PDF 파일을 로컬 파일 객체로 바꿔서 문자열로 읽는 코드

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


def convert_pdf_to_txt(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=laparams)

    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pagenos=set()
 
    for page in PDFPage.get_pages(pdfFile, pagenos, maxpages=0, password="", caching=True, check_extractable=True):
        interpreter.process_page(page)
    
    content = retstr.getvalue()
    device.close()
    retstr.close()
    return content

pdfFile = open('7 Wonders Duel Pantheon.pdf', 'rb')
outputString = convert_pdf_to_txt(pdfFile)
print(outputString)
