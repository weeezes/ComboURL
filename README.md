# ComboURL
↑ ↑ ↓ ↓ ← → ← → B A Start

ComboURL is a short exercise in writing an URL shortener.
It's built on top of [Flask](http://flask.pocoo.org/), which is
the only requirement for the project.

Currently there's no persistent storage, the in-memory database
is not thread safe so take this into account when running ComboURL :).

## API

### POST /shorten
**Parameters:** `link` should contain the link to shorten
**Returns:** a combo for the shortened link in `text/plain` format.

### GET /{combo}
**Returns:**
* 301 if a link matching `combo` is found, redirects to the link
* 404 error if no link matches `combo`

## Running ComboURL

Installing Flask and Gunicorn

    pip install Flask
    pip install gunicorn

Running the service in port 5000

    cd ComboURL/
    gunicorn -b 127.0.0.1:5000 main:app

## Future

A persistent storage should be implemented, eg. by using Redis. This
would require a new `combos.py` module with tiny tweaks. If I understood
the Redis documentation correctly this would also make the application
thread safe if used correctly.