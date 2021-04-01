import flask
from . import db_session
from .job_model import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    js = flask.jsonify({

    })
    return flask.render_template('jobs.html', jobs=jobs)
