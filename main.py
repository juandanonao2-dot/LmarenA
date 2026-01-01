from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import gradio as gr
import threading

def echo(msg):
    return msg

iface = gr.Interface(fn=echo, inputs="text", outputs="text")

def run_gradio():
    iface.launch(server_name="0.0.0.0", server_port=7860)

class LMarenaApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')
        b.add_widget(TextInput(text='Gradio rodando em :7860', multiline=False))
        b.add_widget(Button(text='Sair', on_release=lambda x: App.get_running_app().stop()))
        return b

if __name__ == '__main__':
    threading.Thread(target=run_gradio, daemon=True).start()
    LMarenaApp().run()
