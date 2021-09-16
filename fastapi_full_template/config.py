import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="fastapi_full_template",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="fastapi_full_template_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from fastapi_full_template.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export fastapi_full_template_KEY=value
export fastapi_full_template_KEY="@int 42"
export fastapi_full_template_KEY="@jinja {{ this.db.uri }}"
export fastapi_full_template_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
fastapi_full_template_ENV=production fastapi_full_template run
```

Read more on https://dynaconf.com
"""
