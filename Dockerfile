# Base build
FROM python:3.10-alpine as py-singlestage-builder

RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Now multistage build
FROM python:3.10-alpine AS python-multistage-builder
COPY --from=py-singlestage-builder /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=py-singlestage-builder /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED 1
EXPOSE 8080
ARG CACHEBUST=0
RUN python manage.py collectstatic --noinput
CMD ["python", "-m", "gunicorn", "--preload", "-c", "/app/gunicorn.py", "aaps.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]

# nginx
FROM node:18-alpine as nodejs-builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY ./ .
RUN npm run build

FROM nginx:1.23-alpine AS nginx-builder
COPY --from=nodejs-builder /app/dist /usr/share/nginx/html
EXPOSE 80
COPY ./nginx.conf /etc/nginx/nginx.conf
