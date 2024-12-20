# import win32gui  # 用于窗口和控件操作
# import win32api  # 用于 Win32 API 操作
# import win32con  # 用于一些常量操作
# import time      # 用于延

# hwnds = []
# def call(w,e) :
#     clz = win32gui.GetClassName(w)
#     txt = win32gui.GetWindowText(w)
#     print(clz, txt)
#     if(clz ==  'WindowsForms10.EDIT.app.0.1e09f85_r7_ad1'):
#         hwnds.append(w)
        
#         value_to_send = "未Hello, World!11123231--" + str(len(hwnds))  # 你想输入的文本
#         win32gui.SendMessage(w, win32con.WM_SETTEXT, 0, value_to_send)

#     pass
# hwnd1 = win32gui.FindWindow("WindowsForms10.Window.8.app.0.1e09f85_r7_ad1", "AreaCity Geo格式转换工具 Ver:1.3.240505")
# # hwnd1 = win32gui.FindWindowEx(hwnd1, 0, "WindowsForms10.Window.8.app.0.1e09f85_r7_ad1", None)


# # win32gui.EnumChildWindows(hwnd1, call, None)
# win32gui.EnumChildWindows(hwnd1, call, None)

 
# value_to_send = "ad" + str(len(hwnds))  # 你想输入的文本
# win32gui.SendMessage(hwnds[5], win32con.WM_SETTEXT, 0, value_to_send)
