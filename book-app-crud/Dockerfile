#stage 1
FROM node:16.17.0-alpine3.16 as node
#WORKDIR /dist/src/app
RUN npm cache clean --force
COPY . /app
WORKDIR /app
RUN npm install
RUN npm run build --prod
FROM nginx:latest AS ngi
COPY --from=node /app/dist/angular-14-crud-example /usr/share/nginx/html
#COPY --from=node /app/nginx.conf /etc/nginx/nginx.conf
#COPY /nginx.conf  /etc/nginx/conf.d/default.conf




