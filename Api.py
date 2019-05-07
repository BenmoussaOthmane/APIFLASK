from flask import Flask,jsonify,request
import json
import os



#  Name APP

app = Flask(__name__)



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
def index():
    return '<h1> Bienvenu  </h1>'



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