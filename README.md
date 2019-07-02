# Filling the HMRC "Starter Checklist" PDF form using Python

This Snippet was to enable the [HMRC Starter Checklist](https://www.gov.uk/government/publications/paye-starter-checklist) [PDF](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/783186/Starter_checklist_for_2019_to_2020.pdf) to be pragmatically filled by a python app. It was "written" for a project (that didn't end up being presented) at [NHS Hackday #22 in London](https://nhshackday.com/events/2019/06/london).

For a little more background see my post "[Snippet: Filling a PDF form using Python](https://blu3id.uk/posts/snippet-python-pdf-form-filling)"

## Install

Ensure `pipenv` is installed see https://docs.pipenv.org/ for how to setup on your platform of choice.

To get started and set-up virtualenv and install dependencies initially:
```bash
git clone https://github.com/blu3id/python-pdf-form-filling/
cd python-pdf-form-filling
pipenv install --dev
```

## Run

Edit `starter_checklist.py` so that the values of the `starter_checklist` dict corespond to the answers to the questions on the HMRC form.

```python
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
```

Then run `python starter_checklist.py` to produce `starter_form.pdf`