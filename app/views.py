from app import app
from forms import generateFormBet
from flask import render_template, redirect, url_for
from decorators import valid_user

import gdata.spreadsheet.service
import gdata.service
import gdata.spreadsheet
from config import key, row_id, email, password

APUESTA = '2'
CANTIDAD = '5'
CUOTA = '6'
COMENTARIO = '17'
AREVALO = '7'
DANI = '8'
CHOB = '9'
CHUECA = '10'
EDU = '11'
RICHI = '12'
JULIO = '13'
BORJA = '14'
JAVI = '15'
NAME_COL ={'arevalo':7,'dani':8,'chob':9,'chueca':10,'edu':11,'richi':12,'julio':13,'borja':14,'javi':15}
# COL_NAME = {v: k for k, v in NAME_COL.items()}


spr_client = gdata.spreadsheet.service.SpreadsheetsService()
spr_client.email = email
spr_client.password = password
spr_client.source = 'Example CSV To Spreadsheet Writing Application'
spr_client.ProgrammaticLogin( )

@app.route('/')
@app.route('/index')
def index():
    return render_template('users.html')

@app.route('/<nickname>',methods=('GET', 'POST'))
@valid_user
def user(nickname):
    feed, dic, lista_id = getBets()
    # form = Bet()
    # form.yesno.data = 'no'
    form = generateFormBet(dic,lista_id,nickname)
    if form.validate_on_submit():
        update_excel(form,dic,lista_id,nickname)
        return redirect(url_for('user', nickname = nickname))
    return render_template('user.html',
        nickname =  "nickname",
        form = form,
        lista_id = lista_id)

def update_excel(form,dic,lista_id,nickname):
    spr_client = gdata.spreadsheet.service.SpreadsheetsService()
    spr_client.email = email
    spr_client.password = password
    spr_client.source = 'Example CSV To Spreadsheet Writing Application'
    spr_client.ProgrammaticLogin()
    for i in lista_id:
        if form["comment"+str(i)].data not in [None, ""]:
            if form["comment"+str(i)].data != dic.get((nickname,i)):
                #actualizar con el texto si es diferente a lo que habia antes
                spr_client.UpdateCell(i,NAME_COL[nickname], form["comment"+str(i)].data,key,row_id)



def getBets():
    #feed es un cuando con las distintas apuestas
    #dic es un diccionario, siendo la clave la tupla apusta/cantidad/cuota/nombre fila
    #lista_id contiene las filas con apuestas
    spr_client = gdata.spreadsheet.service.SpreadsheetsService()
    spr_client.email = email
    spr_client.password = password
    spr_client.source = 'Example CSV To Spreadsheet Writing Application'
    spr_client.ProgrammaticLogin( )
    # spr_client.UpdateCell(1,1,nickname,key,row_id)
    query = gdata.spreadsheet.service.CellQuery()
    query.min_col='2'
    query.max_col='17'
    query.min_row='5'
    feed = spr_client.GetCellsFeed(key = key, wksht_id = row_id, query = query)
    dic, lista = splitBet(feed)
    return feed, dic, lista

def splitBet(feed):
    dic = {}
    lista = []
    #apuesta
    for i, entry in enumerate(feed.entry):
      if isinstance(feed, gdata.spreadsheet.SpreadsheetsCellsFeed):
        if entry.cell.col == APUESTA:
            dic['apuesta',int(entry.cell.row)]= entry.content.text
            lista.append(int(entry.cell.row))
        elif entry.cell.col == CANTIDAD:
            dic['cantidad',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == CUOTA:
            dic['cuota',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == COMENTARIO:
            dic['comentario',int(entry.cell.row)]= entry.content.text
        # elif entry.cell.col in COL_NAME:
        #     dic[COL_NAME[entry.cell.col],int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == AREVALO:
            dic['arevalo',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == DANI:
            dic['dani',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == CHOB:
            dic['chob',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == CHUECA:
            dic['chueca',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == EDU:
            dic['edu',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == RICHI:
            dic['richi',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == JULIO:
            dic['julio',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == BORJA:
            dic['borja',int(entry.cell.row)]= entry.content.text
        elif entry.cell.col == JAVI:
            dic['javi',int(entry.cell.row)]= entry.content.text
    lista.sort(key=int)
    return dic, lista