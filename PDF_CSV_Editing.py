#simple
file=open('verysimplefile.txt','w')#right now its read, can add r/w/a
file.write('This has been written to a file')
file.write('\nanother line')
file.close()
file=open('verysimplefile.txt','a')
amount_written=file.write("\nThe Da Vinci Code") #all needs to be in str format
print(amount_written)
file.close()
with open('verysimplefile.txt') as file:
    txt=file.read(10)
    print(txt)
    for line in file.readlines():
        print(line)
#no need for file.close()

#advanced
import csv
import pip
data=open("example.csv",encoding="utf-8") #default is read mode
csv_data=csv.reader(data)
data_lines=list(csv_data)
print(data_lines[0])
print(len(data_lines)-1)
full_names=[]
for line in data_lines[1:20]:
    full_names.append(line[1]+" "+line[2])
print(full_names)
file_to_output=open("to_save_file.csv",mode="w",newline="")
csv_writer=csv.writer(file_to_output,delimiter=",")
csv_writer.writerow(["a","b","c"])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()
#f=open("to_save_file.csv",mode="a",newline="")
#csv_writer=csv.writer(f)
#csv_writer.writerow(['1','2','3'])
pip.main(["install",'PyPDF2'])
import PyPDF2 as P
f=open("C:\\Users\\justi\\Working_Business_Proposal.pdf","rb")
pdf_reader=P.PdfReader(f)
print(len(pdf_reader.pages))
page_one=pdf_reader.pages[2]

page_one_text=page_one.extract_text()
page_one_text=page_one_text.split(".")
for x in range(len(page_one_text)):
    print(page_one_text[x]+'.')
pdf_output=open("Some_new_document.pdf","wb") #for non-text files
pdf_text=[]
pdf_writer = P.PdfWriter()
for num in range(len(pdf_reader.pages)):
    page=pdf_reader.pages[num]
    pdf_writer.add_page(page)
    pdf_writer.write(pdf_output)
pdf_output.close()
f.close()


