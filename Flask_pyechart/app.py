# -*- coding:utf-8 -*-
from flask import Flask,request,redirect,jsonify,render_template,Response,make_response
import json
import os
from shutil import copytree,rmtree
import pandas as pd

app = Flask(__name__)



list = ['殡葬类单位数','分省城区面积','每年度殡葬类职工总数（人)','殡葬类单位数+火化炉与火化数对比']

@app.route('/',methods=['GET'])
def index():
    return redirect('/funeral_units')

@app.route('/funeral_units',methods=['GET'])
def funeral_units():
    result = pd.read_csv( 'csv/Funeral_Units.csv', encoding='gbk', delimiter="," )
    data = result.to_html( )
    return render_template( 'funeral_units.html', the_res=data, list=list )


@app.route('/urban',methods=['GET'])
def urban():
    result = pd.read_csv( 'csv/urban_area.csv', encoding='gbk', delimiter="," )
    data = result.to_html( )
    return render_template( 'urban.html', the_res=data, list=list )

@app.route('/total',methods=['GET'])
def total():
    result = pd.read_csv( 'csv/分省年度殡葬类职工总人数（人）.csv', encoding='gbk', delimiter="," )
    data = result.to_html( )
    return render_template( 'total.html', the_res=data, list=list )

@app.route('/comparison',methods=['GET'])
def comparison():
    result = pd.read_csv( 'csv/Annual_funeral_industry.csv', encoding='gbk', delimiter=',')
    data = result.to_html( )
    return render_template( 'comparison.html', the_res=data, list=list)

@app.route('/skip',methods=['POST'])
def skip():
    option = request.form['option']
    if option == "殡葬类单位数":
        return redirect('/funeral_units')
    elif option == "分省城区面积":
        return redirect('/urban')
    elif option == "每年度殡葬类职工总数（人)":
        return redirect('/total')
    elif option == "殡葬类单位数+火化炉与火化数对比":
        return redirect('/comparison')
    else:
        return "异常"

if __name__ == '__main__':
    app.run(debug=True,port=8080)