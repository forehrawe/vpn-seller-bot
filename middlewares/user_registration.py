from aiogram import BaseMiddleware
from database.config import SessionLocal
from database.models import User

class UserRegistration(BaseMiddleware):
    async def __call__(
        self,
        handler,
        event,
        data
    ):
        print('midd started')
        db = SessionLocal()
        user_account_id = event.from_user.id
        
        user = db.query(User).filter(User.account_id==user_account_id).first()
        
        if not user:
            new_user = User(account_id=user_account_id)
            db.add(new_user)
            db.commit()
            data['is_new_user'] = True
        else:
            data['is_new_user'] = False
        db.close()
        
        return await handler(event, data)