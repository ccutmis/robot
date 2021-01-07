""" 中文函式轉換對照表(字典檔) """
func_re_dict={
    "找圖":"g.seek_img_and_click",
    "點滑鼠":"g.mouse_click",
    "移動滑鼠":"g.mouse_move",
    "拖拉滑鼠":"g.mouse_drag",
    "滑鼠中鍵":"g.mouse_scroll",
    "按組合鍵":"g.combo_key",
    "按鍵":"g.press_key",
    "按連續鍵":"g.typewrite",
    "彈出訊息":"g.alert_msg",
    "複制到暫存區":"g.copy_to_clipboard",
    "當前時間":"g.current_date_time",
    "當前滑鼠XY":"g.mouse_xy",
    "螢幕解析度":"g.screen_resolution",
    "螢幕截圖":"g.print_screen",
    "找視窗":"w.find_window_wildcard",
    "設cmd標題":"w.set_cmd_title",
    "當前視窗標題":"w.active_window_title",
    "視窗座標寬高":"w.get_window_pos_size",
    "設為前景":"w.set_foreground",
    "調視窗":"w.set_window_state",
    "設定寬高":"w.set_window_width_height",
    "休眠":"w.sleep_a_while",
    "結束程序":"w.end_process",
    "重置":"w.reset",
    "執行程式":"w.run_program",
    "設為最上層視窗":"w.set_window_on_top",
    "半透明視窗":"w.set_window_alpha",
    "#.*?\n":"\n"
}
