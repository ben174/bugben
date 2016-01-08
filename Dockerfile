FROM python:2-onbuild
RUN /usr/src/app/manage.py collectstatic --noinput
CMD /usr/local/bin/gunicorn bugben.wsgi:application -w 2 -b :8000
EXPOSE 8000
