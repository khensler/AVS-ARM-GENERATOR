from ast import Str
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, HiddenField, PasswordField,BooleanField, TextAreaField
from wtforms import validators
from wtforms.validators import DataRequired, Email


class form_deploy_info(FlaskForm):
    SubOfVnetGW = StringField('SubOfVnetGW', validators=[DataRequired()])
    PrivateCloudName = StringField("PrivateCloudNAme", validators=[DataRequired()])
    PrivateCloudAddressSpace = StringField("PrivateCloudAddressSpace",validators=[DataRequired()])
    vNetGWRG = StringField("vNetGWRG",validators=[DataRequired()])
    vNetGWvNet = StringField("vNetGWvNet",validators=[DataRequired()])
    GatewayName = StringField("GatewayName",validators=[DataRequired()])
    OnPremExpressRouteAuthorizationKey = StringField("OnPremExpressRouteAuthorizationKey",validators=[DataRequired()])
    OnPremExpressRouteId = StringField("OnPremExpressRouteId",validators=[DataRequired()])
    InternetStatus = HiddenField("InternetStatus", default="Enabled", validators=[DataRequired()])
    submit = SubmitField('Generate ARM Template')