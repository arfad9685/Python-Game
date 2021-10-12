from PyPDF2 import PdfFileMerger
# list of pdf files to merge
pdfs = ['SGX1.pdf', 'SGX2.pdf']
# create instance for merging pdf
merge = PdfFileMerger()
# append all pdf files with
# iteation through pdfs list 
for pdf in pdfs:
    merge.append(pdf)
# write new merged pdf file
with open('SGX3.pdf', 'wb') as file:
    merge.write(file)
print('Pdf files merged into SGX3.pdf')