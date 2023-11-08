import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Widget, Label
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup  import Popup

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation = 'vertical', padding = 80, spacing = 10)

        head_label = Label(text = "Registration", font_size =26, bold = True,
        height = 40)

        #adding lable
        name_label = Label(text = 'Name:',font_size = 24)
        self.name_input = TextInput(multiline = False, font_size = 24)

        surname_label = Label(text='Surname:', font_size=24)
        self.surname_input = TextInput(multiline=False, font_size=24)

        email_label = Label(text = 'Email:', font_size=22)
        self.email_input = TextInput(multiline=False, font_size=22)

        password_label = Label(text='Password:', font_size=20)
        self.password_input = TextInput(multiline=False, font_size=20, password = True)

        confirm_label = Label(text='Confirm Password:', font_size=20)
        self.confirm_input = TextInput(multiline=False, font_size=20 , password = True)

        #button
        submit_button = Button(text = 'Register', font_size = 30, on_press = self.register,
        background_color = 'blue')


        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(surname_label)
        layout.add_widget(self.surname_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(submit_button)

        return layout

    def register(self, instance):

        #Collect information
        name = self.name_input.text
        surname = self.surname_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_input.text

        # Validation
        if name.strip() == '' or email.strip() == '' or password.strip() == '' or  confirm_password.strip() == '' or surname.strip() == '':
            message = 'Please fill in all fields'

        elif password != confirm_password:
            message = 'Passwords are not same'

        else:
            filename = name + surname + '.txt'
            with open(filename, 'w') as file:
                file.write('Name: {}\n'.format(name))
                file.write('Surname: {}\n'.format(surname))
                file.write('Email: {}\n'.format(email))
                file.write('Password: {}\n'.format(password))
            message = "Registration successful\nName: {}\nEmail: {}".format(name,surname,email)

        #Pop-up
        pop_up = Popup(title = "Registration Status", content = Label(text = message),
        size_hint = (None,None), size = (400,200))
        pop_up.open()

        if password.strip() != confirm_password.strip():
            message = 'Passwords are incorrect'






if __name__=='__main__':
    RegistrationApp().run()
