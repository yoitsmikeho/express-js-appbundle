FROM node:16.19.1
#ARG JF_TOKEN

# Create app directory
WORKDIR /usr/src/app
COPY package*.json ./
RUN apt-get update && \
    apt-get install -y curl make ncat && \
    apt-get clean
RUN curl -fL https://install-cli.jfrog.io | sh

# If you are building your code for production
#RUN jf c import ${JF_TOKEN} && \
#    jf npmc --repo-resolve=fgr-npm-remote && \
#    jf npm i --omit dev
#EXPOSE 3000

COPY server.js ./
COPY public public/
COPY views views/
CMD [ "node", "server.js" ]
