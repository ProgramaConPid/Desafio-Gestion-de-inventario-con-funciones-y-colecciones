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
    | 6. Salir del programa                |
    ----------------------------------------

  """)
  
# Funcion para añadir producto
def add_product(name, price, amount):
  
  product = {
    "Producto": name,
    "Precio": int(price),
    "Cantidad": amount
  }
  
  products_list.append(product)
  
# Funcion para buscar producto
def search_product(product_name):
  
  for p in products_list:
    
    if p.get("Producto") == product_name:
      
      price = p.get("Precio")
      amount = p.get("Cantidad")
      
      return f"\n✅ Resultado de la busqueda => [Producto: {product_name.capitalize()}, Precio: {price}, Cantidad disponible: {amount}]"

# Funcion para verificar si el producto ingresado por el usuario se encuentra en el inventario
def check_product(product_name):
  
  found_product = False
          
  for p in products_list:
    
    if p.get("Producto") == product_name:
      found_product = True
      return found_product

# Funcion para modificar el precio de un producto especifico
def update_product_price(product_name, new_price):
  
  for i in range(len(products_list)):
    
    if products_list[i].get("Producto") == product_name:
      
      price = products_list[i].get("Precio")
      products_list[i]["Precio"] = new_price
      
      print(f"\n✅ [Precio anterior del producto {product_name.capitalize()}: {price} - Precio actualizado {int(products_list[i]["Precio"])}]")

# Funcion para eliminar un producto especifico del inventario
def delete_product(product_name):

  for index, product in enumerate(products_list):

    if product.get("Producto") == product_name:

      products_list.pop(index)
         
flag = True
while flag:
  show_menu()

  empty_products_message = "⚠️  Aún no hay ningun producto en el inventario, Ingresa la opcion #1 y añade un producto."
  
  try:
    
    # Entrada: se le solicita al usuario ingresar el numero de la opcion a realizar
    user_option = int(input("Ingresa el numero de la opcion a realizar: "))
    
    print("")
    
    match user_option:
      
      case 1:
        
        # Entrada: Nombre del producto
        product_name = str(input("🛒 Ingresa el nombre del producto: ")).lower()
        
        while not all(part.isalpha() for part in product_name.split()):
          product_name = input("❌ ERROR! Ingresa un producto válido (solo letras y espacios): ")
          
        # Entrada: Precio del producto
        product_price = str(input("💲 Ingresa el precio del producto: "))
        
        # Validacion precio
        while not product_price.isdigit() or len(product_price) > 6:
          print("\n❌ ERROR: Ingresa solo números (sin letras ni símbolos) y que no exceda 6 dígitos. ")
          product_price = str(input("Ingresa de nuevo el precio del producto: "))
          
        product_amount = str(input("📦 Ingresa la cantidad a añadir (MIN 1 - MAX 10): ")) 
        
        # Validacion cantidad
        while not product_amount.isdigit() or len(product_amount) > 2:
          print("\n❌ ERROR: Ingresa solo números (sin letras ni símbolos) y que no exceda 2 dígitos.")
          product_amount = str(input("Ingresa de nuevo la cantidad a añadir: "))
          
        product_amount = int(product_amount)
        
        # Validar que la cantidad ingresada se encuentre en el rango permitido
        while product_amount < 0 or product_amount > 10:
          print("\n❌ ERROR, Ingresaste una cantidad que no se encuentra en el rango permitido.")
          product_amount = int(input("Ingresa de nuevo una cantidad valida: "))
          
        # Separador  
        print("")
          
        # Invocar funcion que recibe los datos del producto y los agrega a un diccionario y luego a la lista de productos
        add_product(product_name, product_price, product_amount)
        
        print(f"\n✅ El producto {product_name.capitalize()} se añadio correctamente al inventario\n")
        
      case 2:
        
        if len(products_list) > 0:
          
          # Entradaa: Solicitar nombre del producto a buscar
          product_to_search = str(input("Ingresa el nombre del producto a buscar: ")).lower()
          
          while not product_to_search.isalpha():
            product_to_search = str(input("❌ ERROR!, Ingresa un producto valido: ")).lower()
            
          # Comprobar si el producto ingresado se encuentra en la lista deproductos
          found_product = check_product(product_to_search)
            
          # Validacion de producto encontrado o no encontrado
          if not found_product:
            print(f"\n❌ El producto {product_to_search.capitalize()} no se encontro en el inventario.")
          else:
            # Se asigna la funcion buscar producto a la variable resultado y se imprime para ver el retorno de la funcion
            search_product_result = search_product(product_to_search)
            print(search_product_result)
         
        else:
          print(empty_products_message)
          
      case 3:
        
        # Verificar que hayan productos en la lista de productos
        if len(products_list) > 0:
          product_to_update_price = str(input("Ingresa el nombre del producto al cual se le modificara el precio: ")).lower() 
          
          # Validar el nombre del producto
          while not product_to_update_price.isalpha():
            product_to_update_price = str(input("❌ ERROR!, Ingresa un nombre de producto valido: "))
            
          # Invocar la funcion que realiza la busqueda del producto
          found_product = check_product(product_to_update_price)
            
          # Verificacion si el producto fue encontrado o no
          if not found_product:
            print(f"\n⚠️ El producto ingresado {product_to_update_price.capitalize()} no se encuentra en el inventario. \n")
          else:
            # Entrada: Se solicita el nuevo precio al usuario
            new_product_price = str(input(f"Ingresa el nuevo precio del producto {product_to_update_price}: "))
            
            # Validar que el precio ingresado sea valido
            while not new_product_price.isdigit() or len(new_product_price) > 6:
              print("❌ ERROR: Ingresa solo números (sin letras ni símbolos) y que no exceda 6 dígitos. ")
              new_product_price = str(input("Ingresa nuevamente el nuevo precio: "))
              
            # Invocar la funcion que modifica el precio del producto
            update_product_price(product_to_update_price, new_product_price)
        
        else:
          print(empty_products_message)
          
      case 4: 
        
        if len(products_list) > 0:
          product_to_delete = str(input("Ingresa el nombre del producto a eliminar: "))

          # Validar el nombre del producto
          while not product_to_delete.isalpha():
            product_to_delete = str(input("ERROR!, Ingresa un nombre de producto valido: "))

          # Comprobar si el producto ingresado se encuentra en la lista deproductos
          found_product = check_product(product_to_delete)

          if not found_product:
            print(f"\n ⚠️ El producto ingresado {product_to_delete.capitalize()} no se encuentra en el inventario. \n")
          else:
            # Entrada: Se solicita el nuevo precio al usuario
            delete_product(product_to_delete)
            print(f"✅ El producto {product_to_delete.capitalize()} fue removido del inventario correctamente.")
        
        else:
          print(empty_products_message)

      case 5:
        
        # Validar que haya productos en la lista de productos
        if len(products_list) > 0:

          print("Los productos registrados en el inventario son los siguientes: ")

          print("")

          total_price, total_amount = 0, 0

          for product in products_list:
            
            product_index = products_list.index(product)
            print(f"Producto #{product_index + 1}: {product}")

            # Obtener el precio de cada producto
            product_price = float(product["Precio"])
            
            # Precio total de los productos
            total_price += product_price

            # Obtener la cantidad de cada producto
            product_amount = float(product["Cantidad"])

            # Cantidad total de los productos
            total_amount += product_amount

          # Funcion lambda encargada de realizar la operacion que calcula el valor total de los productos del inventario
          total_inventory_value = lambda total_p, total_a: (total_p * total_a)

          print(f"\n🧮 El valor total de los productos almacenados en el inventario es: {total_inventory_value(total_price, total_amount)}")

      case 6: 
        print("\nSaliendo del programa...")

      case _:
        print(f"❌ La opcion ingresada {user_option} no es valida.")
          
  except ValueError:
    print("‼️ ERROR, Ingresaste un valor invalido")