import flask
from . import db_session
from .news_model import News

blueprint = flask.Blueprint(
    'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/news')
def get_news():
    session = db_session.create_session()
    news = session.query(News).all()
    return flask.render_template('', news=news)


