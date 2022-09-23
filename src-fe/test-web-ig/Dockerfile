#stage 1
FROM node:16.17.0 as node
WORKDIR /app
COPY . /app
#RUN npm install
RUN yarn
#RUN npm run build --prod
RUN yarn run build --prod
#stage 2
FROM nginx:alpine
COPY --from=node /app/dist/angular-crud-rest-api /usr/share/nginx/html