
FROM python:3.7

ENV strings=tran,ngoc,phi,tran,ngoc

COPY . sparse_array/   

RUN pip install Flask

ENTRYPOINT [ "python3" ]

CMD [ "sparse_array/main.py" ]