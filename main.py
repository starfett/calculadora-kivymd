from kivy.config import Config

Config.set('graphics', 'resizable',False)

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineListItem

Window.size = (360, 540)


class Tela(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validando_operador(self, operador, conta):
        if len(conta) > 0 and conta[-1] in "+-/*" :
            return conta
        return conta+operador

    def verifica_operador(self, operador):
        if self.ids.numeros.text == "":
            return self.ids.valor_operado.text
        if self.ids.valor_operado.text=="" or self.ids.valor_operado.text[-1] not in ["*", "/", "+", "-"]:
            return self.ids.numeros.text+ F" {operador}"
        return self.calcular(F" {operador}")

    def verifica_real(self):
        numero_atual = self.ids.numeros.text
        if self.ids.numeros.text == "":
            self.ids.numeros.text = "0"
        if "," in numero_atual:
            return self.ids.numeros.text
        return self.ids.numeros.text+","

    def puxar_conta_do_historico(self):
        ...

    def calcular(self, operador="", click=False):
        valor_total = 0
        valor_operado = self.ids.valor_operado.text.replace(",", ".")
        valor_atual = self.ids.numeros.text.replace(",", ".")

        if self.ids.valor_operado.text != "" and self.ids.numeros.text != "" and  self.ids.valor_operado.text[-1] in ["*", "/", "+", "-"]:
            if self.ids.valor_operado.text[-1] == "/":
                valor_operado = valor_operado.replace(" /", "")
                valor_total = float(valor_operado) / float(valor_atual)

            if self.ids.valor_operado.text[-1] == "*":
                valor_operado = valor_operado.replace(" *", "")
                valor_total = float(valor_operado) * float(valor_atual)

            if self.ids.valor_operado.text[-1] == "+":
                valor_operado = valor_operado.replace(" +", "")
                valor_total = float(valor_operado) + float(valor_atual)

            if self.ids.valor_operado.text[-1] == "-":
                valor_operado = valor_operado.replace(" -", "")
                valor_total = float(valor_operado) - float(valor_atual)
            self.ids.lista_do_historico.add_widget(LinhaDoHistorico(text=F"{self.ids.valor_operado.text} {self.ids.numeros.text} = {valor_total}"))
            return F"{valor_total}{operador}"
        return self.ids.valor_operado.text

class LinhaDoHistorico(OneLineListItem):
    def __init__(self, **kargs):
        super().__init__(**kargs)

class Calculadora(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.primary_hue = "500"
        return Tela()



Calculadora().run()
