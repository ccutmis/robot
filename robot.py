import os, re, sys,shutil
current_dir=os.path.dirname(os.path.abspath(__file__))
import traceback
from ftplib import FTP
from foxModules.WindowMgr import WindowMgr
from foxModules.Gui import Gui
import foxModules.FileSystem as FS
import foxModules.Ftp as FTP
import foxModules.IniRead as IniRead
#讀取 ReDict.func_re_dict 字典檔 作為中文函式轉換使用
import foxModules.FuncReDict as ReDict

def script_rewrite(script_loc,loc_mode=''):
    w=WindowMgr()
    g=Gui()
    w.set_cmd_title('ROBOT')
    if loc_mode=='':
        if os.path.exists(script_loc):
            tmp_file=open(script_loc,'r',encoding='utf-8')
            content=tmp_file.read()
        else:
            print("腳本文件檔 "+script_loc+" 不存在! 程式結束。")
            return False
    else:
        tmp_list=script_loc.split('|')
        content=""
        for i in tmp_list: content+=i+"\n"
    for k, v in ReDict.func_re_dict.items():
        content=re.sub(k,v,content)
    #print(content)
    try:
        exec(content)
    except Exception as e:
        error_class = e.__class__.__name__ #取得錯誤類型
        detail = e.args[0] #取得詳細內容
        cl, exc, tb = sys.exc_info() #取得Call Stack
        lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
        fileName = lastCallStack[0] #取得發生的檔案名稱
        lineNum = lastCallStack[1] #取得發生的行號
        funcName = lastCallStack[2] #取得發生的函數名稱
        errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
        with open('robot_runtime_error.log','a+',encoding='utf-8') as f:
            f.writelines(g.current_date_time("%Y-%m-%d %H:%M:%S")+'\t'+loc_mode+'\t'+script_loc+'\t'+errMsg+'\n')
        print(errMsg)

if __name__ == '__main__':
    #讀取config.ini參數 使用configparser模組將ini轉為dict並回傳
    try:
        config=IniRead.ini_to_dict("robot_config.ini")
        script_loc=config['SETTING.script_loc']
    except:
        with open('robot_runtime_error.log','a+',encoding='utf-8') as f:
            f.writelines('\t\t\t讀取robot_config.ini失敗!請確認該檔是否存在!\n')
        print("讀取robot_config.ini失敗!請確認該檔是否存在!")
    if len(sys.argv)>2 and sys.argv[1]=='-s':
        #print('執行單行腳本: "'+sys.argv[2]+'"')
        script_rewrite(sys.argv[2],'-s')
    elif len(sys.argv)>1 and sys.argv[1]!='-s':
            script_loc=sys.argv[1]
            #print("腳本文件檔路徑: "+script_loc)
            script_rewrite(script_loc)
    else:
        #print("腳本文件檔路徑: "+script_loc)
        script_rewrite(script_loc)
