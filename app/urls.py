from bottle_neck import Router
from app.views import AppView

router = Router()

router.register_handler(AppView, '/')
