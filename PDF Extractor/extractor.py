from PyPDF2 import PdfFileReader
import csv
import pandas as pd
import glob, os
import sys 



def write_csv(input,page_num):
    with open(path[:-4]+'_'+str(page_num)+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([input])

def extract_text_from_pdf(generate_csv):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        print("number of pages: ",pdf.getNumPages())
        print()

        for i in range(pdf.getNumPages()):
            page_num = i
            # get the first page
            page = pdf.getPage(page_num)
            # print(page)
            # print('Page type: {}'.format(str(type(page))))
            text = page.extractText()
            textList = text.splitlines()

            if generate_csv:
                write_csv(text,page_num)

            business = {
                'License Number': [],
                'Business Name': [],
                'Owner Name': [],
                'License Type': [],
                'Service Address': [],
                'Mailing Address': [],
                'Issue Date': [],
            }

            i = 11
            records = 0

            while i < len(textList)-9:
                # print(i,textList[i])

                # Service Address 3 lines / Mailing Address Same Address
                if len(textList[i])==7 and (textList[i+9][0:3]=="113") and (textList[i+6] == "SAME AS SERVICE ADDRESS"):
                    print(f"Service Address 3 lines / Mailing Address Same Address - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+5] + " " + textList[i+8])
                    business['Mailing Address'].append(textList[i+6])
                    business['Issue Date'].append(textList[i+7])

                # Service Address 2 lines / Mailing Address 2 lines
                elif len(textList[i])==7 and (textList[i+9][0:3]=="113") and (textList[i+6] != "SAME AS SERVICE ADDRESS"):
                    print(f"Service Address 2 lines / Mailing Address 2 lines - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+7])
                    business['Mailing Address'].append(textList[i+5] + " " + textList[i+8])
                    business['Issue Date'].append(textList[i+6])

                # Last Record / Service Address 2 lines / Mailing Address Same Address
                elif len(textList[i])==7 and (textList[i+8][0:4]=="Page"):
                    print(f"Last Record / Service Address 2 lines / Mailing Address Same Address - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+7])
                    business['Mailing Address'].append(textList[i+5])
                    business['Issue Date'].append(textList[i+6])
                    break

                # Last Record / Service Address 2 lines / Mailing Address 2 lines
                elif len(textList[i])==7 and (textList[i+9][0:4]=="Page"):
                    print(f"Last Record / Service Address 2 lines / Mailing Address 2 lines - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+7])
                    business['Mailing Address'].append(textList[i+5] + " " + textList[i+8])
                    business['Issue Date'].append(textList[i+6])
                    break

                # Service Address 2 lines / Mailing Address Same Address
                elif len(textList[i])==7 and (textList[i+8][0:3]=="113") and (textList[i+5] == "SAME AS SERVICE ADDRESS"):
                    print(f"Service Address 2 lines / Mailing Address Same Address - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+7])
                    business['Mailing Address'].append(textList[i+5])
                    business['Issue Date'].append(textList[i+6])

                # Service Address 3 lines / Mailing Address 2 lines and 1 middle empty line
                elif len(textList[i])==7 and (textList[i+10][0:3]=="113"):
                    print(f"Service Address 3 lines / Mailing Address 2 lines and 1 middle empty line - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+5] + " " + textList[i+8])
                    business['Mailing Address'].append(textList[i+6] + " " + textList[i+9])
                    business['Issue Date'].append(textList[i+7])

                # Service Address 3 lines / Mailing Address 3 lines
                elif len(textList[i])==7 and (textList[i+11][0:3]=="113"):
                    print(f"Service Address 3 lines / Mailing Address 3 lines - {textList[i]}")
                    records +=1
                    business['License Number'].append(textList[i])
                    business['Business Name'].append(textList[i+1])
                    business['Owner Name'].append(textList[i+2])
                    business['License Type'].append(textList[i+3])
                    business['Service Address'].append(textList[i+4] + " " + textList[i+5] + " " + textList[i+9])
                    business['Mailing Address'].append(textList[i+6] + " " + textList[i+7] + " " + textList[i+10])
                    business['Issue Date'].append(textList[i+8])

                i+=1
        
            print()
            print(f"Number of records in page {page_num}: {records}")
            print()
            
            df = pd.DataFrame(business, columns = ['License Number','Business Name','Owner Name','License Type','Service Address','Mailing Address','Issue Date'])
            # print(df)
            df.to_excel (path[:-4]+'_'+str(page_num)+'.xlsx', index = False, header=True)

def get_pdfs():
    pdfs_list = []
    os.getcwd()
    for file in glob.glob("*.pdf"):
        pdfs_list.append(file)
    print("pdfs_list: ",pdfs_list)
    return (pdfs_list)

def delete_csv_and_pdfs():    
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('.xlsx'):
            os.remove(os.getcwd() + "\\" + file_name)
        elif file_name.endswith('.csv'):
            os.remove(os.getcwd() + "\\" + file_name)

# get_pdfs()
# path = '2020-07-20.pdf'
# print("Extracting text from pdf: ", path, end="\n")
# delete_csv_and_pdfs()
# extract_text_from_pdf(generate_csv=True)       

# PROCESS ALL PDFs IN DIRECTORY
delete_csv_and_pdfs()
pdfs_list = get_pdfs()
for pdf in pdfs_list:
    path = pdf
    print("Extracting text from pdf: ", path, end="\n")
    extract_text_from_pdf(generate_csv=False)



# for arg in sys.argv: 
#     print (arg) 

# pyinstaller.exe --exclude-module matplotlib --onefile extractor.py