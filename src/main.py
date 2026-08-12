import flet as ft
import time
from flet_webview_all import FletWebviewAll # Your custom extension control

def main(page: ft.Page):
    page.title = "WebView Distortion Fix" 
    page.add(
    FletWebviewAll(
        html="""
        <!doctype html>
        <html>
          <body>
          <h1>Hello from Flet</h1>
          <p>hello from flet webview all</p>
          <h2>hello</h2>
          <button>click me</button>
          </body>
        </html>
        """,
        expand=True,
    )
)

ft.run(main)
