
from flask_admin import Admin
import os
from flask import Blueprint, current_app
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
import os
from flask_sqlalchemy import SQLAlchemy
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import Admin
from sqlalchemy import text
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask_admin.base import BaseView, expose
from flask_admin.menu import MenuLink
from ..models.models import Enderecos, Estados, Municipios


Admin_ = Blueprint('adm', __name__)

#current_app.config["UPLOAD_FOLDER"] = 
#excel.init_excel(current_app)

db = SQLAlchemy()
def admin_db(app):
    db.init_app(app)
    app.db = db

class DefaultModelView(ModelView):
    pass
   
class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def Home(self):
   
        return self.render('admin/index.html')

admin = Admin(current_app, name='Dashboard',
              template_mode='bootstrap3', index_view=MyAdminIndexView())

current_app.config['FLASK_ADMIN_FLUID_LAYOUT'] = True


class CommentView(ModelView):
    create_modal = True



class NotificationsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/notification.html')


class EnderecosView(ModelView):
    can_set_page_size = True
    page_size = 15
    column_display_pk = True
    create_modal = True

class EstadosView(ModelView):
    can_set_page_size = True
    page_size = 15
    column_display_pk = True
    create_modal = True

class MunicipiosView(ModelView):
    can_set_page_size = True
    page_size = 15
    column_display_pk = True
    create_modal = True



admin.add_view(NotificationsView(name='Notifications', endpoint='notify'))

admin.add_view(EnderecosView(
    Enderecos, db.session))

admin.add_view(EstadosView(
    Estados, db.session))

admin.add_view(MunicipiosView(Municipios, db.session))