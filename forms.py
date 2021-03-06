from wtforms import Form, StringField, IntegerField, validators, \
    FieldList, ValidationError, RadioField, TextAreaField, SelectField


def validate_people(form, field):
    """Validator to ensure that all names are unique"""
    for person in form.people:
        if person.id is not field.id and person.data == field.data:
            raise ValidationError('Names must be unique')


class ProjectCreateForm(Form):
    project_name = StringField('Give your project a name', [validators.Length(min=1, max=200),
                                                            validators.DataRequired()])
    # NOTE: Mix and max people also specified in custom.js
    person_count = IntegerField('Number of people on this project (not more than 20)',
                                [validators.NumberRange(min=1, max=20)], default=2)


class PeopleForm(Form):
    people = FieldList(StringField('Name', [validators.InputRequired(), validators.Length(min=1, max=100),
                                            validate_people]))


class WhoAreYouForm(Form):
    people = RadioField('Label', coerce=int, choices=[])


class TaskForm(Form):
    title = StringField('Name for the task', [validators.Length(min=1, max=200), validators.DataRequired()])
    description = TextAreaField('Optional description', [validators.Length(min=0, max=4000)])
    priority = RadioField('priority', choices=[('0', 'Low'), ('1', 'Normal'), ('2', 'Urgent')], default='1')
    assigned_to = SelectField('Who is this task assigned to?', coerce=int, choices=[])


class CommentForm(Form):
    comment = TextAreaField('Add a comment', [validators.Length(min=1, max=4000)])
