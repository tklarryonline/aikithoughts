from flask.ext.assets import Bundle


normalize_css = Bundle(
    'bower_components/foundation/css/normalize.css',
    filters='cssmin',
    output='css/normalize.css'
)


main_css = Bundle(
    'scss/main.scss',
    filters='pyscss',
    output='css/main.css',
    depends=(
        '**/*.scss'
    )
)