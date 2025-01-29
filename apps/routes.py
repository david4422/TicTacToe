import secrets
from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request # type: ignore
from flask_bootstrap import Bootstrap5 # type: ignore
from flask_ckeditor import CKEditor # type: ignore
from flask_gravatar import Gravatar # type: ignore
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column # type: ignore
from typing import List
from sqlalchemy import Integer, String, Text, ForeignKey # type: ignore
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore
# Import your forms from the forms.py
from .forms import  LoginForm
from .models import User
from . import db
import os
from flask_admin import Admin # type: ignore
from flask_admin.contrib.sqla import ModelView # type: ignore
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user # type: ignore
from flask_migrate import Migrate # type: ignore
from .game import playing # type: ignore

def init_apps(app):
    ckeditor = CKEditor(app)
    Bootstrap5(app)

    ########################################################## login ##########################################################
    #מגדיר לוגין מנג'ר
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'  # דף התחברות

        # יצירת ממשק ניהול
    admin = Admin(app, name='Portfolio Admin', template_mode='bootstrap3')

    # הוספת המודל לממשק הניהול
    class AdminModelView(ModelView):
        def is_accessible(self):
            return current_user.is_authenticated and current_user.role == "admin"  # גישה רק למתחברים
        def inaccessible_callback(self, name, **kwargs):
            return redirect(url_for('login'))  # מפנה ידנית לדף התחברות
        
    admin.add_view(AdminModelView(User, db.session))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # מחפש את המשתמש לפי ה-ID

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if request.method == 'POST':
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):  # בדוק את הסיסמה בצורה מאובטחת
                login_user(user)
                return redirect('/')
        return render_template('login.html', form=form)
    

    @app.route('/admin/users', methods=['GET', 'POST'])
    @login_required  # רק מחוברים יכולים להיכנס
    def manage_users():
        if current_user.role != "admin":  # רק אדמין יכול להוסיף משתמשים
            abort(403)  # מחזיר שגיאת Forbidden
        
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            role = request.form.get('role', 'user')  # ברירת מחדל - משתמש רגיל

            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

            new_user = User(username=username, password=hashed_password, role=role)
            db.session.add(new_user)
            db.session.commit()
            flash("User added successfully!", "success")

        return render_template('manage_users.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect('/')
    

    ########################################################## game ##########################################################



    @app.route('/')
    def home():
        # playing()
        return render_template('home.html')
    

    @app.route('/game')
    def game():
        # playing()
        return render_template('game.html')
    
    with app.app_context():
        
        db.create_all()