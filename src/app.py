

#from models.configDB import app
from models.model_setup import create_tables
from controllers import Books_Controller
from controllers import error_handler
from controllers.error_handler import create_flask_app_with_error_handlers




app = create_flask_app_with_error_handlers()
app.register_blueprint(Books_Controller.BOOKS_CONTROLLER)

if __name__=="__main__":
    create_tables()
    app.run(debug=True,port=4000)
    