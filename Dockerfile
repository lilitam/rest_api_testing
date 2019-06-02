FROM python:3.6

COPY tests /tests

RUN pip install unittest2
RUN pip install requests

CMD ["python","-m","unittest","discover","-s","./tests/"]

