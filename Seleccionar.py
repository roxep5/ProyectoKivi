from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class Seleccionar(BoxLayout):
    def callback(self,event):
        if event=="persona":
            print("Hola persona")
        elif event=="lugar":
            print("hola lugar")
        elif event=="evento":
            print("hola evento")


    pass