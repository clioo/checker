# FROM python:3.8
# # MAINTAINER autochecker

# # install Chrome
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get -y update
# RUN apt-get install -y google-chrome-stable

# # install chromedriver
# RUN apt-get install -yqq unzip
# RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
# RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# # set display port to avoid crash
# ENV DISPLAY=:99

# # python dependenciess


# ENV PYTHONUNBUFFERED 1

# COPY ./requirements.txt /requirements.txt
# # RUN apk add --update --no-cache --virtual .tmp-build-deps \
# #     gcc libc-dev linux-headers musl-dev
# RUN pip install -r /requirements.txt
# # RUN apk del .tmp-build-deps

# RUN mkdir /app
# WORKDIR /app
# COPY ./app /app

# # -p for subdirectories
# # RUN adduser -D user
# # RUN chown -R user:user /vol/
# # RUN chmod -R 755 /vol/web
# # USER user
FROM python:3.8

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium

RUN mkdir /app
COPY ./app /app