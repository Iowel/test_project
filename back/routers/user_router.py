from datetime import datetime
from fastapi import APIRouter, HTTPException, Response
from routers.schemas import User, UserList, UpdateUserSchema


users = [
    User(
        id=1,
        username="andreq",
        first_name="Aquaewe",
        last_name="AWDawd",
        age=28,
        created_at=datetime.now(),
    ),
    User(
        id=2,
        username="marty",
        first_name="Marta",
        last_name="Martina",
        age=16,
        created_at=datetime.now(),
    ),
    User(
        id=3,
        username="lisik",
        first_name="Danil",
        last_name="Ivanov",
        age=22,
        created_at=datetime.now(),
    ),
]


# POST, GET, DELETE, PUT

user_router = APIRouter(prefix="/users", tags=["пользователи"])


@user_router.get("/", name="Все пользователи", response_model=UserList)
def get_all_users():
    return UserList(count=len(users), users=users)


@user_router.post("/", name="Добавить пользователя", response_model=User)
def create_user(user: User):
    users.append(user)
    return user


@user_router.get("/{user_id}", name="Получить пользователя", response_model=User)
def get_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@user_router.delete("/{user_id}", name="Удалить пользователя", response_class=Response)
def delete_user(user_id: int):
    for i, user in enumerate(tuple(users)):
        if user.id == user_id:
            del users[i]
            break
        return Response(status_code=204)


@user_router.put("/{user_id}", name="Обновить данные пользователя", response_model=User)
def update_user(user_id: int, new_user_data: UpdateUserSchema):
    print(new_user_data.dict())
    for i in range(len(users)):
        if users[i].id == user_id:
            data = new_user_data.dict()
            for key in data:
                if data[key] is not None:
                    setattr(users[i], key, data[key])
            return users[i]
        raise HTTPException(status_code=404, detail="User not found!")
    