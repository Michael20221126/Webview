# coding = utf-8
import webview
with open(".\config.json", "r", encoding="utf-8") as file:
    data = file.read()
config = str()
exec("config = " + data)

webview.create_window(title=config['window']['title'],
                      url=config['window']['url'],
                      width=config['window']['width'],
                      height=config['window']['height'],
                      resizable=config['size']['resizable'],
                      fullscreen=config['size']['fullscreen'],
                      min_size=config['size']['min_size'],
                      frameless=config['frameless']['frameless'],
                      easy_drag=config['frameless']['easy_drag'],
                      minimized=config['state']['minimized'],
                      on_top=config['state']['on_top'],
                      confirm_close=config['state']['confirm_close'],
                      background_color=config['web']['background_color'],
                      transparent=config['web']['transparent'],
                      text_select=config['web']['text_select']
                      )
webview.start()
