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









class MyApp(App):



    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=75, padding=50)
        lbl = Label(text='BIENVENIDO/A A AVALANCHE',color= (1.5,1.35,0.9,2),font_size= 45)
        btn = Button(text='Empezar', size_hint=(0.17,0.3),pos_hint= {'center_x': 0.5},color= (1.5,1.6,0.9,2))
        btn1 = Button(text='Salir',size_hint=(0.17,0.3),pos_hint= {'center_x': 0.5},color= (1.5,1.6,0.9,2))

        layout.add_widget(lbl)
        layout.add_widget(btn)
        layout.add_widget(btn1)


        return layout






MyApp().run()