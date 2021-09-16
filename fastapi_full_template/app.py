import os
import io
from fastapi import FastAPI

from .db import create_db_and_tables, engine
from .routes import main_router


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("VERSION")
    """
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


description = """
fastapi_full_template API helps you do awesome stuff. 🚀
"""

app = FastAPI(
    title="fastapi_full_template",
    description=description,
    version=read("VERSION"),
    terms_of_service="http://fastapi_full_template.com/terms/",
    contact={
        "name": "leohakim",
        "url": "http://fastapi_full_template.com/contact/",
        "email": "leohakim@fastapi_full_template.com",
    },
    license_info={
        "name": "The Unlicense",
        "url": "https://unlicense.org",
    },
)


app.include_router(main_router)


@app.on_event("startup")
def on_startup():
    create_db_and_tables(engine)
