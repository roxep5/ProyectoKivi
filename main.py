from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from PreguntasPersonas import *




class FFFF(App):
    def build(self):
        self.load_kv('PreguntasPersonas.kv')
        return PreguntasPersonas()


FFFF().run()
