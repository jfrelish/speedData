from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'speedData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Jeffrey'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblSpeedData')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, speedData=result)


@app.route('/view/<int:speedData_id>', methods=['GET'])
def record_view(speedData_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblSpeedData WHERE id=%s', speedData_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', speedData=result[0])


@app.route('/edit/<int:speedData_id>', methods=['GET'])
def form_edit_get(speedData_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblSpeedData WHERE id=%s', speedData_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', speedData=result[0])


@app.route('/edit/<int:speedData_id>', methods=['POST'])
def form_update_post(speedData_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('speed.fldTheft_year'), request.form.get('speed.fldVeh_model'), speedData_id)
    sql_update_query = """UPDATE tblSpeedData t SET t.fldTheft_year = %s, t.fldVeh_model = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Height/Weight Form')


@app.route('/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    input_data = (request.form.get('fldTheft_year'), request.form.get('fldVeh_model'))
    sql_insert_query = """INSERT INTO tblSpeedData ( speed.fldTheft_year, speed.fldVeh_model) VALUES ( %s, %s) """
    cursor.execute(sql_insert_query, input_data)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/delete/<int:speedData_id>', methods=['GET'])
def form_delete_post(speeddata_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tblSpeedData WHERE id = %s """
    cursor.execute(sql_delete_query, speeddata_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/speedData', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblSpeedData')
    result = cursor.fetchall()
    json_result = json.dumps(result)
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/speedData/<int:speedData_id>', methods=['GET'])
def api_retrieve(speedData_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblSpeedData WHERE id=%s', speedData_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/speedData/', methods=['POST'])
def api_add() -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/v1/hw/<int:speedDatad_id>', methods=['PUT'])
def api_edit(speedDataid) -> str:
    resp = Response(status=201, mimetype='application/json')
    return resp


@app.route('/api/speedData/<int:speedData_id>', methods=['DELETE'])
def api_delete(speedData_id) -> str:
    resp = Response(status=210, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)