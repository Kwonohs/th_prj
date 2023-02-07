import pdf
#오류가 해결이 안돼..
pdfFile = 'C:/Users/kwonohsem/Desktop/cookbook_c-2/sample-one-line.pdf'
pdfFileEncrypted = 'C:/Users/kwonohsem/Desktop/cookbook_c-2/sample-one-line.protected.pdf'
print('PDF 1: \n', pdf.getTextPDF(pdfFile))
print('PDF 2: \n', pdf.getTextPDF(pdfFileEncrypted, 'tuffy'))