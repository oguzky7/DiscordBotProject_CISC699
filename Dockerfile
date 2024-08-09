FROM python
WORKDIR /app
RUN pip install --no-cache-dir discord pandas datetime requests bs4
COPY . /app
CMD [ "python", "main.py" ]