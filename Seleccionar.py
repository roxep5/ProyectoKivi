from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.filechooser import FileChooserIconView
from kivy.graphics import *
from PreguntasPersonas import *
from PreguntasLugares import *
from PreguntasEventos import *
class Seleccionar(BoxLayout):
    vistaformevent=BoxLayout()
    vistaformlugar=BoxLayout()
    vistaformpers=BoxLayout(orientation="vertical",padding=50,spacing=100)
    gLayoutform=GridLayout(cols=2,spacing=20)
    gLayoutToggle = GridLayout(cols=3, spacing=20)
    def __init__(self,**kwargs):
        super(Seleccionar, self).__init__(**kwargs)
        self.seleccionarVista=BoxLayout(orientation="vertical")
        self.btnpersonas=Button(text="Persona")
        self.btnlugar=Button(text="Lugar")
        self.btnevento=Button(text="Evento")
        self.btnpersonas.bind(on_press=self.personasSel)
        self.btnevento.bind(on_press=self.eventosSel)
        self.btnlugar.bind(on_press=self.lugaresSel)
        self.seleccionarVista.add_widget(self.btnpersonas)
        self.seleccionarVista.add_widget(self.btnevento)
        self.seleccionarVista.add_widget(self.btnlugar)
        self.add_widget(self.seleccionarVista)




    def personasSel(self,*args):
        self.remove_widget(self.seleccionarVista)

        self.lblquien=Label(
            text="¿Con quién apareces en estas fotos?",

        )
        self.lblquien2=TextInput(
            text=""
        )
        self.lbldonde=Label(
            text="¿Donde apareces en estas fotos?",

        )
        self.lbldonde2=TextInput(
            text=""
        )
        self.lblpersonas=Label(
            text="Personas",

        )
        self.lblrelacion = Label(
            text="Relacion",

        )
        self.tgbtnAmigos = ToggleButton(
            text="Amigos",
            group="relacion",
        )
        self.tgbtnFamilia = ToggleButton(
            text="Familia",
            group="relacion",
        )
        self.tgbtnPareja = ToggleButton(
            text="Pareja/s",
            group="relacion",
        )

        self.lblpersonas2=TextInput(
            text=""
        )
        with self.canvas:
            self.rect=Rectangle(pos=self.pos,size=self.size,source="imagenes/personas.jpg")
        self.Aceptar=Button(text="Aceptar")
        self.Aceptar.bind(on_press=self.algo)
        self.gLayoutToggle.add_widget(self.tgbtnAmigos)
        self.gLayoutToggle.add_widget(self.tgbtnFamilia)
        self.gLayoutToggle.add_widget(self.tgbtnPareja)

        self.gLayoutform.add_widget(self.lblquien)
        self.gLayoutform.add_widget(self.lblquien2)

        self.gLayoutform.add_widget(self.lbldonde)
        self.gLayoutform.add_widget(self.lbldonde2)
        self.gLayoutform.add_widget(self.lblrelacion)
        self.gLayoutform.add_widget(self.gLayoutToggle)
        self.gLayoutform.add_widget(self.lblpersonas)
        self.gLayoutform.add_widget(self.lblpersonas2)

        self.vistaformpers.add_widget(self.gLayoutform)
        self.vistaformpers.add_widget(self.Aceptar)

        self.add_widget(self.vistaformpers)
    def eventosSel(self,*args):
        self.remove_widget(self.seleccionarVista)

        self.lblquien = Label(
            text="¿Con quién apareces en estas fotos?",

        )
        self.lblquien2 = TextInput(
            text=""
        )
        self.lbldonde = Label(
            text="¿En qué evento apareces en estas fotos?",

        )
        self.lbldonde2 = TextInput(
            text=""
        )
        self.lblpersonas = Label(
            text="¿Cuánto te gustó ese evento",

        )

        self.lblpersonas2 = TextInput(
            text=""
        )
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size, source="imagenes/eventos.jpg")
        self.Aceptar = Button(text="Aceptar")

        self.gLayoutform.add_widget(self.lblquien)
        self.gLayoutform.add_widget(self.lblquien2)

        self.gLayoutform.add_widget(self.lbldonde)
        self.gLayoutform.add_widget(self.lbldonde2)
        self.gLayoutform.add_widget(self.lblpersonas)
        self.gLayoutform.add_widget(self.lblpersonas2)

        self.vistaformpers.add_widget(self.gLayoutform)
        self.vistaformpers.add_widget(self.Aceptar)

        self.add_widget(self.vistaformpers)

    def lugaresSel(self,*args):
        self.remove_widget(self.seleccionarVista)
        self.lblquien = Label(
            text="¿Con quién apareces en estas fotos?",

        )
        self.lblquien2 = TextInput(
            text=""
        )
        self.lbldonde = Label(
            text="¿En donde has sacado estas fotos?",

        )
        self.lbldonde2 = TextInput(
            text=""
        )
        self.lblpersonas = Label(
            text="¿Cuánto te gustó ese sitio",

        )

        self.lblpersonas2 = TextInput(
            text=""
        )
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size, source="imagenes/Lugares.jpg")
        self.Aceptar = Button(text="Aceptar")

        self.gLayoutform.add_widget(self.lblquien)
        self.gLayoutform.add_widget(self.lblquien2)

        self.gLayoutform.add_widget(self.lbldonde)
        self.gLayoutform.add_widget(self.lbldonde2)
        self.gLayoutform.add_widget(self.lblpersonas)
        self.gLayoutform.add_widget(self.lblpersonas2)

        self.vistaformpers.add_widget(self.gLayoutform)
        self.vistaformpers.add_widget(self.Aceptar)

        self.add_widget(self.vistaformpers)

    def vistaFinal(self, *args):
        self.remove_widget(self.vistaformpers)
        self.lable=Label(text=("hello"+self.lblquien2.text))
        self.add_widget(self.lable)

    def algo(self, *args):
        self.remove_widget(self.vistaformpers)
        self.box = BoxLayout(orientation="vertical")

        self.buscadorArch = FileChooserIconView(
            on_selection=self.select
        )

        self.box.add_widget(self.buscadorArch)

        self.add_widget(self.box)
    def select(self,*args):
        try: self.label.text=args[1][0]
        except:pass
    pass



'''class Filechooser(BoxLayout):

    def algo(self,*args):
        self.box = BoxLayout(orientation="vertical")

        self.buscadorArch=FileChooserIconView(
            on_selection=root.select(*args)
        )

        self.box.add_widget(self.buscadorArch)


        self.add_widget(box)
'''













'''class abrirFotos(BoxLayout):
    def vistaArch(self):
        self.box=BoxLayout(orientation="vertical")

        self.box2=BoxLayout(size_hint_y=None,height=30)

        self.cargar=Button(text="Cargar")
        self.guardar=Button(text="Guardar")

        self.box2.add_widget(self.cargar)
        self.box2.add_widget(self.guardar)

        self.box3=BoxLayout()

        self.input=TextInput(text='')


        self.box.add_wigdet(self.box2)
        self.add_widget(box)

    pass
'''
