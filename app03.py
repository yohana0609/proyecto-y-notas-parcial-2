from guizero import App, Text, PushButton

app = App("ICI App")

message = Text(app, text="Welcome to the ICI App")
button = PushButton(app, text="Click me")

app.display()
