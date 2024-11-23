from aiogram_i18n.managers import BaseManager
from aiogram.types.user import User


# class UserManager(BaseManager):
#     async def get_locate(self, event_from_user: User, db: Database) :
#         default = event_from_user.language_code or self.default_locale
#         if db:
#             user_lang = db.get_lang(event_from_user.id)
#             if user_lang:
#                 return user_lang
#         return default


#     async def set_locate(self, locales: str, event_from_user: User, db: Database = None) -> None:
#         if db:
#             db.set_lang(event_from_user.id, locales)