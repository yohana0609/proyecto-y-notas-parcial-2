from guizero import App, Text, TextBox

app = App(title="ICI App")

message = Text(app, text="¿Cómo te llamas?")
name = TextBox(app)

#button = PushButton(app, text="Click me!", command=say_hello)


app.display()

