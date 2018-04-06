import bottle
from app.urls import router


wsgi = bottle.Bottle()

router.mount(wsgi)
