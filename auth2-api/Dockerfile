FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install requests
RUN pip install psycopg2-binary fastapi[all]
RUN pip install pydantic
RUN pip install requests_oauthlib
RUN pip install python-dotenv 

COPY ./app /code/app  

ENV URL=http://localhost:3000/oauth2/token
ENV CLIENT_ID=4f76e525-47c4-4841-beb3-cd500fcb3e50
ENV CLIENT_SECRET=ce4da7f3-cba7-40f8-9674-a9fd6f98e80e

EXPOSE 9090  

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9090"]
