# grabgrub
Grabgrub MSYS22 WebApp project repository. Testing for deployment.

Feel free to look around the code, although a lot are redundant and could use some fixing. Do note, however that this is for the heroku app deployment, as some settings have changed to better suit it for deployment.

About the project:

GrabGrub is the project name, as such multiple apps and pages can be fitted inside this single project. Kiosk is currently the only working application, although it is very basic.

Happy coding!

# Installation Instructions

First, install `virtualenv` using the `pip` package manager

```bash
pip install virtualenv
```

Create new virtual environment
```bash
python -m venv env
```

Activate the virtual environment

In Linux:
```bash
source env/bin/activate
```

In Windows:
```bash
env\Scripts\activate.bat
```

Install libraries from from `requirements.txt`

```bash
pip install -r requirements.txt
```

# Running the app using Docker

First, build the Docker image using the following command:

```bash
docker build -t grab_grub_dev .
```

Then, run the Docker image as a container in detached mode using the following command:

```bash
docker run -p 8080:8080 -d grab_grub_dev
```