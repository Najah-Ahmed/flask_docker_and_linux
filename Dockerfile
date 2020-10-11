FROM python:alpine3.8

WORKDIR /user/src/app


COPY . .

RUN pip install -r requirement.txt




ENTRYPOINT ["python","app.py"] 