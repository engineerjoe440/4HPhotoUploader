# 4HPhotoUploader
Photo consent and uploader prototype for 4-H programs.

### Frontend:
The frontend of this system is a React-js site.

### Backend:
The backend is a Python/FastAPI server responsible for serving the static files
and accessing permitting file uploads.

### Linking frontend and backend (React/FastAPI):
With some minor modifications made to the FastAPI configuration,
[this guide on using Flask and React](https://blog.learningdollars.com/2019/11/29/how-to-serve-a-reactapp-with-a-flask-server/)
was used to develop the link between the two ecosystems.

## Rebuilding React Components for Serving

From the `frontend` directory, issue the following command:

```shell
npm run build
```

## Running Server for Development

From the `backend` directory, issue the following command:

```shell
uvicorn main:app --reload
```