from flask import render_template, redirect, url_for, flash, session, request
from . import main
from ..models import *
from ..getlan import *


# ==============================================================================
# ==============================================================================
@main.route('/')  # Главня страница
def main_page():
    if 'lang' not in session:
        session['lang'] = 'uz'

    # # ---------------------------------
    directions = Direction.query.all()
    services = Services.query.all()
    questions_1 = QuestionAnswers.query.filter_by(direction=1).limit(3)
    questions_2 = QuestionAnswers.query.filter_by(direction=2).limit(3)
    questions_3 = QuestionAnswers.query.filter_by(direction=3).limit(3)
    questions_4 = QuestionAnswers.query.filter_by(direction=4).limit(3)
    news = News.query.order_by(News.id.desc()).all()
    events = Events.query.all()
    links = Links.query.all()
    smc = Smc.query.all()
    # # ---------------------------------

    # # ---------------------------------
    direction_data = direction_lang(directions)
    services_data = services_lang(services)
    questions_data = questions_lang(questions_1, questions_2,
                                    questions_3, questions_4)
    news_data = news_lang(news)
    events_data = events_lang(events)
    links_data = links_lang(links)
    # # ---------------------------------

    return render_template(
        'main.html',
        direction_data=direction_data,
        services_data=services_data,
        questions_data=questions_data,
        news_data=news_data,
        events_data=events_data,
        links_data=links_data,
        smc=smc
        )




@main.route('/News/<int:id>') # Страница новости
def news_page(id):
    if 'lang' not in session:
        session['lang'] = 'uz'
    all_news = News.query.order_by(News.id.desc()).all()
    news = News.query.filter_by(id=id).first()
    
    news.views = news.views + 1
    db.session.add(news)
    db.session.commit()

    all_news_data = news_lang(all_news)
    news_data = news_item_lang(news)

    return render_template(
        'news.html',
        news_data=news_data,
        all_news_data=all_news_data
        )

import telegram_send


@main.route('/FeedBack', methods=["GET", "POST"]) # Отправляет сообщения в тг бот
def feedback():
    
    if request.method == 'POST':
        radio = request.form.get('satellite_connection')
        organization = request.form.get('organization')
        position = request.form.get('position')
        phone = request.form.get('phone')
        comment = request.form.get('comment')
        if radio != '' and organization != '' and position != '' and phone != '' and comment != '':
            telegram_send.send(messages=[
                f'''Напровление: {radio}

                Организация:
                {organization}

                Должность:
                {position}

                Тел: {phone}
                =============================
                
                Вопрос:
                {comment}'''
                ])
            if session['lang'] == 'uz':flash('Xabar yuborildi!')
            elif session['lang'] == 'ru':flash('Сообщение отправлено!')
            else:flash('The message has been sent!')
        else:
            if session['lang'] == 'uz':flash('Yuborishda xato!')
            elif session['lang'] == 'ru':flash('Ошибка при отправке!')
            else:flash('Error sending!')
        return redirect(url_for('main.main_page'))




@main.route('/lang/<lang_code>') # Меняет язык
def lang(lang_code):
    session['lang'] = lang_code
    return redirect(url_for('main.main_page'))

