import pdfrw
from datetime import date

TEMPLATE_PATH = 'template.pdf'
OUTPUT_PATH = 'starter_form.pdf'

ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def fill_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    for page in template_pdf.pages:
        annotations = page[ANNOT_KEY]
        for annotation in annotations:
            if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
                if annotation[ANNOT_FIELD_KEY]:
                    key = annotation[ANNOT_FIELD_KEY][1:-1]
                    if key in data_dict.keys():
                        if type(data_dict[key]) == bool:
                            if data_dict[key] == True:
                                annotation.update(pdfrw.PdfDict(
                                    AS=pdfrw.PdfName('Yes')))
                        else:
                            annotation.update(
                                pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                            )
                            annotation.update(pdfrw.PdfDict(AP=''))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)


def fill_starter_checklist(data):
    today = date.today()
    data_dict = {
        'last_name': data['last_name'],
        'first_name_l1': data['first_names'],
        'first_name_l2': '',
        '3_male': True if data['sex'] == 'm' else False,
        '3_female': True if data['sex'] == 'f' else False,
        '4_d1': "{:02}".format(data['date_of_birth'].day)[0],
        '4_d2': "{:02}".format(data['date_of_birth'].day)[1],
        '4_m1': "{:02}".format(data['date_of_birth'].month)[0],
        '4_m2': "{:02}".format(data['date_of_birth'].month)[1],
        '4_y1': "{:04}".format(data['date_of_birth'].year)[0],
        '4_y2': "{:04}".format(data['date_of_birth'].year)[1],
        '4_y3': "{:04}".format(data['date_of_birth'].year)[2],
        '4_y4': "{:04}".format(data['date_of_birth'].year)[3],
        'home_address_1': [str.strip() for str in data['address'].splitlines()][0],
        'home_address_2': [str.strip() for str in data['address'].splitlines()][1],
        'home_address_3': [str.strip() for str in data['address'].splitlines()][2],
        'home_address_4': data['postcode'],
        'home_address_5': data['country'],
        '6_1': data['ni_number'][0],
        '6_2': data['ni_number'][1],
        '6_3': data['ni_number'][2],
        '6_4': data['ni_number'][3],
        '6_5': data['ni_number'][4],
        '6_6': data['ni_number'][5],
        '6_7': data['ni_number'][6],
        '6_8': data['ni_number'][7],
        '6_9': data['ni_number'][8],
        '7_d1': "{:02}".format(data['employment_start'].day)[0],
        '7_d2': "{:02}".format(data['employment_start'].day)[1],
        '7_m1': "{:02}".format(data['employment_start'].month)[0],
        '7_m2': "{:02}".format(data['employment_start'].month)[1],
        '7_y1': "{:04}".format(data['employment_start'].year)[0],
        '7_y2': "{:04}".format(data['employment_start'].year)[1],
        '7_y3': "{:04}".format(data['employment_start'].year)[2],
        '7_y4': "{:04}".format(data['employment_start'].year)[3],
        '8_a': True if data['question_8'] == 'a' else False,
        '8_b': True if data['question_8'] == 'b' else False,
        '8_c': True if data['question_8'] == 'c' else False,
        '9_y': True if data['question_9'] == True else False,
        '9_n': True if data['question_9'] == False else False,
        '10_y': True if data['question_10'] == True else False,
        '10_n': True if data['question_10'] == False else False,
        '11_y': True if data['question_11'] == True else False,
        '11_n': True if data['question_11'] == False else False,
        '12_plan_1': True if data['question_12'] == '1' else False,
        '12_plan_2': True if data['question_12'] == '2' else False,
        '12_both': True if data['question_12'] == 'b' else False,
        '13_y': True if data['question_13'] == True else False,
        '13_n': True if data['question_13'] == False else False,
        '14_y': True if data['question_14'] == True else False,
        '14_n': True if data['question_14'] == False else False,
        '15_y': True if data['question_15'] == True else False,
        '15_n': True if data['question_15'] == False else False,
        'full_name': data['first_names'] + ' ' + data['last_name'],
        'd_d1': "{:02}".format(today.day)[0],
        'd_d2': "{:02}".format(today.day)[1],
        'd_m1': "{:02}".format(today.month)[0],
        'd_m2': "{:02}".format(today.month)[1],
        'd_y1': "{:04}".format(today.year)[0],
        'd_y2': "{:04}".format(today.year)[1],
        'd_y3': "{:04}".format(today.year)[2],
        'd_y4': "{:04}".format(today.year)[3],
    }

    return fill_pdf(TEMPLATE_PATH, OUTPUT_PATH, data_dict)


starter_checklist = {
    'first_names': 'Frederic John',
    'last_name': 'Smith',
    'sex': 'm',  # Either 'm' or 'f'
    'date_of_birth': date(1980, 12, 30),
    'address': "123 Fake Street \n Westminster \n London",
    'postcode': 'AB1 2CD',
    'country': 'United Kingdom',
    'ni_number': 'AB123456F',
    'employment_start': date.today(),
    'question_8': 'a',  # 'a', 'b' or 'c'
    'question_9': True,
    'question_10': False,
    'question_11': '',
    'question_12': '',  # '1', '2', 'b'
    'question_13': False,
    'question_14': '',
    'question_15': '',
}

if __name__ == '__main__':
    fill_starter_checklist(starter_checklist)
