from flask import render_template, redirect, url_for, flash, session, request
from . import admin
from ..models import *
from .forms import *
from .. import db



@admin.route('/1', methods=["GET", "POST"])
def direction():
    form = DirectionForms()

    if form.validate_on_submit():
        data = Direction(
            uz_name = form.uz_name.data,
            ru_name = form.ru_name.data,
            en_name = form.en_name.data,
            order = form.order.data
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('admin.direction'))

    return render_template('direction.html', form=form)



@admin.route('/2', methods=["GET", "POST"])
def services():
    form = ServicesForms()

    if form.validate_on_submit():
        data = Services(
            uz_title = form.uz_title.data,
            ru_title = form.ru_title.data,
            en_title = form.en_title.data,

            uz_text = form.uz_text.data,
            ru_text = form.ru_text.data,
            en_text = form.en_text.data
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('admin.services'))

    return render_template('services.html', form=form)






@admin.route('/3', methods=["GET", "POST"])
def question_answers():
    form = QuestionAnswersForms()

    if form.validate_on_submit():
        data = QuestionAnswers(
            uz_ques = form.uz_ques.data,
            ru_ques = form.ru_ques.data,
            en_ques = form.en_ques.data,

            uz_answer = form.uz_answer.data,
            ru_answer = form.ru_answer.data,
            en_answer = form.en_answer.data,

            direction = form.id.data,
            slider_class = form.slider_class.data
        )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('admin.question_answers'))

    return render_template('answers.html', form=form)


import datetime
import os

@admin.route('/4', methods=["GET", "POST"])
def news():
    form = NewsForms()

    fpath = os.path.join('app', 'main', 'main-static', 'news_images')
    if form.validate_on_submit():

        poster = request.files.get('image')
        if poster.filename != '':
            poster.save(os.path.join(fpath, poster.filename))
            data = News(
                uz_title = form.uz_title.data,
                ru_title = form.ru_title.data,
                en_title = form.en_title.data,

                uz_text = form.uz_text.data,
                ru_text = form.ru_text.data,
                en_text = form.en_text.data,

                image = poster.filename,
                created_on = datetime.datetime.utcnow(),
                updated_on = datetime.datetime.utcnow()
            )
            db.session.add(data)
            db.session.commit()
        return redirect(url_for('admin.news'))

    return render_template('add_news.html', form=form)






@admin.route('/5', methods=["GET", "POST"])
def events():
    form = EventsForms()

    fpath = os.path.join('app', 'main', 'main-static', 'events_images')
    if form.validate_on_submit():
        poster = request.files.get('image')
        if poster.filename != '':
            poster.save(os.path.join(fpath, poster.filename))
            data = Events(
                uz_name = form.uz_name.data,
                ru_name = form.ru_name.data,
                en_name = form.en_name.data,

                uz_position = form.uz_position.data, #lavozim
                ru_position = form.ru_position.data,
                en_position = form.en_position.data,

                image = poster.filename,
                facebook = form.facebook.data,
                instagram = form.instagram.data,
                telegram = form.telegram.data,
                phone = form.phone.data
                )
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('admin.events'))

    return render_template('events.html', form=form)

    


@admin.route('/6', methods=["GET", "POST"])
def links():
    form = LinksForms()

    fpath = os.path.join('app', 'main', 'main-static', 'links_images')
    if form.validate_on_submit():
        poster = request.files.get('image')
        if poster.filename != '':
            poster.save(os.path.join(fpath, poster.filename))
            data = Links(
                uz_title = form.uz_title.data,
                ru_title = form.ru_title.data,
                en_title = form.en_title.data,

                uz_text = form.uz_text.data,
                ru_text = form.ru_text.data,
                en_text = form.en_text.data,

                link = form.link.data,
                image = poster.filename
                )
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('admin.links'))

    return render_template('links.html', form=form)




@admin.route('/7', methods=["GET", "POST"])
def smc():
    form = SmcForms()

    if form.validate_on_submit():
        data = Smc(
            email = form.email.data,
            tel = form.tel.data,
            address = form.address.data,
            )
        db.session.add(data)
        db.session.commit()
        return redirect(url_for('admin.smc'))

    return render_template('smc.html', form=form)


