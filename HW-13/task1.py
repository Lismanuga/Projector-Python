

def is_admin(func):
    def wrapper(**kwarqs):
        user_type = kwarqs.get('user_type')
        if user_type == 'admin':
            return func(**kwarqs)
        else:
            raise ValueError('Permission denied')
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    print('dangerous operation')


try:
    show_customer_receipt(user_type='admin')
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(e)
