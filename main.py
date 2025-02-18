import scriptlibraries.myui as ui
import scriptlibraries.myio as io 
import scriptlibraries.mymainlogic as logic
import logging #2024-11-30_Wiederinbetriebnahme_2463.022_signiert.pdf

logging.basicConfig(
        level=logging.ERROR,
        format='%(asctime)s - %(name)10s - %(levelname)10s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='logs/main.log')

logger = logging.getLogger('Main')
logger.setLevel(logging.DEBUG)

pdfstxt = logic.read_all_pdfs(input("The name of the subfolder where the files are located\n\
The folder must be in the same folder from where this script is being run! : "),echo=True)
fleet = input("Which fleet are you reading the reports for:\n Options: ABY, Desiro, Mireo, FLIRT:")
firstpass=True
for pdftxt in pdfstxt:
    logger.debug(f'Starting work on the new pdf file!')
    train_num = logic.find_train_num(pdftxt,fleet)
    date = logic.extract_between_strings(pdftxt,logic.DATE_START_STRING,"")
    b1_txt = logic.extract_between_strings(pdftxt,logic.B1_START_STRING_ALT,train_num)
    b2_txt = logic.extract_between_strings(pdftxt,logic.B2_START_STRING,logic.B2_END_STRING)
    date = date[0]

    try:
        str_b2 = b2_txt[0].splitlines()
    except IndexError:
        str_b2=[]
        logger.info(f'Index list out of range for str_b2 = {str_b2}, skipping it')
    try:
        str_b1 = b1_txt[0].splitlines()
    except IndexError:
        str_b1=[]
        logger.info(f'Index list out of range for str_b2 = {str_b1}, skipping it')

    str_sum = str_b1+str_b2 # Contains indications from both 2b and 1b parts of the report

    export_list = logic.form_data_for_export(date,train_num,str_sum)
    column_names = ("Date","Vehicle ID","Indication Number", "Description")

    if firstpass:
        logic.export_to_csv(export_list,column_names=column_names,mode='w')
        firstpass=False
        logger.debug('The first pdf file done!')
        # If its the first file to be worked on, write the new output file.
    else:
        logic.export_to_csv(export_list)
        # When its not the first file to be worked on, append to the csv instead of overriding

