FROM python:3.8.5
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
#RUN python3 -m nltk.downloader popular
COPY . /app/
RUN apt-get update && apt-get install -y gettext libgettextpo-dev \
    python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils tesseract-ocr flac \
    ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig \
    && git clone https://github.com/vishnubob/wait-for-it.git && echo "OK: wait-for-it cloned" \
    && chmod +x ./wait-for-it/wait-for-it.sh

