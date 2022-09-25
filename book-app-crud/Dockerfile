#stage 1
FROM node:16.17.0-alpine3.16 as node
WORKDIR /dist/src/app
RUN npm cache clean --force
COPY . /app
WORKDIR /app
RUN npm install
RUN npm run build --prod
FROM nginx:latest AS ngi
COPY --from=node /app/dist/angular-14-crud-example /usr/share/nginx/html
#COPY /nginx.conf  /etc/nginx/conf.d/default.conf


#RUN mkdir -p /app
#WORKDIR /app
#COPY package.json /app
#RUN npm install
#COPY . /app
#RUN npm run build --prod 
#FROM nginx:1.17.1-alpine
#COPY --from=node /app/dist/angular-14-crud-example /usr/share/nginx/html

