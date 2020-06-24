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

RUN mkdir /code
WORKDIR /code

RUN apt-get install -y zsh

# install library
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install selenium
RUN pip install pandas
RUN pip install Pillow
RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install scrapy

COPY . /code/
COPY .zshrc /root/
RUN chsh -s /bin/zsh
