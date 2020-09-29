from flask import render_template,redirect,url_for,abort
from . import main
from ..models import User,Pitch
from .forms import PitchForm,UpdateProfile
from ..import db,photos
from flask_login import login_required, current_user
import markdown2


@main.route('/')
def index():
    title ='Home - Welcome to the best pitches website online'
    return render_template('index.html',title = title)

@main.route('/pitch/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    
    if form.validate_on_submit():
        pitch = form.pitch.data
        

        # Updated review instance
        new_pitch = Pitch(pitch=pitch,user=current_user)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.new_pitch' ))

    
    return render_template('pitches/new_pitch.html',pitch_form=form)
@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template("profile/update.html",form = form)



@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
