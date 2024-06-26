# Importación de librerias:
    # marco de flask es el frameworrk backendy 
    #SqlAlchemy Es el ORM para modelar los datos de la base de datos como objetos
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



# Instanciamos la aplicacion
app = Flask(__name__)  

# Configuramos la base de datos mysql 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/taller'  

# creamos el objeto db utilizando la instancia de la aplicacion 
db = SQLAlchemy(app)


### MODELOS DE DATOS ##########################################################################

# Se crea el modelo ciudad:
class Ciudad(db.Model):
    __tablename__ = 'ciudades'
    IdCiudad = db.Column(db.Integer, primary_key=True)
    Ciudad = db.Column(db.String(45), nullable = False)

# Se crea el modelo de datos para la tabla TipoCliente
class TipoCliente(db.Model):
    __tablename__='Tipo_Cliente'
    idTipoCliente = db.Column(db.Integer, primary_key=True)
    TipoCliente = db.Column(db.String(45), nullable = False)
    IdEstado = db.Column(db.Integer, nullable=False)


# Creamos el modelo de datos para la tabla Cliente usando el ORM SQLAlchemy
class Cliente(db.Model):
    __tablename__ = 'clientes'    
    idCliente = db.Column(db.Integer, primary_key=True)
    IdTipoCliente = db.Column(db.Integer, nullable = False)
    CC_NIT = db.Column(db.String(50), nullable = False)
    Nombres = db.Column(db.String(100), nullable = False)
    IdCiudad = db.Column(db.Integer, nullable = False)
    Direccion = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    telefono = db.Column(db.String(50), nullable = False)
    
# Crear el modelo vehiculo
class Vehiculo(db.Model):
    __tablename__ = 'Vehiculos'
    IdVehiculo = db.Column(db.Integer, primary_key = True)
    Placa = db.Column(db.String(10), nullable = False)
    IdMarca = db.Column(db.Integer, nullable = False)
    Linea = db.Column(db.String(45), nullable = False)
    Modelo = db.Column(db.Integer, nullable = False)
    Color = db.Column(db.String(45), nullable = False)
    IdTipoCarroceria = db.Column(db.Integer, nullable = False)

# Crear el modelo Tipo Carroceria
class Tipo_Carroceria(db.Model):
    __tablename__ ='tipos_carroceria'
    IdTipoCarroceria = db.Column(db.Integer, primary_key = True)
    TipoCarroceria = db.Column(db.String(45), nullable = False)

#Crear el modelo Marca
class Marca(db.Model):
    __tablename__= 'Marcas'
    IdMarca = db.Column(db.Integer, primary_key = True)
    Marca = db.Column(db.String, nullable = False)


#Rutas
@app.route('/clientes')
def verClientes():
    clientes = Cliente.query.all() # Consulta todos los clientes en la base de datos
    return render_template('clientes.html', clientes=clientes)

@app.route('/')
def home():
   return render_template('index.html')
#---------------------------------------------------------------------------
#Ejecucion
    
if __name__ == "__main__":
    app.run(debug=True)

#-----------------------------------------------------------------------------   
#--- Rutas:


