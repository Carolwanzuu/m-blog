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
    title = TextAreaField('Enter Title',validators = [Required()])
    blog_content = TextAreaField('Enter blog conteny',validators = [Required()])
    author = TextAreaField('Name of author',validators = [Required()])
   
    submit = SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment=TextAreaField('Type comment:', validators=[DataRequired()])
    submit=SubmitField('Post Comment')
