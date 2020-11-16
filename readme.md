# pyRobot 是什麼 ?

pyRobot 是使用Python開發的自動化腳本執行程式。

-----

# 為何要開發 pyRobot ?

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

# pyRobot 基本架構:

* pyRobot.exe (主程式)
* pyRobot_config.ini (設定要執行的腳本路徑)
* pyRobot_script.txt (預設腳本文件)
* pyRobot_func_help.htm (中文化函式說明文檔)

-----

# pyRobot 執行方式

pyRobot自動化程式有三種執行方式:

1. 用notepad++編輯 pyRobot_script.txt 完成後直接執行 pyRobot.exe即可。

2. 用notepad++編輯 自己命名的.txt文件(文件編碼需為utf-8)完成後用滑鼠拖拉這個文件到pyRobot.exe圖示上放開即執行此腳本。

3. pyRobot.exe 支援在cmd底下以pine方式執行語法，例如: pyRobot.exe -s "語法一|語法二|語法三"

-----

# pyRobot 取得方式

1. 下載主程式(支援Windows7 SP1 及 Windows10 的64位元版本) [下載pyRobot主程式](http://www.web3d.url.tw/pyRobot/pyRobot-exe.zip)

2. 若對主程式的安全有顧慮也可以下載原始碼自行用Pyinstaller編釋成執行檔 [下載pyRobot原始檔](http://www.web3d.url.tw/pyRobot/pyRobot-source-code.zip)

-----

# pyRobot_script.txt 編輯工具

基本上只要是能編輯utf-8編碼的純文件編輯器都可以使用(不建議使用微軟內建的記事本，存檔有時會自己把編碼變成utf-8 BOM或Big5造成執行失敗)，在此推薦一套由台灣團隊研發的免費軟體 Notepad++ [下載 Notepad++](https://notepad-plus-plus.org/downloads/)