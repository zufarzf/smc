from flask import session
# ==============================================================================
# ==============================================================================
def direction_lang(directions):
    data_of_contente = []

    if session['lang'] == 'uz':
        for i in directions:
            data_of_contente.append(i.uz_name)

    elif session['lang'] == 'ru':
        for i in directions:
            data_of_contente.append(i.ru_name)

    else:
        for i in directions:
            data_of_contente.append(i.en_name)
    
    return data_of_contente
# ==============================================================================
# ==============================================================================
def services_lang(services):
    data_of_contente = []

    if session['lang'] == 'uz':
        for i in services:
            dict_data_of_contente = {'title':i.uz_title, 'text':i.uz_text}
            data_of_contente.append(dict_data_of_contente)

    elif session['lang'] == 'ru':
        for i in services:
            dict_data_of_contente = {'title':i.ru_title, 'text':i.ru_text}
            data_of_contente.append(dict_data_of_contente)

    else:
        for i in services:
            dict_data_of_contente = {'title':i.en_title, 'text':i.en_text}
            data_of_contente.append(dict_data_of_contente)
    
    return data_of_contente
# ==============================================================================
# ==============================================================================
def questions_lang(questions_1, questions_2, questions_3, questions_4):
    # -------------------------------
    questions_1_data_of_contente = []
    questions_2_data_of_contente = []
    questions_3_data_of_contente = []
    questions_4_data_of_contente = []
    # -------------------------------
    data_of_contente = [
        questions_1_data_of_contente,
        questions_2_data_of_contente,
        questions_3_data_of_contente,
        questions_4_data_of_contente
        ]
    # -------------------------------
    if session['lang'] == 'uz':
        for i in questions_1:
            dict_data_of_contente = {
                'ques' : i.uz_ques, 'answer' : i.uz_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_1_data_of_contente.append(dict_data_of_contente)
        # -------------------------------

        for i in questions_2:
            dict_data_of_contente = {
                'ques' : i.uz_ques, 'answer' : i.uz_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_2_data_of_contente.append(dict_data_of_contente)
        # -------------------------------
        
        for i in questions_3:
            dict_data_of_contente = {
                'ques' : i.uz_ques, 'answer' : i.uz_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_3_data_of_contente.append(dict_data_of_contente)
        # -------------------------------
        
        for i in questions_4:
            dict_data_of_contente = {
                'ques' : i.uz_ques, 'answer' : i.uz_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_4_data_of_contente.append(dict_data_of_contente)
        # -------------------------------
    # ====================================================================
    elif session['lang'] == 'ru':
        for i in questions_1:
            dict_data_of_contente = {
                'ques' : i.ru_ques, 'answer' : i.ru_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_1_data_of_contente.append(dict_data_of_contente)
        # -------------------------------

        for i in questions_2:
            dict_data_of_contente = {
                'ques' : i.ru_ques, 'answer' : i.ru_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_2_data_of_contente.append(dict_data_of_contente)
        # -------------------------------
        
        for i in questions_3:
            dict_data_of_contente = {
                'ques' : i.ru_ques, 'answer' : i.ru_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_3_data_of_contente.append(dict_data_of_contente)
        # -------------------------------
        
        for i in questions_4:
            dict_data_of_contente = {
                'ques' : i.ru_ques, 'answer' : i.ru_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_4_data_of_contente.append(dict_data_of_contente)
        # -------------------------------

    # ====================================================================
    else:
        for i in questions_1:
            dict_data_of_contente = {
                'ques' : i.en_ques, 'answer' : i.en_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_1_data_of_contente.append(dict_data_of_contente)
        # -------------------------------

        for i in questions_2:
            dict_data_of_contente = {
                'ques' : i.en_ques, 'answer' : i.en_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_2_data_of_contente.append(dict_data_of_contente)
        # -------------------------------
        
        for i in questions_3:
            dict_data_of_contente = {
                'ques' : i.en_ques, 'answer' : i.en_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_3_data_of_contente.append(dict_data_of_contente)
        # -------------------------------
        
        for i in questions_4:
            dict_data_of_contente = {
                'ques' : i.en_ques, 'answer' : i.en_answer,
                'slider_class' : i.slider_class, 'direction' : i.direction,
            }
            questions_4_data_of_contente.append(dict_data_of_contente)
        # -------------------------------
    return data_of_contente
# ==============================================================================
# ==============================================================================
def news_lang(news):
    data_of_contente = []

    if session['lang'] == 'uz':
        for i in news:
            dict_data_of_contente = {
                'id':i.id, 'title':i.uz_title,
                'text':i.uz_text, 'image':i.image,
                'views':i.views
            }
            data_of_contente.append(dict_data_of_contente)

    elif session['lang'] == 'ru':
        for i in news:
            dict_data_of_contente = {
                'id':i.id, 'title':i.ru_title,
                'text':i.ru_text, 'image':i.image,
                'views':i.views
            }
            data_of_contente.append(dict_data_of_contente)

    else:
        for i in news:
            dict_data_of_contente = {
                'id':i.id, 'title':i.en_title,
                'text':i.en_text, 'image':i.image,
                'views':i.views
            }
            data_of_contente.append(dict_data_of_contente)
    
    return data_of_contente

def news_item_lang(news):
    if session['lang'] == 'uz':
        dict_data_of_contente = {
            'id':news.id, 'title':news.uz_title,
            'text':news.uz_text, 'image':news.image,
            'views':news.views
        }

    elif session['lang'] == 'ru':
        dict_data_of_contente = {
            'id':news.id, 'title':news.ru_title,
            'text':news.ru_text, 'image':news.image,
            'views': news.views
        }

    else:
        dict_data_of_contente = {
            'id':news.id, 'title':news.en_title,
            'text':news.en_text, 'image':news.image,
            'views':news.views
        }
    return dict_data_of_contente

# ==============================================================================
# ==============================================================================

def events_lang(events):
    data_of_contente = []

    if session['lang'] == 'uz':
        for i in events:
            dict_data_of_contente = {
                'name':i.uz_name, 'position':i.uz_position,
                'image':i.image, 'facebook':i.facebook,
                'instagram':i.instagram, 'telegram':i.telegram,
                'phone':i.phone 
            }
            data_of_contente.append(dict_data_of_contente)

    elif session['lang'] == 'ru':
        for i in events:
            dict_data_of_contente = {
                'name':i.ru_name, 'position':i.ru_position,
                'image':i.image, 'facebook':i.facebook,
                'instagram':i.instagram, 'telegram':i.telegram,
                'phone':i.phone 
            }
            data_of_contente.append(dict_data_of_contente)

    else:
        for i in events:
            dict_data_of_contente = {
                'name':i.en_name, 'position':i.en_position,
                'image':i.image, 'facebook':i.facebook,
                'instagram':i.instagram, 'telegram':i.telegram,
                'phone':i.phone 
            }
            data_of_contente.append(dict_data_of_contente)
    
    return data_of_contente

# ==============================================================================
# ==============================================================================

def links_lang(links):
    data_of_contente = []

    if session['lang'] == 'uz':
        for i in links:
            dict_data_of_contente = {
                'title':i.uz_title, 'text':i.uz_text,
                'link':i.link, 'image':i.image
            }
            data_of_contente.append(dict_data_of_contente)

    elif session['lang'] == 'ru':
        for i in links:
            dict_data_of_contente = {
                'title':i.ru_title, 'text':i.ru_text,
                'link':i.link, 'image':i.image
            }
            data_of_contente.append(dict_data_of_contente)

    else:
        for i in links:
            dict_data_of_contente = {
                'title':i.en_title, 'text':i.en_text,
                'link':i.link, 'image':i.image
            }
            data_of_contente.append(dict_data_of_contente)
    
    return data_of_contente
