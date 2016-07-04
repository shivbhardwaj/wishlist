from system.core.router import routes
routes['default_controller'] = 'Wishlists'
routes['POST']['/login']="Wishlists#login"
routes['POST']['/register']="Wishlists#register"
routes['GET']['/dashboard']="Wishlists#dashboard"
routes['GET']['/wish_item/<id>']="Wishlists#wish_item"
routes['POST']['/remove']="Wishlists#remove"
routes['POST']['/add']="Wishlists#add"
routes['GET']['/wish_items/create']='Wishlists#create'
routes['POST']['/wish_item/create/process']='Wishlists#create_process'
routes['GET']['/logout']='Wishlists#logout'
