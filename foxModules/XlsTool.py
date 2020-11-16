#pd.read_excel()報錯解決方案參考: https://www.itread01.com/content/1541404144.html
#開啟Python\lib\site-packages\xlrd\compdoc.py 找到426行將它註解即可 #raise CompDocError("%s corruption: seen[%d] ...)
#pandas讀csv檔案錯誤解決辦法: https://www.itread01.com/content/1546616345.html
#讀csv時注意讀入文件編碼不要設錯
import os,json,re
from datetime import datetime, timedelta
import pandas as pd

def is_contain_ch(strdate):
    match = re.search(r"[\u4e00-\u9fa5]+",strdate)
    if match!=None:
        #strdate內含中文
        return True
    else:
        return False

def is_date(strdate):
    if len(strdate)!=10: return False
    if is_contain_ch(strdate): return False
    match=re.search(r"\d{4}[\/|-]\d{2}[\/|-]\d{2}",strdate)
    if match==None:
        return False
    else:
        return True

def get_file_fullname(input_str1):
    return input_str1.split("\\")[-1]

def get_file_type(input_str2):
    return input_str2.split(".")[-1]

""" XLS匯出CSV函式 """
def xls_to_csv(xls_loc,csv_loc, sheet='Sheet1',output_encoding='utf-8'):
    read_file = pd.read_excel(xls_loc, sheet_name=sheet)
    read_file.to_csv(csv_loc, sep='\t', index = None, header=True, encoding=output_encoding)
    #print(xls_loc+" 轉存為 "+csv_loc+" 完成!")
    print("[ OK ] 將 "+get_file_fullname(xls_loc)+" 轉存為 "+get_file_fullname(csv_loc)+"  文件編碼:"+output_encoding+"")

""" 變更CSV文件編碼 """
def csv_change_encoding(csv_loc_s,csv_loc_o,input_encoding='Big5',output_encoding='utf-8'):
    read_file = pd.read_csv(csv_loc_s,encoding=input_encoding)
    read_file.to_csv(csv_loc_o, sep='\t', index = None, header=True, encoding=output_encoding)
    print("[ OK ] 將 "+get_file_fullname(csv_loc_o)+" 的文件編碼由 "+input_encoding+" 變更為 "+output_encoding)
