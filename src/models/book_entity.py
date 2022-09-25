import configDB as configDb


from flask_marshmallow import Marshmallow

class Books(configDb.db.Model):
    #uuid= uuid_pkg.UUID = Field(default_factory=uuid_pkg.uuid4,primary_key=True,index=True,nullable=False)
    
    title = configDb.db.Column(configDb.db.String(100), unique=True)
    author = configDb.db.Column(configDb.db.String(200), unique=False)
    read= configDb.db.Column (configDb.db.Boolean, unique=False, default=False)
    
    
    def __init__(self,title, author, read):
        
        self.title=title
        self.author=author
        self.read=read
    
create_tables=configDb.db.create_all()

class BookSchema(configDb.ma.Schema):
    class Meta:
        fields = ('id', 'title', 'author', 'read')

book_schema=BookSchema();
books_schema=BookSchema(many=True);

#def create_app(config=None, app_name=None, blueprints=None):
    