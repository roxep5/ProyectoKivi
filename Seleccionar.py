from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from PreguntasPersonas import *
from PreguntasLugares import *
from PreguntasEventos import *
class Seleccionar(BoxLayout):
    def callback(self,event):
        if event=="persona":
            Funciona.prueba(self)
        elif event=="lugar":
            print("hola lugar")
        elif event=="evento":
            print("hola evento")


    pass