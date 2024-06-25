from django.urls import path, include
from . import views
urlpatterns = [
    #Doglover
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('alimentos/', views.alimentos, name="alimentos"),
    path('accesorios/', views.accesorios, name="accesorios"),
    path('servicios/', views.servicios, name="servicios"),
    path('fichas/', views.fichas, name="fichas"),
    path('calc/', views.calc, name="calc"),
    path('login_view/', views.login_view, name="login_view"),
    #Crud Usuarios
    path('user_list/', views.user_list, name='user_list'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  # URL para eliminar usuario
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    #Productos Crud
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    #Sesiones
    path("accounts/", include("django.contrib.auth.urls")),
    path('menu/', views.menu, name="menu"),
    path('home', views.home, name='home'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    #Login
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup, name='signup'),
    #Carrito
    path('carrito',views.carrito,name="carrito"),
    path('',views.tienda,name="Tienda"),
    path('agregar/<int:producto_id>/',views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/',views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/',views.restar_producto, name="Sub"),
    path('limpiar/',views.limpiar_carrito, name="CLS"),
    ]
    
