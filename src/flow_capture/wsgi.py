import atexit
import gc
import environ

from ...config import WebAppConfig
from ...logging import setup_logging, setup_sentry
from .app_maker import make_wsgi_app
from .instrumentation import flask_metrics 

app_cfg = environ.to_config(WebAppConfig)
setup_logging(app_cfg.env, app_cfg.backend_id)
setup_sentry(app_cfg)

application, cleanup = make_wsgi_app(app_cfg)
atexit.register(cleanup)

flask_metrics.init_app(application)

gc.freeze()