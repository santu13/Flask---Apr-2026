FROM python:3.10.4-slim-bullseye
WORKDIR /docker

# Install the application dependencies
COPY Requirements.txt ./
RUN pip install -r Requirements.txt

# Copy in the source code
COPY ./ ./

CMD ["python","-m", "flask","--app", "loan","run","--host", "0.0.0.0"]