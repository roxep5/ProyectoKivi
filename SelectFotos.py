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
from kivy.core.window import Window

Builder.load_file('SelectFotos.kv')


class MyLayout3(Widget):
    pass


class MyApp3(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout3()


MyApp3().run()