from utils.repository import SqlRepository
from models.user import UserModel


class UserRepository(SqlRepository):
    model=UserModel