FROM python

WORKDIR /app

COPY userAPI/app.py ./

RUN pip install flask

ENV PORT=8081

EXPOSE 8081

CMD [ "python", "app.py" ]