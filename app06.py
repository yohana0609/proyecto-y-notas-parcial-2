from guizero import App, Text, TextBox, PushButton

def say_hello():
    app.info("Saludo", text = f"Hola {name.value}")
    #message_2.value = "Hola " + name.value

app = App(title="ICI App")

message = Text(app, text="¿Cómo te llamas?", color="blue")
name = TextBox(app, width=30, height=1, multiline=True)
message_2 = Text(app)
button = PushButton(app, text="Click me!",command=say_hello)


app.display()

