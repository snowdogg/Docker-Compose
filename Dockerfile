FROM python:alpine
WORKDIR /webapp
ADD flask_app /webapp
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
