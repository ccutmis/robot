from ftplib import FTP

""" 建立ftp連線物件 """
def ftpconnect(host,username,password):
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(host,21)
    ftp.login(username,password)
    return ftp

""" 檢查遠端目錄是否存在 """
def check_folder_exist(ftp,remotepath):
    try:
        resp = ftp.sendcmd('MLST '+remotepath)
        if 'type=dir;' in resp:
            print('"'+remotepath+'" dir exists')
            return True
    except:
        print('"'+remotepath+'" dir not exist')
        return False

""" 創建遠端目錄 """
def create_folder(ftp,remotepath):
    if check_folder_exist(ftp,remotepath)==False:
        #確定資料夾不存在，執行mkd()創建目錄
        ftp.mkd(remotepath)
        print('"'+remotepath+'" folder create completed!')
        return True
    else:
        print('"'+remotepath+'" folder has alread exist!')
        return False

""" 移除遠端目錄 """
def remove_folder(ftp,remotepath):
    if check_folder_exist(ftp,remotepath)!=False:
        #確定資料夾存在，執行rmd()移除目錄
        ftp.rmd(remotepath)
        print('"'+remotepath+'" folder remove completed!')
        return True
    else:
        print('"'+remotepath+'" folder dont exist!')
        return False

""" 小心使用!!! 移除path路徑內所有檔案與目錄 """
def remove_ftp_dir_all(ftp, path):
    #這是一個相當可怕的函式 會把path以下階層的所有檔案跟資料夾刪除
    #如果跟網管有仇可以試試 remove_ftp_dir_all(ftp,"/") 後果自負
    for (name, properties) in ftp.mlsd(path=path):
        if name in ['.', '..']:
            continue
        elif properties['type'] == 'file':
            ftp.delete(f"{path}/{name}")
        elif properties['type'] == 'dir':
            remove_ftp_dir_all(ftp, f"{path}/{name}")
    ftp.rmd(path)

""" 下載檔案 """
def downloadfile(ftp,remotepath,localpath):
    bufsize = 1024
    fp = open(localpath,'wb')
    ftp.retrbinary('RETR  '+ remotepath,fp.write,bufsize)
    # 接受服务器上文件并写入文本
    ftp.set_debuglevel(0) # 关闭调试
    fp.close() # 关闭文件

""" 上傳檔案 """
def uploadfile(ftp,remotepath,localpath):
    bufsize = 1024
    fp = open(localpath,'rb')
    ftp.storbinary('STOR '+ remotepath, fp,bufsize) # 上传文件
    ftp.set_debuglevel(0)
    fp.close()

def get_file_fullname(input_str1):
    return input_str1.split("\\")[-1]

def get_file_type(input_str2):
    return input_str2.split(".")[-1]
