from config.settings.base import *


ALLOWED_HOSTS = ["hostname"]
CORS_ORIGIN_ALLOW_ALL = False
DEBUG = False

# ===================== #
#   Logging Config      #
# ===================== #
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "file": {
            "format": ",".join([
                "[%(levelname)s]",
                "%(asctime)s",
                "%(pathname)s",
                "%(lineno)d",
                "%(message)s",
            ])
        },
    },
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": os.path.join(os.path.dirname(BASE_DIR), "log/develop.log"),
            "formatter": "file",
            "when": "D",
            "interval": 1,
            "backupCount": 7,
        }
    },
    "loggers": {
        "Application": {"handlers": ["file"], "level": "INFO"}
    },
}
