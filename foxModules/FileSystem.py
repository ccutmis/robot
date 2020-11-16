""" FileSystem.py 說明 創建日期:2020/10/27
    用途: 作為本地端目錄與檔案管理的常用功能進行函式化封裝
"""
import os,shutil,codecs

def current_loc():
    return os.path.abspath(os.getcwd())

""" 移除目錄 """
def remove_loc_dir(dir_loc):
    if os.path.exists(dir_loc):
        shutil.rmtree(dir_loc)
        print("[OK]移除目錄:"+dir_loc)
        return True
    else:
        print("[XX]不存在目錄:"+dir_loc)
        return False

""" 創建目錄 """
def create_loc_dir(dir_loc):
    if not os.path.exists(dir_loc):
        os.makedirs(dir_loc)
        print("[OK]新建目錄:"+dir_loc)
        return True
    else:
        print("[XX]已存在目錄:"+dir_loc)
        return False

""" 列出dir_loc目錄所有檔案，可用allow_file_type指定檔案副檔名類型 """
def dir_list(dir_loc,allow_file_type=[]):
    tmp_list=[]
    #print('allow_file_type length:'+len(allow_file_type))
    for path, subdirs, files in os.walk(dir_loc):
        for name in files:
            is_match=False
            if len(allow_file_type)>0: 
                if get_file_type(name) in allow_file_type:
                    is_match=True
            else:
                is_match=True
            if is_match==True:
                tmp_list.append(os.path.join(path, name))
    return tmp_list

""" 將 src 的編碼 src_encoding 轉成 dst_encoding 然後另存為 dst """
def change_txt_encoding(src,dst,src_encoding,dst_encoding,BLOCKSIZE=1048576):
     # or some other, desired size in bytes
    with codecs.open(src, "r", src_encoding) as sourceFile:
        with codecs.open(dst, "w", dst_encoding) as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)

""" 逐行讀取文字檔並傳回陣列 """
def read_file_into_list(file_loc,write_mode="r",encode_set="utf-8",split_char="\n"):
    tmp_list=open(file_loc,write_mode,encoding=encode_set).read().split(split_char)
    return tmp_list

""" 將陣列元素逐行寫入文字檔 """
def write_file_from_list(file_loc,tmp_list=[],write_mode="w+",encode_set="utf-8"):
    if len(tmp_list)!=0:
        with open(file_loc,write_mode,encoding=encode_set) as f:
            for i in tmp_list:
                #try:
                f.writelines(i+'\n')
                #except:
                #    print('error:'+i)
                #    input("===========")
        f.close()
        print("[ OK ] 陣列寫入文字檔 "+get_file_fullname(file_loc)+" 完成!  文件編碼:"+encode_set+"")
    else:
        print("[ XX ] 陣列寫入文字檔 "+get_file_fullname(file_loc)+" 失敗!")
        return False

""" 複制檔案(原檔案完整路徑,新檔案完整路徑) """
def cope_file(src,dest):
    """ 假如複制成功會傳回True否則傳回False """
    try:
        shutil.copyfile(src, dest)
        return True
    except:
        return False
""" 檔案大小(file_path) """
def get_file_size_in_bytes(file_path):
   """ Get size of file at given path in bytes"""
   size = os.path.getsize(file_path)
   return size

""" 取得完整檔名(不含路徑) """
def get_file_fullname(input_str1):
    return input_str1.split("\\")[-1]

""" 取得副檔名 """
def get_file_type(input_str2):
    return input_str2.split(".")[-1]