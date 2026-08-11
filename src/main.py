import flet as ft
import time
from flet_webview_all import FletWebviewAll # Your custom extension control

def main(page: ft.Page):
    page.title = "WebView Distortion Fix"
    
    # Track the previous full_screen state
    page.data = {"was_fullscreen": page.window.full_screen}

    webview = FletWebviewAll(
        url="https://flet.dev",
        expand=True,
    )

    def on_page_resize(e):
        current_fullscreen = page.window.full_screen
        
        # Detect if a full-screen transition just took place
        if current_fullscreen != page.data["was_fullscreen"]:
            page.data["was_fullscreen"] = current_fullscreen
            
            # WORKAROUND: Force a layout refresh.
            # Toggling visible off/on breaks the stale DirectComposition buffer
            webview.visible = False
            page.update()
            
            # A tiny pause allows the window manager to finish layout
            time.sleep(0.05) 
            
            webview.visible = True
            page.update()

    page.on_resize = on_page_resize
    page.add(webview)
    page.update()

ft.run(main)
