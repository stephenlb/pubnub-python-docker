# docker build -t python-sdk . && docker run python-sdk
# sudo tcpdump host ps1.pndsn.com

#FROM python:2
FROM python:3.8.2-slim
RUN python -m pip install --upgrade pip
RUN pip install pycryptodomex requests cbor2
COPY pubnub pubnub
COPY pubnub-python-publish.py .
COPY pubnub-python-subscribe.py .
ENV PYTHONUNBUFFERED 1
CMD ["python", "pubnub-python-publish.py"]
