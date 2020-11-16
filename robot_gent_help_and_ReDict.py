"""
功能愈寫愈雜，怕之後會很難整理，寫了一個把foxModules裡面的函式輸出成文字說明的功能
"""
import os, re, sys
current_dir=os.path.dirname(os.path.abspath(__file__))

def gent_help(source_arr,output_doc,output_dict):
    #print(source_arr,output_doc)
    tmp_dict={}
    tmp_full_dict={}
    for i in source_arr:
        tmp_loc=current_dir+"\\foxModules\\"+i
        tmp_arr=open(tmp_loc,"r",encoding="utf-8").read().split("\n")
        print(i)
        is_init=False
        for j in range(2,len(tmp_arr)):
            if tmp_arr[j-2].find('"""')>-1 and tmp_arr[j-1].find('###')>-1:
                #print(tmp_arr[j-2])
                #print(tmp_arr[j-1])
                #print(tmp_arr[j])
                tmp_full_dict[re.sub(r'""" ([^\(]+)\([^\)]*\) """',r'\g<1>',tmp_arr[j-2].strip())]=[i,re.sub(r'""" ([^\(]+\([^\)]*\)) """',r'\g<1>',tmp_arr[j-2].strip()),re.sub(r'### ([^ ]+) ###',r'\g<1>',tmp_arr[j-1].strip()),preset_dict[i]+re.sub(r'def ([^\(]+\()self[,]*([^\)]*\)):',r'\g<1>\g<2>',tmp_arr[j].strip())]
                tmp_dict[re.sub(r'""" ([^\(]+)\([^\)]*\) """',r'\g<1>',tmp_arr[j-2].strip())]=preset_dict[i]+re.sub(r'def ([^\(]+)\([^\)]+\):',r'\g<1>',tmp_arr[j].strip())
    print("------------------------------")
    print("匯出函式說明完成!:"+output_doc)
    #print(str(tmp_full_dict))
    #讀取robot_gent_help_htm_header.txt
    htm_header=open(current_dir+"\\robot_gent_help_htm_header.txt","r",encoding="utf-8").read()
    with open(current_dir+"\\"+output_doc,"w+",encoding="utf-8") as f:
        #f.writelines('<!DOCTYPE html><html lang="zh-tw"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" /><meta http-equiv="X-UA-Compatible" content="ie=edge">\n')
        #f.writelines('</head><body>\n')
        f.write(htm_header)
        f.writelines('<script>\n')
        f.writelines('func_re_dict={\n')
        for k, v in tmp_full_dict.items():
            f.writelines('    "'+str(k)+'":'+str(v)+',\n')
        f.writelines('};\n')
        f.writelines('</script>\n')
        f.writelines('<script>\n')
        f.writelines('let open_close_div=(tmp_str)=>{\n')
        f.writelines('document.querySelector("."+tmp_str.replace("div","h3")).classList.toggle("on");\n')
        f.writelines('document.querySelector("."+tmp_str).classList.toggle("invisible");\n')
        f.writelines('};\n')
        f.writelines('</script>\n')
        tmp_num=0
        last_head=''
        for k, v in tmp_full_dict.items():
            v_arr=v
            if last_head=='':
                f.writelines('<div class="'+v_arr[0].replace(".py","")+'_title mod_title mod_title_on" onclick="open_close_div(\''+v_arr[0].replace(".py","")+'\')">'+v_arr[0]+'</div>\n')
                f.writelines('<div class="'+v_arr[0].replace(".py","")+'">\n')
            elif last_head!=v_arr[0]:
                f.writelines('</div><div class="'+v_arr[0].replace(".py","")+'_title  mod_title mod_title_on" onclick="open_close_div(\''+v_arr[0].replace(".py","")+'\')">'+v_arr[0]+'</div>\n')
                f.writelines('<div class="'+v_arr[0].replace(".py","")+'">\n')
            last_head=v_arr[0]
            #print(last_head,v_arr[0])
            f.writelines('<h3 class="h3_'+str(tmp_num)+' func_btn" onclick="open_close_div(\'div_'+str(tmp_num)+'\')">'+str(k)+'</h3><div class="div_'+str(tmp_num)+' invisible func_desc"><div class="func_desc1"><span class="desc_sub_title">語法範例</span>'+v_arr[1]+'</div><div class="func_desc2"><span class="desc_sub_title">用法說明</span>'+v_arr[2].strip().replace("###","")+'</div><div class="func_desc3"><span class="desc_sub_title">函式原形</span>'+v_arr[3]+'</div></div>\n')
            tmp_num+=1
        f.writelines('</div>\n')
        f.writelines('</body></html>')
    f.close()
    print("------------------------------")
    with open(current_dir+"\\foxModules\\"+output_dict,"w+",encoding="utf-8") as f:
        f.writelines('""" 中文函式轉換對照表(字典檔) """\n')
        f.writelines('func_re_dict={\n')
        for k, v in tmp_dict.items():
            f.writelines('    "'+k+'":"'+v+'",\n')
        f.writelines('    "#.*?\\n":"\\n"\n')
        f.writelines('}\n')
        #新建FuncReDictNew.py
    f.close()
    print("匯出FuncReDictNew.py完成!")

if __name__ == '__main__':
    preset_dict={
        "Gui.py":"g.",
        "WindowMgr.py":"w."
    }
    func_arr=[]
    for k, v in preset_dict.items():
        func_arr.append(k)
    gent_help(func_arr,"robot_func_help.htm","FuncReDict.py")