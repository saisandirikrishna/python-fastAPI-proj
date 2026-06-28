users = []


def get_users():
    return users


def create_user(user):
    user_data = {
        "id": len(users) + 1,
        "name": user.name,
        "email": user.email
    }

    users.append(user_data)

    return user_data