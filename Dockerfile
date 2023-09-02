# backend
FROM python-3.10-alpine as backend

# Base build
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Multistage build
COPY /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app
ENV PYTHONUNBUFFERED 1
EXPOSE 8080
ARG CACHEBUST=0
RUN python manage.py collectstatic --noinput
CMD ["python", "-m", "gunicorn", "--preload", "-c", "/app/gunicorn.py", "aaps.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]

# frontend
FROM nginx:1.23-alpine AS frontend

COPY templates/main.html /usr/share/nginx/html
COPY static/css /usr/share/nginx/html
COPY static/js /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

COPY --from=backend /app/static/img /usr/share/nginx/html/static
COPY --from=backend /etc/nginx/nginx.conf /etc/nginx/nginx.conf
