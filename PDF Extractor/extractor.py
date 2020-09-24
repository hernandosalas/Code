from PyPDF2 import PdfFileReader
import csv
import pandas as pd
import glob, os
import sys 

total_records = 0

def write_csv(input,page_num):
    with open(path[:-4]+'_'+str(page_num)+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([input])

def extract_text_from_pdf(generate_csv):
    global total_records
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)

        print("Number of pages found: ",pdf.getNumPages())
        print()

        business = {
            'License Number': [],
            'Business Name': [],
            'Owner Name': [],
            'License Type': [],
            'Service Address': [],
            'Mailing Address': [],
            'Issue Date': [],
        }

        for i in range(pdf.getNumPages()):
            page_num = i
            page = pdf.getPage(page_num)
            text = page.extractText()
            textList = text.splitlines()

            if generate_csv:
                write_csv(text,page_num)

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
            total_records += records
            
        df = pd.DataFrame(business, columns = ['License Number','Business Name','Owner Name','License Type','Service Address','Mailing Address','Issue Date'])
        # df.to_excel (path[:-4]+'_'+str(page_num)+'.xlsx', index = False, header=True)
        df.to_excel (path[:-4]+'.xlsx', index = False, header=True)

def get_pdfs():
    pdfs_list = []
    os.getcwd()
    for file in glob.glob("*.pdf"):
        pdfs_list.append(file)
    print("Pdf files found: ",pdfs_list)
    print()
    return (pdfs_list)

def get_xlsx():
    xlsx_list = []
    os.getcwd()
    for file in glob.glob("*.xlsx"):
        xlsx_list.append(file)
    # print("xlsx_list: ",xlsx_list)
    return (xlsx_list)

def delete_csv_and_xlsx():    
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('.xlsx'):
            os.remove(os.getcwd() + "\\" + file_name)
        elif file_name.endswith('.csv'):
            os.remove(os.getcwd() + "\\" + file_name)

def delete_all_xlsx_except_total():
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith('.xlsx') and file_name !="total.xlsx":
            os.remove(os.getcwd() + "\\" + file_name)

def join_xlsx():
    df = pd.DataFrame()
    xlsx_list = get_xlsx()
    for file in xlsx_list:
        df = df.append(pd.read_excel(file), ignore_index=True) 
    df.head() 

    # Write xlsx file with auto fit width columns
    writer = pd.ExcelWriter('total.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index = False)
    worksheet = writer.sheets['Sheet1']
    for idx, col in enumerate(df):
        series = df[col]
        max_len = max((
            series.astype(str).map(len).max(), len(str(series.name)))) + 2  
        worksheet.set_column(idx, idx, max_len)
    writer.save()

def get_arguments():
    args = []
    for arg in sys.argv:
        args.append(arg)
    if len(args) > 1:
        print("Arguments:")
        print(args[1:])
    print()

# PROCESS ALL PDFs IN DIRECTORY
get_arguments()
delete_csv_and_xlsx()
pdfs_list = get_pdfs()
# pdfs_list = ['2020-07-13.pdf']
print("///////////////////////////////////////////////")
print("---Extraction of texts from pdfs - Started")
print("///////////////////////////////////////////////")
print()
for pdf in pdfs_list:
    path = pdf
    print("-----------------------------------------------------------------------------------------------")
    print("Extracting text from pdf: ", path)
    extract_text_from_pdf(generate_csv=False)
print()
print("///////////////////////////////////////////////")
print("---Extraction of texts from pdfs - Ended")
print("///////////////////////////////////////////////")
print()
print("***********************************************")
print("Results total.xlsx generated")
print(f"Total records processed: {total_records}")
join_xlsx()
delete_all_xlsx_except_total()

