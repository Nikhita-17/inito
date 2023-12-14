FROM python
WORKDIR /a
COPY . /a
CMD ["python3","a.py"]