from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from PreguntasPersonas import *
from PreguntasLugares import *
from PreguntasEventos import *
from Seleccionar import *




class Preguntas(App):
    def build(self):
        '''self.load_kv('PreguntasPersonas.kv')
        return PreguntasPersonas()

        self.load_kv('PreguntasLugares.kv')
        return PreguntasLugares()
        '''
        '''self.load_kv('PreguntasEventos.kv')
        return PreguntasEventos()
        '''
        # self.load_kv('Seleccionar.kv')
        return Seleccionar()
Preguntas().run()
