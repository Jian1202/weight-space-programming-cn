"""启动本地中文博客；无需安装额外的 Python 依赖。"""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Timer
import webbrowser

根目录 = Path(__file__).resolve().parents[1]
处理器 = partial(SimpleHTTPRequestHandler, directory=str(根目录))
try:
    服务 = ThreadingHTTPServer(('127.0.0.1', 51973), 处理器)
except OSError:
    服务 = ThreadingHTTPServer(('127.0.0.1', 0), 处理器)
地址 = f'http://127.0.0.1:{服务.server_address[1]}/'
print(f'中文博客：{地址}\n关闭本窗口即可停止服务。')
Timer(0.5, lambda: webbrowser.open(地址)).start()
try:
    服务.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    服务.server_close()
