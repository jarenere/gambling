from flask.ext.wtf import Form
from wtforms import TextField, RadioField, SubmitField, HiddenField
from wtforms.validators import Length, Optional


class Bet(Form):
    Label = ('hola')
    yesno = RadioField('Aceptas', choices=[('si','si'),('no','no')],validators = [Optional()])
    comment = TextField('Comentario', validators = [Length(min = 0, max = 140)])
    submit = SubmitField('Enviar')


def generateFormBet(bets,list,username):
    class MyBets(Form):
        submit = SubmitField('Enviar')


    for l in list:
        # setattr(F,"apuesta"+str(l),Label('apuesta'+str(l)))
        comment = ""
        if ('comentario',l) in bets :
            comment = "<br/><i>Comentario: </i>"+ bets['comentario',l]
        text = bets['apuesta',l] + "<br/><i>Cantidad: </i>"+ bets.get(('cantidad',l),"") +\
         " <i>Cuota: </i>" + bets.get(('cuota',l),"") + comment
        comment_default = ""
        # default = None
        # answared = False
        if (username, l) in bets:
            comment_default = bets[username,l]
        #     if bets[username,l].lower() in ['si', 'si']:
        #         default = 'si'
        #     elif bets[username,l].lower() in ['no','ne']:
        #         default = 'no'
        #     else:
        #         comment_default = bets[username,l]
        #     answared = True

        # setattr(MyBets,"yesno"+str(l),RadioField(text, choices=[('si','si'),('no','no'),('otro','otro')], default = default, validators = [Optional()]))
        setattr(MyBets,"comment"+str(l),TextField(text.decode("utf-8"), validators = [Length(min = 0, max = 140)], default = comment_default))
        # setattr(MyBets,"answared"+str(l),HiddenField('answared'+str(l),default=answared))
    form = MyBets()
    return form
  

