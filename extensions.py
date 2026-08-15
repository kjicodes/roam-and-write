import os
import ssl
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from celery import Celery

#Initialize db
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
migrate = Migrate()

#Async processing for AI generated content
redis_url = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
celery = Celery(
    "roam-and-write",
    broker=redis_url,
    backend=redis_url
)
if redis_url.startswith("rediss://"):
    celery.conf.broker_use_ssl = {"ssl_cert_reqs": ssl.CERT_NONE}
    celery.conf.redis_backend_use_ssl = {"ssl_cert_reqs": ssl.CERT_NONE}

