# FaceTrix

It is a Facial Recognition based Criminal System for CCTV feeds made in VueJS for frontend and for backend, it uses FastAPI server.

## Project Setup

To get started with local development, follow the steps below to install the necessary dependencies.

### Client-Side Dependencies

We use **pnpm** for managing dependencies in the VueJS. Ensure that all package installations or removals are done using `pnpm`.

```bash
cd client # navigate to client directory
pnpm install
```

### Server-Side Dependencies

Our FastAPI server uses **pipenv** to manage a virtual Python environment. Ensure you use `pipenv` for all package installations and removals.

```bash
cd Server # navigate to server directory
pipenv shell # Activate the virtual environment
pipenv install
```

### Running the Development Server

Starting the Client

```bash
cd client
pnpm run dev
```

Starting the Backend

```bash
cd server
uvicorn main:app --reload
```
