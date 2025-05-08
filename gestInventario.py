# Entregable semana 3 - Gestion de inventario con funciones y colecciones

products_list = []

# Menu
def show_menu():
  
  print("""
       
    --- TIENDA RIWI (MENU DE OPCIONES) ---
        
    ----------------------------------------
    | 1. Añadir producto                   |
    | 2. Buscar producto                   |
    | 3. Actualizar precio                 |
    | 4. Eliminar producto                 |
    | 5. Mostrar valor total del inventario|
    ----------------------------------------

  """)
  
# Funcion para añadir producto
def add_product(name, price, amount):
  
  product = {
    "Producto": name,
    "Precio": float(price),
    "Cantidad": amount
  }
  
  products_list.append(product)
  
# Funcion para buscar producto
def search_product(product_name):
  
  for p in products_list:
    
    if p.get("Producto") == product_name:
      
      price = p.get("Precio")
      amount = p.get("Cantidad")
      
      return f"\n- Resultado de la busqueda => [Producto: {product_name}, Precio: {price}, Cantidad disponible: {amount}]"
    
def check_product(product_name):
  
  found_product = False
          
  for p in products_list:
    
    if p.get("Producto") == product_name:
      found_product = True
      return found_product
    
def update_product_price(product_name, new_price):
  
  for i in range(len(products_list)):
    
    if products_list[i].get("Producto") == product_name:
      
      price = products_list[i].get("Precio")
      products_list[i]["Precio"] = new_price
      
      print(f"\n- [Precio anterior del producto {product_name}: {price} - Precio actualizado {float(products_list[i]["Precio"])}]")
         
flag = True
while flag:
  show_menu()
  
  try:

    user_option = int(input("Ingresa el numero de la opcion a realizar: "))
    
    print("")
    
    match user_option:
      
      case 1:
        
        # Entrada: Nombre del producto
        product_name = str(input("Ingresa el nombre del producto: ")).lower()
        
        # Validacion producto
        while not product_name.isalpha():
          product_name = str(input("ERROR!, Ingresa un producto valido: "))
          
        # Entrada: Precio del producto
        product_price = str(input("Ingresa el precio del producto: "))
        
        # Validacion precio
        while not product_price.isdigit() or len(product_price) > 6:
          print("\nERROR: Ingresa solo números (sin letras ni símbolos) y que no exceda 6 dígitos. ")
          product_price = str(input("Ingresa de nuevo el precio del producto: "))
          
        product_amount = str(input("Ingresa la cantidad a añadir (MIN 1 - MAX 10): ")) 
        
        # Validacion cantidad
        while not product_amount.isdigit() or len(product_amount) > 2:
          print("\nERROR: Ingresa solo números (sin letras ni símbolos) y que no exceda 2 dígitos.")
          product_amount = str(input("Ingresa de nuevo la cantidad a añadir: "))
          
        product_amount = int(product_amount)
        
        while product_amount < 0 or product_amount > 10:
          print("\nERROR, Ingresaste una cantidad que no se encuentra en el rango permitido.")
          product_amount = int(input("Ingresa de nuevo una cantidad valida: "))
          
        print("")
          
        # Invocar funcion que recibe los datos del producto y los agrega a un diccionario y luego a la lista de productos
        add_product(product_name, product_price, product_amount)
        
        print(f"\nEl producto {product_name} se añadio correctamente al inventario\n")
        
      case 2:
        
        if len(products_list) > 0:
          
          # Entradaa: Solicitar nombre del producto a buscar
          product_to_search = str(input("Ingresa el nombre del producto a buscar: ")).lower()
          
          while not product_to_search.isalpha():
            product_to_search = str(input("ERROR!, Ingresa un producto valido: ")).lower()
            
          # Comprobar si el producto ingresado se encuentra en la lista deproductos
          found_product = check_product(product_to_search)
            
          # Validacion de producto encontrado o no encontrado
          if not found_product:
            print(f"\n* El producto {product_to_search} no se encontro en el inventario *")
          else:
            search_product_result = search_product(product_to_search)
            print(search_product_result)
         
        else:
          print("Aún no hay ningun producto en el inventario, Ingresa la opcion #1 y añade un producto.")
          
      case 3:
        
        if len(products_list) > 0:
          product_to_update_price = str(input("Ingresa el nombre del producto al cual se le modificara el precio: ")).lower() 
          
          while not product_to_update_price.isalpha():
            product_to_update_price = str(input("ERROR!, Ingresa un nombre de producto valido: "))
            
          found_product = check_product(product_to_update_price)
            
          if not found_product:
            print(f"\n* El producto ingresado {product_to_update_price} no se encuentra en el inventario. *\n")
          else:
            new_product_price = str(input(f"Ingresa el nuevo precio del producto {product_to_update_price}: "))
            
            while not new_product_price.isdigit() or len(new_product_price) > 6:
              print("ERROR: Ingresa solo números (sin letras ni símbolos) y que no exceda 6 dígitos. ")
              new_product_price = str(input("Ingresa nuevamente el nuevo precio: "))
              
            update_product_price(product_to_update_price, new_product_price)
        
        else:
          print("Aún no hay ningun producto en el inventario, Ingresa la opcion #1 y añade un producto.")
          
      case 4: 
        
        product_to_delete = str(input("Ingresa el nombre del producto a eliminar"))
          
            
  except ValueError:
    print("ERROR, Ingresaste un valor invalido")