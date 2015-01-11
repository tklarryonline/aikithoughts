'''
Created by tklarryonline on Jan 11, 2015.
'''
from flask.ext.assets import Bundle


main_css = Bundle(
    'scss/main.scss',
    filters='pyscss',
    output='css/main.css'
)