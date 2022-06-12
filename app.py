import PyPDF2
import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
pdfs=[]
for f in files:
    if f[-6:]=='RO.pdf':
        print("Ignoring",f)
    elif f[-4:]=='.pdf':
        pdfs.append(f)
    

if pdfs == []:
    print('No PDFS in working directory')
    exit()
else:
    print("PDFs to reorder")
    for pdf in pdfs:
        print(pdf)
    edit=input("Commence editing of above files? [y/n]")
    if edit.lower()=='y':
        print("Proceeding")
    else:
        exit()



for pdf in pdfs:
    epdf=PyPDF2.PdfFileReader(pdf, strict=False)
    pdf_writer = PyPDF2.PdfFileWriter()
    numpages=epdf.getNumPages()
    if numpages%2!=0:
        print(pdf, "not duplex scan, needs even number of pages")
    else:
        start=0
        end=numpages-1
        for pagenum in range(int(numpages/2)):
            if pagenum%2==1:
                page = epdf.getPage(end)
                end-=1
            else:
                page = epdf.getPage(start)
                start+=1
            pdf_writer.addPage(page)
        output_file=open((pdf[:-4]+'_RO'+'.pdf'),mode='wb')
        pdf_writer.write(output_file)
        print(pdf, 'reordered and saved')
