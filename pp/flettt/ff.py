import flet as ft
import subprocess
import platform

def open_file_explorer():
    system = platform.system()
    if system == "Darwin":  # macOS
        subprocess.run(["open", "/System/Applications/Finder.app"])
    elif system == "Windows":  # Windows
        subprocess.run(["explorer"])
    else:
        print("Sistem operasi tidak didukung untuk operasi ini.")

def main(page: ft.Page):
    page.title = "Aplikasi Flet dengan Integrasi File Explorer"
    
    def on_button_click(e):
        if name_input.value.lower() == "finder":
            open_file_explorer()
        else:
            greeting.value = f"Hello, {name_input.value}!"
            page.update()

    name_input = ft.TextField(label="Masukkan kata kunci:")
    greeting = ft.Text(value="Hello!", style="headlineMedium")
    greet_button = ft.ElevatedButton(text="Submit", on_click=on_button_click)

    page.controls.extend([name_input, greet_button, greeting])
    page.update()

ft.app(target=main)
