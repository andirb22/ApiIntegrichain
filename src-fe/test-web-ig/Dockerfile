#stage 1
FROM node:16.17.0 as node
WORKDIR /app
COPY . /app
#RUN npm install
RUN yarn
#RUN npm run build --prod
CMD ng serve --host 0.0.0.0
