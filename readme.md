# 更新測試: 2020-11-27

# Robot 是什麼 ?

Robot 是使用Python開發的自動化腳本執行程式。

-----

# 為何要開發 Robot ?

在 Python 裡如果要操控鍵盤滑鼠或尋找特定圖片是否在畫面上顯示通常會用到 pyautogui 模組，而要切換視窗(例如最大化視窗，將目標視窗置頂等等)則會用到 pywin32 模組。

在 Windows 作業系統要實現自動化通常會混合鍵盤滑鼠切換視窗等動作，因此想把這兩個模組綁在一起，再把函式封裝成用中文化函式來執行，讓使用者即使不熟悉Python程式也可以輕鬆編寫自動化腳本文件，例如:

```
w.sleep_a_while(tmp_sec)
可寫成
休眠(tmp_sec)
上面這句中文化函式可以讓程式暫停 tmp_sec 秒
```

當然腳本文件除了可以用中文函式來編寫之外，也支援Python基本語法，例如:

```
for i in range(0,5):print(i)

上面執行結果:
0
1
2
3
4
```

-----

# Robot 基本架構:

* robot.exe (主程式)
* robot_config.ini (設定要執行的腳本路徑)
* robot_script.txt (預設腳本文件)
* robot_func_help.htm (中文化函式說明文檔)

-----

# Robot 執行方式

robot自動化程式有三種執行方式:

1. 用notepad++編輯 robot_script.txt 完成後直接執行 robot.exe即可。

2. 用notepad++編輯 自己命名的.txt文件(文件編碼需為utf-8)完成後用滑鼠拖拉這個文件到robot.exe圖示上放開即執行此腳本。

3. robot.exe 支援在cmd底下以pine方式執行語法，例如: robot.exe -s "語法一|語法二|語法三"

-----

# Robot 取得方式:

1. 下載主程式(支援Windows7 SP1 及 Windows10 的64位元版本) [下載robot主程式](https://ccutmis.github.io/robot-exe.zip)

2. 若對主程式的安全有顧慮也可以下載原始碼自行用Pyinstaller編釋成執行檔 [下載robot原始檔](https://ccutmis.github.io/robot-source-code.zip)

-----

# robot_script.txt 編輯工具

基本上只要是能編輯utf-8編碼的純文件編輯器都可以使用(不建議使用微軟內建的記事本，存檔有時會自己把編碼變成utf-8 BOM或Big5造成執行失敗，如果你用記事本編輯的文字檔在執行時發生錯誤，請檢查文字檔的文件編碼是否為'utf-8'格式，不可為'utf-8 BOM'或其它編碼)，在此推薦一套由台灣團隊研發的免費軟體 Notepad++ [下載 Notepad++](https://notepad-plus-plus.org/downloads/)
