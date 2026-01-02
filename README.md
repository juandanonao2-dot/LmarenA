# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import gradio as gr
import threading, webbrowser, time

def echo(msg):
    return msg

iface = gr.Interface(echo, "textbox", "text")

class LMarenaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.lbl = Label(text='Servidor Gradio iniciando…', size_hint_y=.3)
        layout.add_widget(self.lbl)
        return layout
    def on_start(self):threading.Thread(target=self.run_gradio, daemon=True).start()
    def run_gradio(self):
        time.sleep(1)
        iface.launch(server_name='0.0.0.0', server_port=7860, share=False, inline=False)
        self.lbl.text = 'Abra o navegador em http://localhost:7860'

if __name__ == '__main__':
    LMarenaApp().run()

# buildozer.spec
[app]
title = LMarena
package.name = lmarena
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
version = 1.0
requirements = python3,kivy,gradio,fastapi,uvicorn,pydantic,packaging
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 34
android.minapi = 24
android.ndk = 25.2.9519653
android.archs = arm64-v8a,armeabi-v7a
orientation = portrait# .github/workflows/build.yml
name: BuildAPK
on:
  push:
    branches: [ main ]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v4
        with: {python-version: '3.10'}
      - run: |
          sudo apt update
          sudo apt install -y openjdk-17-jdk zip unzip
          pip install buildozer Cython
      - run: buildozer android debug
      - uses: actions/upload-artifact@v3
        with:
          name: lmarena-apk
          path: bin/*.apk
 
