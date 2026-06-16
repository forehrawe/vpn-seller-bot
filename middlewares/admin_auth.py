from aiogram import BaseMiddleware
from database.config import session_local
from database.models import User

class AdminAuthentication(BaseMiddleware):
    async def __call__(self, handler, event, data):
        db = session_local()
        user = db.query(User).filter(User.account_id==event.from_user.id).first()
        
        if user.is_admin:
            return await handler(event, data)
        else:
            return None