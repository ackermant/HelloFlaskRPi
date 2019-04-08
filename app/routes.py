from app import app
from app.forms import RegInputForm
from flask import Flask, render_template, flash, redirect, url_for
from app.smartymodbusreader import MyConnection

@app.route("/smartyconnect")
def connectiontest():
    myconnection = MyConnection()
    testconnect = myconnection.testconnection()
    if(testconnect):
        result = "ModbusTCP connection established"
    else:
        result = "ModbusTCP connection established"
    return render_template('connectiontestresult.html', result=result)



@app.route('/reginput', methods=['GET', 'POST'])
def reginput():
    registervalue = "No value found"
    form = RegInputForm()
    if form.validate_on_submit():
        myconnection = MyConnection()
        regnum = form.registerno.data
        registervalue = myconnection.readregister(regnum)
        templateData = {
            'regvalue': registervalue
        }
        return render_template('regval.html', **templateData)
    return render_template('smartyregin.html', title='Enter Smarty Register Number', form=form)