FROM python:2-onbuild
RUN ./manage.py collectstatic --noinput
CMD gunicorn -b 0.0.0.0:8116 bugben.wsgi
EXPOSE 8116
