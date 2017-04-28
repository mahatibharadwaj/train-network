import htmlPy
from back_end import BackEnd 
from train import Ticket

app = htmlPy.AppGUI(
    title=u"Sample application")
app.maximized = True
app.template_path = "."
app.bind(BackEnd(app))
app.bind(Ticket(app))
app.template = ("index.html", {})

if __name__ == "__main__":
    app.start()
                    
                