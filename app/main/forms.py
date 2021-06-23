from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required, Email, EqualTo,DataRequired


class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something interesting about you.', validators = [Required()])
    submit = SubmitField('Submit')

class BlogForm(FlaskForm):
    title = TextAreaField('Enter Business Name',validators = [Required()])
    blog_content = TextAreaField('Enter Number',validators = [Required()])
    author = TextAreaField('Tell us about your business',validators = [Required()])
    posted = StringField('Enter the day of posting')
    submit = SubmitField('Submit')
