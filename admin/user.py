from sqladmin import ModelView

from models.user import UserModel


class UserAdmin(ModelView, model=UserModel):
    column_list = [UserModel.id, UserModel.name]