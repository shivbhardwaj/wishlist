from system.core.model import Model

class Wishlist(Model):
    def __init__(self):
        super(Wishlist, self).__init__()

    def success(self, id):
        query="SELECT * FROM users WHERE id=:id"
        data={'id':id}
        return self.db.query_db(query, data)

    def login(self, info):
        errors=[]
        query="SELECT * FROM users WHERE username=:username"
        data={
            'username':info['username'], 
            'password': info['password']
        }
        user_login=self.db.query_db(query,data)
        if user_login and self.bcrypt.check_password_hash(user_login[0]['password'], info['password']):
            return {'status': True, "user_login":user_login}
        else:
            errors.append('Invalid user or password!')
            return {'status': False, "errors": errors} 
        #check PW and if validates, return success w/ user data 
        # Go back to Controller

    def register(self, info):
        #EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors=[]
        if not info['name']:
            errors.append('Name cannot be blank')
        elif len(info['name'])<3:
            errors.append('Name must be at least 3 characters long')
        if not info['username']:
            errors.append('Username cannot be blank')
        elif len(info['username'])<3:
            errors.append('Username must be at least 3 characters long')
        # if not info['email']:
        #     errors.append('Email cannot be blank')
        # elif not EMAIL_REGEX.match(info['email']):
        #     errors.append('Email format must be valid')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password'])<8:
            errors.append('Password must be at least 8 characters long')
        elif info['password'] != info['pconfirm']:
            errors.append('Password and confirmation must match!')
        elif not info['hired']:
            errors.append('Hired date cannot be blank')
        if errors:
            return {'status': False, "errors": errors}
        else:
            encrypt = self.bcrypt.generate_password_hash(info['password'])
            query = "INSERT INTO users (name, username, password, hired, created_at, updated_at) VALUES (:name, :username, :password, :hired, NOW(), NOW())"
            data={"name":info['name'], "username":info['username'], "password":encrypt, "hired":info['hired']}
            #get_user_query="SELECT * FROM users ORDER BY id DESC LIMIT 1"
            user_id = self.db.query_db(query, data)
            return { "status": True, "user_id": user_id}

    def prod_by_user(self, id):
        query="SELECT users.id as user_id, users.username, products.name, products.created_at, products.users_id as added_by, products.id as product_id FROM users JOIN products on users.id=products.users_id JOIN favorites on users.id=favorites.users_id WHERE favorites.users_id=:user_id"
        data={'user_id':id}
        print self.db.query_db(query, data)
        print "query from prod by user method"
        print "query from prod by user method"
        print "query from prod by user method"
        print "query from prod by user method"
        print "query from prod by user method"
        print "query from prod by user method"
        return self.db.query_db(query, data)

    def remaining_prods(self, id):
        query="SELECT users.id as user_id, users.username, products.name, products.created_at, products.users_id as added_by, products.id as product_id FROM users JOIN products on users.id=products.users_id JOIN favorites on users.id=favorites.users_id WHERE favorites.users_id!=:user_id"
        data={'user_id':id}
        return self.db.query_db(query, data)

    def add_prod(self, id, info):
        query="INSERT INTO products (name, created_at, updated_at, users_id) VALUES (:name, NOW(), NOW(), :users_id)"
        data={'users_id':id, "name":info['name']}
        return self.db.query_db(query, data)

    def wish_items(self, id):
        query="SELECT products.name, products.id, favorites.users_id, users.username from products join favorites on products.id=favorites.products_id join users on favorites.users_id=users.id where products.users_id=:users_id"
        data={'users_id':id}
        print self.db.query_db(query, data)
        print id, "this is the id"
        print "this is the wish item method"
        print "this is the wish item method"
        print "this is the wish item method"
        print "this is the wish item method"
        print "this is the wish item method"
        return self.db.query_db(query, data)

    def remove_fav(self, id):
        query="DELETE from products where users_id=:id"
        data={'users_id':id}
        return self.db.query_db(query, data)

    # def users_fav(self, id):
    #     query="SELECT users.username from users join favorites on users.id = favorites.users_id join products on favorites.products_id = products.id where products.id=:product"
























            