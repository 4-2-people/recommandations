# Recommandations

Movie and series recommendation app project.

## Setup

To run the project, you will need [poetry][1] and [docker][2].

```bash
$ docker-compose up -d
$ poetry shell
(poetry) $ cd service
(poetry) $ alembic upgrade head
(poetry) $ python3 app.py
```

Once launched, project documentation is available at `http://0.0.0.0:8000/docs`.


[1]: https://python-poetry.org/docs/#installation
[2]: https://docs.docker.com/engine/install/
