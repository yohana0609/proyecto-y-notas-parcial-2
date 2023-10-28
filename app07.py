#suma de dos numeros usando: Text,TextBox, PushButton, Info

from guizero import App, Text, TextBox, PushButton

def suma():
    app.info("Suma", text = f"La suma es {int(n1.value) + int(n2.value)}")
    #message_2.value = "Hola " + name.value

app = App(title="Suma de dos números")

msg_num_1 = Text(app, text="Introduce el primer número", color="purple")
n1 = TextBox(app)
msg_num_2 = Text(app, text="Introduce el segundo número", color="green")
n2 = TextBox(app)
#message_2 = Text(app)
button = PushButton(app, text="sumar",command=suma)


app.display()



