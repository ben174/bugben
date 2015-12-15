FROM python:2-onbuild
CMD gunicorn bugben.wsgi

