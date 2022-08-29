from app import db

class Direction(db.Model): #Yo'nalishlar
    __tablename__='direction'
    id = db.Column(db.Integer, primary_key=True)

    uz_name = db.Column(db.String(100))
    ru_name = db.Column(db.String(100))
    en_name = db.Column(db.String(100))

    questions = db.relationship('QuestionAnswers', backref='catalog', lazy='dynamic')

    def __repr__(self):
        return f"<Direction {self.id} >"

class Services(db.Model): #Bizning xizmatlarimiz
    __tablename__='services'
    id = db.Column(db.Integer, primary_key=True)
    
    uz_title = db.Column(db.String(100))
    ru_title = db.Column(db.String(100))
    en_title = db.Column(db.String(100))

    uz_text = db.Column(db.String(150))
    ru_text = db.Column(db.String(150))
    en_text = db.Column(db.String(150))

    def __repr__(self):
        return f"<Services {self.id} >"


class QuestionAnswers(db.Model):
    __tablename__='question_answers'
    id = db.Column(db.Integer, primary_key=True)

    uz_ques = db.Column(db.String(100))
    ru_ques = db.Column(db.String(100))
    en_ques = db.Column(db.String(100))

    uz_answer = db.Column(db.Text(100))
    ru_answer = db.Column(db.Text(100))
    en_answer = db.Column(db.Text(100))

    slider_class = db.Column(db.Boolean(), default=False)

    direction = db.Column(db.Integer(), db.ForeignKey('direction.id'))

    def __repr__(self):
        return f"<QuestionAnswers {self.id} >"


class News(db.Model): #Yangiliklar
    __tablename__='news'
    id = db.Column(db.Integer, primary_key=True)

    uz_title = db.Column(db.String(100))
    ru_title = db.Column(db.String(100))
    en_title = db.Column(db.String(100))

    uz_text = db.Column(db.String(100))
    ru_text = db.Column(db.String(100))
    en_text = db.Column(db.String(100))
    views = db.Column(db.Integer(), default=0)

    image = db.Column(db.String(50))
    created_on = db.Column(db.DateTime, nullable=False)
    updated_on = db.Column(db.DateTime, nullable=False)


class Events(db.Model): #Hodimlar
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True)

    uz_name = db.Column(db.String(100))
    ru_name = db.Column(db.String(100))
    en_name = db.Column(db.String(100))

    uz_position = db.Column(db.String(100)) #lavozim
    ru_position = db.Column(db.String(100))
    en_position = db.Column(db.String(100))

    image = db.Column(db.String(100))
    facebook = db.Column(db.String(50))
    instagram = db.Column(db.String(50))
    telegram = db.Column(db.String(50))
    phone = db.Column(db.String(50))


class Links(db.Model):  # Полезные ссылки
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)

    uz_title = db.Column(db.String(100))
    ru_title = db.Column(db.String(100))
    en_title = db.Column(db.String(100))

    uz_text = db.Column(db.String(100))
    ru_text = db.Column(db.String(100))
    en_text = db.Column(db.String(100))

    link = db.Column(db.String(100))
    image = db.Column(db.String(100))


class Smc(db.Model):  # Additional information
    __tablename__ = 'smc'
    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(100))
    tel = db.Column(db.String(100))
    address = db.Column(db.String(100))