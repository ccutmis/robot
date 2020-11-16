""" 讀取config.ini參數 使用configparser模組將ini轉為dict並回傳 """
""" 如果讀入的參數值有%會報錯，改成%%就好了 """
import configparser
def ini_to_dict(ini_loc):
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(ini_loc,encoding='utf-8')
    sections=config.sections()
    tmp_dict={}
    for i in sections:
        options=config.options(i)
        for j in options:
            tmp_dict[i+'.'+j]=config[i][j]
    return tmp_dict
