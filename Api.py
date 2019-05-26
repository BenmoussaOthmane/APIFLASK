from flask import Flask,jsonify,request,make_response,render_template
from flask_sqlalchemy import SQLAlchemy
import uuid
from werkzeug.security import generate_password_hash , check_password_hash

import json
import os




#  Name APP
app = Flask(__name__ ,  template_folder ="/Users/benmoussaothmane/Desktop/Flask_API/template")

app.config['SECRET_KEY'] ='thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/benmoussaothmane/Desktop/Flask_API/mac.db'
db= SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    public_id = db.column(db.String(50))
    name = db.column(db.String(50))
    pasword = db.column(db.String(50))
@app.route('/user' , methods = ['GET'])
def get_all_User():
    users =User.query.all()
    output = []
    for user in users:

        user_data = {}
        user_data['name'] = user.name
        user_data['public_id'] = user.public_id
        user_data['pasword'] = user.pasword
        output.append(user_data)
    return jsonify({'users' : output})





@app.route('/user/<id>',methods = ['GET'])
def oneUser(id):
    user = User.query.filter_by(id = id).first()
    if not user:
        return jsonify({'messeg' : 'not existe User'})
    
    user_data = {}
    user_data['name'] = user.name
    user_data['public_id'] = user.public_id
    user_data['pasword'] = user.pasword
    return jsonify({'user' : user_data})



#  Name APP



###########  PARCING LE FICHER JSON EN DICTIONARY  ##############

CWd = os.getcwd()


#  pour acceder le path de fichier JSON
pathjson = '%s/%s' % (CWd , 'Imac.json')

# declari un dictioner vide 
dictioner = {}

try:
    with open(pathjson) as datefile:
        dictioner=json.load(datefile)
except IOError:
    print("EROOOOR")




# cration index de API
@app.route('/' , methods = ['GET'])
def indeex():
    return render_template("index.html")



# les marque de Imac
@app.route('/Imac' , methods = ['GET'])
def Imac():
    return jsonify({'Imac' : dictioner})



#  acceder  3La hsab Id 
@app.route('/Imac/<int:Id>' , methods = ['GET'])
def Oneid(Id):
    i = [id for id in dictioner if id['Id'] == Id]
    return jsonify({'Imac' : i})






# acceder le Imac 3la hsab Proce

@app.route('/Imac/price/<string:price>' , methods = ['GEt'])
def PriceImac(price):
    onne = [dico for dico in dictioner if dico['price'] == price]
    return jsonify({'Imac' : onne})



# acceder  a name de cette Imac
@app.route('/Imac/etoil/<string:Etiol>' , methods = ['GET'])
def OneEtoil(Etiol):

    n = [name for name in dictioner if name['Etiol'] == Etiol]
    return jsonify({"Imac" : n})




# accder le nome de Imac
@app.route('/Imac/name/<string:Name>' , methods = ['GET'])
def Onename(Name):
    nome = [name for name in dictioner if name['Name'] == Name]
    return jsonify({'Imac' : nome})


#  Inser un neveau Imac 
@app.route('/Imac/insert' , methods = ['POST'])
def addOn():
    Nv = {'Name' : request.json['Name'],
           'price' : request.json['price'],
           'Etiol' : request.json['Etiol'],
           'Id' : request.json['Id']
    }
    dictioner.append(Nv)
    return jsonify({'Imac' : dictioner})


# Update un marque de APPl 3la hsab Id
@app.route('/Imac/<string:price>'  , methods = ['PUT'])
def Updet(price):
    mod = [mod for mod in dictioner if mod['price'] == price]
    mod[0]['price'] = request.json['price']
    return jsonify({'Imac':mod[0]})

# delait un marque de apple 
@app.route('/Imac/sup/<int:Id>' , methods = ['DELETE'])
def sup(Id):
    S = [d for d in dictioner if d['Id'] == Id]
    dictioner.remove(S[0])
    return jsonify({'Imac' : dictioner})



# run APi 

if __name__ == '__main__':
    app.run(debug = True , port = 8000)



###############@ test commite 