FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN secondhand_e_commerce_svc create-db
RUN secondhand_e_commerce_svc populate-db
RUN secondhand_e_commerce_svc add-user -u admin -p admin
EXPOSE 5000
CMD ["secondhand_e_commerce_svc", "run"]
