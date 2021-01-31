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


Builder.load_file('MenuSelect.kv')


class MyLayout2(Widget):
    pass


class MyApp2(App):
    def build(self):
        return MyLayout2()


MyApp2().run()