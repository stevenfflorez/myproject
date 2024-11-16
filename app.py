from flask import Flask
from config import  db, DATABASE_URI
from router.user_routes import user_bp


app = Flask(__name__)

#configurar la URi de la db
app.config['SQLALCHEMY_DATABASE_URI'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#Inicializar Db
db.init_app(app)

#Registrar los Blueprints de las rutas
app.register_blueprint(user_bp)

#Crear las tablas si no existen
with app.app_context():
    db.create_all()

    if __name__ =='__main__':
        app.run(debug=True)