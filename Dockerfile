FROM python:3.10.4
ADD . /facebook-scraping
WORKDIR /facebook-scraping
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
RUN pip install -r requirements.txt