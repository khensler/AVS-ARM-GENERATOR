#from app import app
from tokenize import Floatnumber
from flask import current_app as app
from flask import render_template, redirect, flash, request, session
from flask_session import Session
from app.forms import *
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import json
import uuid
import os
import urllib.parse

@app.route('/',methods = ['GET','POST'])
@app.route('/index',methods = ['GET','POST'])
def index():
    form = form_deploy_info()
    if form.validate_on_submit():
        f = open('template.json')
        data = json.load(f)
        f.close
        data['parameters']['SubOfVnetGW']['defaultValue'] = form.SubOfVnetGW.data
        data['parameters']['vNetGWRG']['defaultValue'] = form.vNetGWRG.data
        data['parameters']['PrivateCloudAddressSpace']['defaultValue'] = form.PrivateCloudAddressSpace.data
        data['parameters']['vNetGWvNet']['defaultValue'] = form.vNetGWvNet.data
        data['parameters']['PrivateCloudName']['defaultValue'] = form.PrivateCloudName.data
        data['parameters']['GatewayName']['defaultValue'] = form.GatewayName.data
        data['parameters']['OnPremExpressRouteAuthorizationKey']['defaultValue'] = form.OnPremExpressRouteAuthorizationKey.data
        data['parameters']['OnPremExpressRouteId']['defaultValue'] = form.OnPremExpressRouteId.data
        data['parameters']['InternetStatus']['defaultValue'] = form.InternetStatus.data
        fname = uuid.uuid4()
        #with open("app\static\{fname}.json".format(fname=fname),'w') as f:
        #    json.dump(data,f)
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
        blobstorename = os.getenv('AZURE_BLOB_STORE_NAME')
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        blob_client = blob_service_client.get_blob_client(container="templates", blob="{fname}.json".format(fname=fname))        
        #with open("app\static\{fname}.json".format(fname=fname), "rb") as data:
        #    blob_client.upload_blob(data)
        blob_client.upload_blob(data)
        #os.remove("app\static\{fname}.json".format(fname=fname))
        link = urllib.parse.quote("https://{blobstorename}.blob.core.windows.net/templates/{fname}.json".format(blobstorename=blobstorename, fname=fname), safe='')
        flash('<a href="https://portal.azure.com/#create/Microsoft.Template/uri/{link}" target="_blank">Click Here To Deploy https://portal.azure.com/#create/Microsoft.Template/uri/{link}</a>'.format(link=link))
    else:
        flash("All Values Required","error")
    return render_template('index.html',title='AVS ARM Template Generator', form = form )
