from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<ClickableTextFieldRound>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        password: True
        icon_left: "key-variant"

    MDIconButton:
        icon: "eye-off"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            text_field.password = False if text_field.password is True else True


MDScreen:

    MDCard:
        orientation: "vertical"
        padding: 0, 0, 0 , "36dp"
        size_hint: .5, .5
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 4
        shadow_radius: 6
        shadow_offset: 0, 2

        MDBoxLayout:
            orientation: "vertical"
            spacing: "20dp"
            adaptive_height: True
            size_hint_x: .8
            pos_hint: {"center_x": .5, "center_y": .8}
        
            MDLabel:
                adaptive_size: True
                pos_hint: {"center_x": .5, "center_y": .5}
                text: "Bem Vindo!"
                allow_selection: True
                padding: "4dp", "4dp"
                bold: True
                font_style: "H5"
        
            MDTextField:
                id: text_field1
                mode: "round"
                hint_text: "Digite seu id"
                icon_left: "account-circle"
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint_x: .5
            
            MDTextField:
                id: text_field2
                mode: "round"
                hint_text: "senha"
                password: True
                pos_hint: {"center_x": .5, "center_y": .5}
                size_hint_x: .5
                icon_left: "key"

            MDRaisedButton:
                text: "Logar"
                
                on_release: app.switch_theme_style()
                on_release: app.log()
                pos_hint: {"center_x": .5}
            

            

'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style_switch_animation_duration = 0.8
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)

    def switch_theme_style(self):
        self.theme_cls.primary_palette = (
            "Orange" if self.theme_cls.primary_palette == "Red" else "Red"
        )
        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
        

    def get_input(self):
        self.usuario = self.root.ids.text_field1.text
        self.senha = self.root.ids.text_field2.text
        

    def log(self):
        self.usuario = self.root.ids.text_field1.text
        self.senha = self.root.ids.text_field2.text
        if self.usuario == '01' and self.senha == "12345":
            print("logado")
        elif self.usuario == '006' and self.senha == "54321":
            print("logado")
            

        ###Do it###
Example().run()

