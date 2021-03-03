from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image,AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics.vertex_instructions import Rectangle
from kivy.clock import Clock







class Vistas(BoxLayout):
    vistaMenu=BoxLayout()
    VistaSelect=BoxLayout(orientation='vertical', spacing=20, padding=50)
    VistasFotos=BoxLayout(orientation='vertical', spacing=20, padding=50)

    def __init__(self, **kwargs):
        super(Vistas, self).__init__(**kwargs)

        self.vistaMenu=BoxLayout(orientation='vertical', spacing=20, padding=50)

        self.lbl = Label(text='BIENVENIDO/A A AVALANCHE', color=(1.5, 1.35, 0.9, 2), font_size=45)
        self.btn = Button(text='Empezar', size_hint=(0.17, 0.3), pos_hint={'center_x': 0.5}, color=(1.5, 1.6, 0.9, 2))


        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size,source='Imagenes/Avalanche.png')


        self.btn.bind(on_press=self.Seleccionar)


        self.vistaMenu.add_widget(self.lbl)
        self.vistaMenu.add_widget(self.btn)

        self.add_widget(self.vistaMenu)

    def Seleccionar(self, *args):
        self.remove_widget(self.seleccionarMenu)

        self.lbl = Label(text='¿Que tipo de presentacion deseas?', color=(1.5, 1.35, 0.9, 2), font_size=30)
        self.btn1 = Button(text='Personas', size_hint=(0.35, 0.3), pos_hint={'center_x': 0.5},
                      color=(1.5, 1.6, 0.9, 2))
        self.btn2 = Button(text='Lugares', size_hint=(0.35, 0.3), pos_hint={'center_x': 0.5},
                      color=(1.5, 1.6, 0.9, 2))
        self.btn3 = Button(text='Eventos', size_hint=(0.35, 0.3), pos_hint={'center_x': 0.5},
                           color=(1.5, 1.6, 0.9, 2))
        self.btn4 = Button(text='Continuar ->', size_hint=(0.17, 0.25), pos_hint={'center_x': 0.9}, color=(1.5, 1.6, 0.9, 2))

        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size,source='Imagenes/bosque.png')


        self.btn1.bind(on_press=self.Seleccionar)
        self.btn2.bind(on_press=self.Seleccionar)
        self.btn3.bind(on_press=self.Seleccionar)
        self.vistaSelect.add_widget(self.lbl)
        self.vistaSelect.add_widget(self.btn1)
        self.vistaSelect.add_widget(self.btn2)
        self.vistaSelect.add_widget(self.btn3)
        self.vistaSelect.add_widget(self.btn4)
        self.add_widget(self.vistaSelect)

    def Fotos(self, *args):
        self.remove_widget(self.seleccionarMenu)

        self.img = Image(source='Imagenes/icono.png', pos_hint={'center_x': 0.5})

        self.btn1 = Button(text='Elija sus fotos', size_hint=(0.35, 0.3), pos_hint={'center_x': 0.5},
                      color=(1.5, 1.6, 0.9, 2))
        self.btn2 = Button(text='Ver numero de fotos seleccionadas', size_hint=(0.35, 0.3), pos_hint={'center_x': 0.5}, color=(1.5, 1.6, 0.9, 2))
        self.btn4 = Button(text='Continuar ->', size_hint=(0.17, 0.25), pos_hint={'center_x': 0.9}, color=(1.5, 1.6, 0.9, 2))

        self.vistaFotos.add_widget(self.img)
        self.vistaFotos.add_widget(self.btn1)
        self.vistaFotos.add_widget(self.btn2)
        self.vistaFotos.add_widget(self.btn3)
        self.vistaFotos.add_widget(self.btn4)

Vistas().run()