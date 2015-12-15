FROM python:2-onbuild
CMD gunicorn -b 0.0.0.0:8116 bugben.wsgi
EXPOSE 8116
