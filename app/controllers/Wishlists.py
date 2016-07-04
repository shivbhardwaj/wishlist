from system.core.controller import *

class Wishlists(Controller):
    def __init__(self, action):
        super(Wishlists, self).__init__(action)
        self.load_model('Wishlist')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def register(self):
        create_status=self.models['Wishlist'].register(request.form)
        if create_status['status']:
            session['user_id']=create_status['user_id']
            return redirect('/dashboard')
        else: 
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/')
    
    def login(self):
        #whatever we set equal is what is returned
        users=self.models['Wishlist'].login(request.form)
        session['user_id']=users['user_login'][0]['id']
        print session['user_id']
        return redirect('/dashboard')

    def dashboard(self):
        user=self.models['Wishlist'].success(session['user_id'])
        print "the user I got back when I ran the success method in user controller: ", user
        products_by_user=self.models['Wishlist'].prod_by_user(session['user_id'])
        remain_products=self.models['Wishlist'].remaining_prods(session['user_id'])
        return self.load_view('dashboard.html', user=user[0], products_by_user=products_by_user, remain_products=remain_products)

    def wish_item(self, id):
        wish_item_id=self.models['Wishlist'].wish_items(session['user_id'])
        print wish_item_id
        print 'testtesttest'
        print 'testtesttest'
        print 'testtesttest'
        print 'testtesttest'
        return self.load_view('product.html', wish_item_id=wish_item_id)

    def remove(self, id):
        remove_favorite=self.models['Wishlist'].remove_fav(session['user_id'])
        return redirect('/dashboard')

    def create(self):
        return self.load_view('create.html')

    def create_process(self):
        create_prod=self.models['Wishlist'].add_prod(session['user_id'], request.form)
        return redirect ('/dashboard')

    def logout(self):
        session.pop('user_id')
        return redirect('/')