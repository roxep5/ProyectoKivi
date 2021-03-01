from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.filechooser import FileChooserIconView
from reportlab.pdfgen import canvas
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

        self.Aceptar.bind(on_press=self.vistapenlug)
        self.fotos = Button(text="FotosAceptar")
        self.fotos.bind(on_press=self.printerPersonas)
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
        self.gLayoutform.add_widget(self.fotos)
        self.gLayoutform.add_widget(self.Aceptar)
        self.vistaformpers.add_widget(self.gLayoutform)
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

        self.Aceptar.bind(on_press=self.vistapenlug)
        self.fotos = Button(text="FotosAceptar")

        self.fotos.bind(on_press=self.printerEventos)
        self.gLayoutform.add_widget(self.lblquien)
        self.gLayoutform.add_widget(self.lblquien2)

        self.gLayoutform.add_widget(self.lbldonde)
        self.gLayoutform.add_widget(self.lbldonde2)
        self.gLayoutform.add_widget(self.lblpersonas)
        self.gLayoutform.add_widget(self.lblpersonas2)
        self.gLayoutform.add_widget(self.fotos)
        self.gLayoutform.add_widget(self.Aceptar)
        self.vistaformpers.add_widget(self.gLayoutform)

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
        self.fotos = Button(text="FotosAceptar")
        self.Aceptar.bind(on_press=self.vistapenlug)
        self.fotos.bind(on_press=self.printerLugares)

        self.gLayoutform.add_widget(self.lblquien)
        self.gLayoutform.add_widget(self.lblquien2)

        self.gLayoutform.add_widget(self.lbldonde)
        self.gLayoutform.add_widget(self.lbldonde2)
        self.gLayoutform.add_widget(self.lblpersonas)
        self.gLayoutform.add_widget(self.lblpersonas2)

        self.gLayoutform.add_widget(self.fotos)
        self.gLayoutform.add_widget(self.Aceptar)

        self.vistaformpers.add_widget(self.gLayoutform)

        self.add_widget(self.vistaformpers)

    def vistaFinal(self, *args):
        self.remove_widget(self.vistaformpers)
        self.lable=Label(text=("hello!! "+self.lblquien2.text))
        self.add_widget(self.lable)

    def vistapenpers(self, *args):
        self.remove_widget(self.vistaformpers)
        self.box = BoxLayout(orientation="vertical")

        self.buscadorArch = FileChooserIconView(
            on_selection=self.select
        )

        self.box.add_widget(self.buscadorArch)

        self.add_widget(self.box)
    def vistapeneven(self, *args):
        self.remove_widget(self.vistaformpers)
        self.box = BoxLayout(orientation="vertical")

        self.buscadorArch = FileChooserIconView(
            on_selection=self.select
        )

        self.box.add_widget(self.buscadorArch)

        self.add_widget(self.box)
    def vistapenlug(self, *args):
        self.remove_widget(self.vistaformpers)
        self.box = BoxLayout(orientation="vertical")

        self.buscadorArch = FileChooserIconView(
            on_selection=self.select
        )

        self.box.add_widget(self.buscadorArch)

        self.add_widget(self.box)
    def select(self,filename):
        try:
            for i in filename:
                print("no funciona")
        except:
            pass





    def printerPersonas(self,*args):
        print("Pdf personas creado")
        self.rep=canvas.Canvas('pdf/Personas.pdf')
        self.rep.setFont('Helvetica-Bold',size=9)
        texto=('Apareces con: '+self.lblquien2.text)
        self.rep.drawString(100,750,texto)
        texto2=('Apareces en: '+self.lbldonde2.text)
        self.rep.drawString(100,600,texto2)
        texto = ('Apareces con: ' + self.lblquien2.text)
        self.rep.drawString(100, 350, texto)
        texto2 = ('Personas: ' + self.lblpersonas2.text)
        self.rep.drawString(100, 100, texto2)
        self.rep.save()
    def printerEventos(self,*args):
        print("Pdf eventos creado")
        self.rep=canvas.Canvas('pdf/Eventos.pdf')
        self.rep.setFont('Helvetica-Bold',size=9)
        texto=('Apareces con: '+self.lblquien2.text)
        self.rep.drawString(100,750,texto)
        texto2=('El evento es: '+self.lbldonde2.text)
        self.rep.drawString(100,500,texto2)
        texto = ('Te gusto: ' + self.lblquien2.text)
        self.rep.drawString(100, 250, texto)
        self.rep.save()
    def printerLugares(self,*args):
        print("Pdf Lugares creado")
        self.rep=canvas.Canvas('pdf/Lugar.pdf')
        self.rep.setFont('Helvetica-Bold',size=9)
        texto=('Apareces con: '+self.lblquien2.text)
        self.rep.drawString(100,750,texto)
        texto2=('Las sacaste en: '+self.lbldonde2.text)

        texto = ('Te gusto: ' + self.lblquien2.text)
        self.rep.drawString(100, 500, texto)
        self.rep.drawString(100,250,texto2)
        self.rep.save()
    pass

