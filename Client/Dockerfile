FROM python

WORKDIR /app

COPY app.py ./

RUN pip install http.client

ENV PORT=8081

EXPOSE 8081

CMD [ "python", "app.py" ]