from datetime import datetime
import pyautogui, pyperclip,PIL, time
pyautogui.PAUSE =0.1
pyautogui.FAILSAFE=True
class Gui:
    """ 建構式 """
    def __init__ (self):
        self._handle = None
        self.last_x=0
        self.last_y=0

    """ 找圖(img_url,seek_mode='infinite') """
    ### seek_mode若為'infinite'就會一直等，若為數字字串則會等N秒，例如seek_mode='2'會等圖2秒後跳出無限廻圈 ###
    def seek_img_and_click(self,img_url,seek_mode='infinite'):
        init_time=time.time()
        tmp_true_flag=True
        print(img_url)
        while tmp_true_flag:
            try:
                tmp_x,tmp_y=pyautogui.locateCenterOnScreen(img_url, grayscale=True)
            except:
                tmp_x=None
                tmp_y=None
            msg_str = 'tmp_x:'+str(tmp_x)+'\t'+'tmp_y:'+str(tmp_y)
            print(msg_str, end='')
            print('\b' * len(msg_str), end='', flush=True)
            if tmp_x==None:
                pass
            else:
                print('\n搜尋到'+img_url+'中心位置:'+str(tmp_x)+','+str(tmp_y))
                pyautogui.click(tmp_x,tmp_y)
                self.last_x,self.last_y=[tmp_x,tmp_y]
                tmp_true_flag=False
            #time.sleep(0.1)
            #若 seek_mode不為'infinite'就計算目前seek_mode乘4的值是否大於tmp_counter，若大於就跳出廻圈
            if seek_mode!='infinite':
                ct= time.time()
                diff = int(ct-init_time)
                if diff>int(seek_mode):
                    tmp_true_flag=False

    """ 點滑鼠(x_pos,y_pos,click_num=1,sec_between=0.2,btn='left') """
    ### 點滑鼠函式說明 ###
    def mouse_click(self,x_pos,y_pos,click_num=1,sec_between=0.2,btn='left'):
        if btn=='left' or btn=='right':
            pyautogui.click(x=x_pos,y=y_pos,clicks=click_num,interval=sec_between,button=btn)
        else:
            self.alert_msg("點滑鼠 mouse_click 函式的btn參數有誤")
            pass

    """ 移動滑鼠(tx,ty,dur=1,coord='abs') """
    ### 移動滑鼠(x,y,秒數,絕對或相對座標) ###
    def mouse_move(self,tx,ty,dur=1,coord='abs'):
        if coord=='abs':
            pyautogui.moveTo(tx,ty,duration=dur)
        elif coord=='rel':
            pyautogui.moveRel(tx,ty,duration=dur)
        else:
            self.alert_msg("移動滑鼠 mouse_move 函式的coord參數需為 'abs' 或 'rel'")
            pass
        self.last_x,self.last_y=pyautogui.position()

    """ 拖拉滑鼠(tx,ty,dur=1,coord='abs',button='left') """
    ### 拖拉滑鼠(x,y,秒數,絕對或相對座標,左鍵或右鍵) ###
    def mouse_drag(self,tx,ty,dur=1,coord='abs',button='left'):
        if button not in ['left','right']:
            self.alert_msg("拖曳滑鼠 mouse_drag 函式的button參數需為 'left' 或 'right'")
            return False
        if coord=='abs':
            pyautogui.dragTo(tx,ty,duration=dur,button=button)
        elif coord=='rel':
            pyautogui.dragRel(tx,ty,duration=dur,button=button)
        else:
            self.alert_msg("拖曳滑鼠 mouse_drag 函式的coord參數需為 'abs' 或 'rel'")
            pass
        self.last_x,self.last_y=pyautogui.position()

    """ 滑鼠中鍵(amount_to_scroll,scroll_x=0,scroll_y=0) """
    ### amount_to_scroll正值往上滾動負值往下滾動 ###
    def mouse_scroll(self,amount_to_scroll,scroll_x=0,scroll_y=0):
        pyautogui.scroll(amount_to_scroll,x=scroll_x,y=scroll_y)

    """ 按組合鍵(tmp_hot_key,tmp_key) """
    ### 按組合鍵函式說明 ###
    def combo_key(self,tmp_hot_key,tmp_key):
        pyautogui.hotkey(tmp_hot_key,tmp_key)

    """ 按鍵(tmp_key,repeat=1) """
    ### 按鍵函式說明 ###
    def press_key(self,tmp_key,repeat=1):
        pyautogui.press(tmp_key,presses=repeat)

    """ 按連續鍵(tmp_str,sec_between=0) """
    ### 按連續鍵函式說明 ###
    def typewrite(self,tmp_str,sec_between=0):
        pyautogui.typewrite(tmp_str,interval=sec_between)

    """ 彈出訊息(tmp_msg,tmp_title='MESSAGE') """
    ### 彈出函式說明 ###
    def alert_msg(self,tmp_msg,tmp_title='MESSAGE'):
        pyautogui.alert(text=tmp_msg, title=tmp_title, button='OK')

    """ 複制到暫存區(tmp_str) """
    ### 複制到暫存區函式說明 ###
    def copy_to_clipboard(self,tmp_str):
        pyperclip.copy(tmp_str)

    """ 當前時間(t_str="%Y%m%d%H%M%S") """
    ### 傳回當前日期時間，可用t_str決定輸出的日期時間格式，若t_str為空白則直接輸出年月日時分秒。<br/> exam: YYYYmmddHHmmss 20201023083159 ###
    def current_date_time(self,t_str="%Y%m%d%H%M%S"):
        return datetime.now().strftime(t_str)

    """ 將timestamp轉成格式化時間字串 """
    def timestampToDateStr(self,arg,format_str="%Y%m%d"):
        """ 這是從 escodeUpload 提取出來的 不對外提供 """
        dt_object = datetime.fromtimestamp(int(arg))
        return dt_object.strftime(format_str)

    """ 將dateStr轉成Datetime (日期時間格式) """
    def dateStrToDatetime(self,arg):
        """ 這是從 escodeUpload 提取出來的 不對外提供 """
        return datetime.strptime(arg, "%Y/%m/%d %H:%M")

    """ 將datetime轉成timestamp (int格式) """
    def datetimeToTimestamp(self,arg):
        """ 這是從 escodeUpload 提取出來的 不對外提供 """
        return int(datetime.timestamp(arg))
        #print(datetimeToTimestamp(dateStrToDatetime(timestamp)))

    """ 當前滑鼠XY() """
    ### 傳回當前滑鼠XY座標，例如:x,y=當前滑鼠XY() ###
    def mouse_xy(self):
        return pyautogui.position()

    """ 螢幕解析度() """
    ### 傳回螢幕[width,height] exam: w,h=螢幕解析度() ### 
    def screen_resolution(self):
        return pyautogui.size()

    """ 螢幕截圖(save_loc='圖檔名稱') """
    ### 將當前螢幕截圖，若無'圖檔名稱'則傳回螢幕截圖的圖資，可供PIL作後續處理 ###
    def print_screen(self,save_loc=''):
        if save_loc=='':
            return pyautogui.screenshot()
        else:
            pyautogui.screenshot().save(save_loc)
