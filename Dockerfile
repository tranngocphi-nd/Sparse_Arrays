
FROM python:3.7

ENV strings=tran,ngoc,phi,tran,ngoc

COPY . sparse_array/  

RUN pip install -r sparse_array/requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "sparse_array/main.py" ]