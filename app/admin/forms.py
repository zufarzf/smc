from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, FileField, IntegerField, BooleanField


class DirectionForms(FlaskForm):
    uz_name = TextAreaField()
    ru_name = TextAreaField()
    en_name = TextAreaField()
    order = StringField()

    submit = SubmitField('Save')


class ServicesForms(FlaskForm):

    uz_title = StringField()
    ru_title = StringField()
    en_title = StringField()

    uz_text = TextAreaField()
    ru_text = TextAreaField()
    en_text = TextAreaField()

    submit = SubmitField('Save')



class FAQCatForms(FlaskForm):
    uz_title = TextAreaField()
    ru_title = TextAreaField()
    en_title = TextAreaField()

    submit = SubmitField('Save')



class QuestionAnswersForms(FlaskForm):

    uz_ques = TextAreaField()
    ru_ques = TextAreaField()
    en_ques = TextAreaField()

    uz_answer = TextAreaField()
    ru_answer = TextAreaField()
    en_answer = TextAreaField()
    slider_class = BooleanField()
    id = IntegerField()

    submit = SubmitField('Save')



class NewsForms(FlaskForm):
    uz_title = StringField()
    ru_title = StringField()
    en_title = StringField()

    uz_text = TextAreaField()
    ru_text = TextAreaField()
    en_text = TextAreaField()

    image = FileField()

    submit = SubmitField('Save')



class EventsForms(FlaskForm):
    uz_name = StringField()
    ru_name = StringField()
    en_name = StringField()

    uz_position = StringField() #lavozim
    ru_position = StringField()
    en_position = StringField()

    facebook = StringField()
    instagram = StringField()
    telegram = StringField()
    phone = StringField()
    image = FileField()

    submit = SubmitField('Save')



class LinksForms(FlaskForm):

    uz_title = StringField()
    ru_title = StringField()
    en_title = StringField()

    uz_text = TextAreaField()
    ru_text = TextAreaField()
    en_text = TextAreaField()

    link = StringField()
    image = FileField()

    submit = SubmitField('Save')


class MenuForms(FlaskForm):
    uz_name = StringField()
    ru_name = StringField()
    en_name = StringField()

    submit = SubmitField('Save')



class SmcForms(FlaskForm):
    email = StringField()
    tel = StringField()
    address = StringField()

    submit = SubmitField('Save')
