FROM node:19-alpine
WORKDIR /frontend
COPY . .
RUN npm run build