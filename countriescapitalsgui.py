# pyjamas gui
# app pyjamas countriescapitals index

import mywidgets as w
import countriescapitals as n

def start(sender):
    mainpanel.clear()
    dialog.setText(n.start_game())
    mainpanel.add(dialog)
    mainpanel.add(answerbox)
    mainpanel.add(answerbutton)
    return

def answer(sender):
    a = answerbox.getText()
    dialog.setText(n.answer_question(a))
    answerbox.setText("")
    
welcome = w.label("Welcome To Countries Capitals Quiz")
startbutton = w.labelbutton("Click Here To Start",start)
answerbutton = w.labelbutton("Submit Answer",answer)

dialog = w.label("")
answerbox = w.textbox()

mainpanel = w.verticalpanel()
mainpanel.setHorizontalAlignment("center")
mainpanel.add(welcome)
mainpanel.add(startbutton)

w.rootadd(mainpanel)
