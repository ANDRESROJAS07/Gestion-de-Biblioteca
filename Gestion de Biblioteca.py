import tkinter as tk  
from tkinter import messagebox  
#construimos la clase libro y usuario para la gestion de la biblioteca
class Libro:
    def __init__(self, titulo, autor, disponible=True):  
        self.titulo = titulo  
        self.autor = autor  
        self.disponible = disponible  

    def __str__(self):  # Método para representar el objeto Libro como una cadena
        return f"{self.titulo} por {self.autor} - {'Disponible' if self.disponible else 'Prestado'}"

class Usuario:
    def __init__(self, nombre, id_usuario):  # Constructor de la clase Usuario
        self.nombre = nombre  # Inicializa el atributo nombre
        self.id_usuario = id_usuario  # Inicializa el atributo id_usuario
        self.libros_prestados = []  # Inicializa la lista de libros prestados

    def __str__(self):  # Método para representar el objeto Usuario como una cadena
        return f"{self.nombre} (ID: {self.id_usuario})"

class SistemaGestionBiblioteca:
    def __init__(self, root):  # Constructor de la clase SistemaGestionBiblioteca
        self.root = root  # Inicializa la ventana principal
        self.root.title("Biblioteca A&A")  # Establece el título de la ventana

        self.libros = self.cargar_libros_famosos()  # Carga la lista de libros famosos
        self.usuarios = self.cargar_usuarios_ejemplo()  # Carga la lista de usuarios de ejemplo

        self.crear_interfaz()  # Crea la interfaz gráfica

    def cargar_libros_famosos(self):  # Método para cargar libros famosos # ... (lista de libros)
        libros = [
            ("Cien años de soledad", "Gabriel García Márquez"),
            ("1984", "George Orwell"),
            ("El Señor de los Anillos", "J.R.R. Tolkien"),
            ("Orgullo y prejuicio", "Jane Austen"),
            ("Matar a un ruiseñor", "Harper Lee"),
            ("Don Quijote de la Mancha", "Miguel de Cervantes"),
            ("El Gran Gatsby", "F. Scott Fitzgerald"),
            ("En busca del tiempo perdido", "Marcel Proust"),
            ("Ulises", "James Joyce"),
            ("Moby Dick", "Herman Melville"),
            ("Hamlet", "William Shakespeare"),
            ("Crimen y castigo", "Fyodor Dostoevsky"),
            ("Madame Bovary", "Gustave Flaubert"),
            ("La Ilíada", "Homero"),
            ("La Odisea", "Homero"),
            ("La Divina Comedia", "Dante Alighieri"),
            ("Lolita", "Vladimir Nabokov"),
            ("Guerra y paz", "Leo Tolstoy"),
            ("Anna Karenina", "Leo Tolstoy"),
            ("Middlemarch", "George Eliot"),
            ("Las aventuras de Huckleberry Finn", "Mark Twain"),
            ("Grandes Esperanzas", "Charles Dickens"),
            ("Cumbres Borrascosas", "Emily Brontë"),
            ("El retrato de Dorian Gray", "Oscar Wilde"),
            ("Un mundo feliz", "Aldous Huxley"),
            ("El guardián entre el centeno", "J.D. Salinger"),
            ("El Principito", "Antoine de Saint-Exupéry"),
            ("El Hobbit", "J.R.R. Tolkien"),
            ("Las uvas de la ira", "John Steinbeck"),
            ("Pedro Páramo", "Juan Rulfo")
         
        ]
        return [Libro(titulo, autor) for titulo, autor in libros]  # Crea objetos Libro a partir de la lista

    def cargar_usuarios_ejemplo(self):  # Método para cargar usuarios de ejemplo # ... (lista de usuarios)
        usuarios = [
            ("Ana García", "12345"),
            ("Luis Martínez", "67890"),
            ("Luis Jimenez", "54321"),
            ("Sofía Rodríguez", "13579"),
            ("Carlos Pérez", "24680"),
            ("Laura Sánchez", "11223"),
            ("Diego López", "44556"),
            ("Isabel Torres", "77889"),
            ("Javier Ramírez", "99001"),
            ("Paula Díaz", "22334"),
            ("Miguel Castro", "55667"),
            ("Elena Ruiz", "88990"),
            ("Andrés Morales", "10101"),
            ("Carmen Gutiérrez", "21212"),
            ("Roberto Jiménez", "32323"),
            ("Silvia Álvarez", "43434"),
            ("David Romero", "54545"),
            ("Marta Navarro", "65656"),
            ("Sergio Alonso", "76767"),
            ("Raquel Herrera", "87878"),
            ("Jorge Serrano", "98989")
            
        ]
        return [Usuario(nombre, id_usuario) for nombre, id_usuario in usuarios]  # Crea objetos Usuario a partir de la lista

    def crear_interfaz(self):  # Método para crear la interfaz gráfica
        tk.Label(self.root, text="Biblioteca A&A", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=10)  # Título

        tk.Button(self.root, text="Agregar Libro", command=self.agregar_libro_dialog).grid(row=1, column=0, pady=5)  # Botón para agregar libro
        tk.Button(self.root, text="Agregar Usuario", command=self.agregar_usuario_dialog).grid(row=1, column=2, pady=5)  # Botón para agregar usuario
        tk.Button(self.root, text="Prestar Libro", command=self.prestar_libro_dialog).grid(row=2, column=0, pady=5)  # Botón para prestar libro
        tk.Button(self.root, text="Devolver Libro", command=self.devolver_libro_dialog).grid(row=2, column=2, pady=5)  # Botón para devolver libro
        tk.Button(self.root, text="Buscar Libro", command=self.buscar_libro_dialog).grid(row=3, column=0, pady=5)  # Botón para buscar libro
        tk.Button(self.root, text="Buscar Usuario", command=self.buscar_usuario_dialog).grid(row=3, column=2, pady=5)  # Botón para buscar usuario
        tk.Button(self.root, text="Mostrar Libros", command=self.mostrar_libros).grid(row=4, column=0, pady=5)  # Botón para mostrar libros
        tk.Button(self.root, text="Mostrar Usuarios", command=self.mostrar_usuarios).grid(row=4, column=2, pady=5)  # Botón para mostrar usuarios

    def agregar_libro_dialog(self):  # Método para mostrar el diálogo de agregar libro
        dialog = tk.Toplevel(self.root)
        dialog.title("Agregar Libro")

        tk.Label(dialog, text="Título:").grid(row=0, column=0)
        titulo_entry = tk.Entry(dialog)
        titulo_entry.grid(row=0, column=1)

        tk.Label(dialog, text="Autor:").grid(row=1, column=0)
        autor_entry = tk.Entry(dialog)
        autor_entry.grid(row=1, column=1)

        tk.Button(dialog, text="Agregar", command=lambda: self.agregar_libro(titulo_entry.get(), autor_entry.get(), dialog)).grid(row=2, column=0, columnspan=2)

    def agregar_libro(self, titulo, autor, dialog):  # Método para agregar un libro
        if titulo and autor:
            libro = Libro(titulo, autor)
            self.libros.append(libro)
            messagebox.showinfo("Éxito", "Libro agregado correctamente.")
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def agregar_usuario_dialog(self):  # Método para mostrar el diálogo de agregar usuario
        dialog = tk.Toplevel(self.root)
        dialog.title("Agregar Usuario")

        tk.Label(dialog, text="Nombre:").grid(row=0, column=0)
        nombre_entry = tk.Entry(dialog)
        nombre_entry.grid(row=0, column=1)

        tk.Label(dialog, text="ID Usuario:").grid(row=1, column=0)
        id_usuario_entry = tk.Entry(dialog)
        id_usuario_entry.grid(row=1, column=1)

        tk.Button(dialog, text="Agregar", command=lambda: self.agregar_usuario(nombre_entry.get(), id_usuario_entry.get(), dialog)).grid(row=2, column=0, columnspan=2)

    def agregar_usuario(self, nombre, id_usuario, dialog):  # Método para agregar un usuario
        if nombre and id_usuario:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios.append(usuario)
            messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
            dialog.destroy()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def prestar_libro_dialog(self):  # Método para mostrar el diálogo de prestar libro
        dialog = tk.Toplevel(self.root)
        dialog.title("Prestar Libro")

        tk.Label(dialog, text="Título del Libro:").grid(row=0, column=0)
        titulo_libro_entry = tk.Entry(dialog)
        titulo_libro_entry.grid(row=0, column=1)

        tk.Label(dialog, text="ID Usuario:").grid(row=1, column=0)
        id_usuario_entry = tk.Entry(dialog)
        id_usuario_entry.grid(row=1, column=1)

        tk.Button(dialog, text="Prestar", command=lambda: self.prestar_libro(titulo_libro_entry.get(), id_usuario_entry.get(), dialog)).grid(row=2, column=0, columnspan=2)

    def prestar_libro(self, titulo_libro, id_usuario, dialog):  # Método para prestar un libro
        libro = next((libro for libro in self.libros if libro.titulo.lower() == titulo_libro.lower()), None)  # Busca el libro (ignora mayúsculas/minúsculas)
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)  # Busca el usuario

        if libro and usuario:
            if libro.disponible:
                libro.disponible = False
                usuario.libros_prestados.append(libro)
                messagebox.showinfo("Éxito", f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
                dialog.destroy()
            else:
                messagebox.showerror("Error", "El libro no está disponible.")
        else:
            messagebox.showerror("Error", "Libro o usuario no encontrado.")

    def devolver_libro_dialog(self):  # Método para mostrar el diálogo de devolver libro
        dialog = tk.Toplevel(self.root)
        dialog.title("Devolver Libro")

        tk.Label(dialog, text="Título del Libro:").grid(row=0, column=0)
        titulo_libro_entry = tk.Entry(dialog)
        titulo_libro_entry.grid(row=0, column=1)

        tk.Label(dialog, text="ID Usuario:").grid(row=1, column=0)
        id_usuario_entry = tk.Entry(dialog)
        id_usuario_entry.grid(row=1, column=1)

        tk.Button(dialog, text="Devolver", command=lambda: self.devolver_libro(titulo_libro_entry.get(), id_usuario_entry.get(), dialog)).grid(row=2, column=0, columnspan=2)

    def devolver_libro(self, titulo_libro, id_usuario, dialog):  # Método para devolver un libro
        libro = next((libro for libro in self.libros if libro.titulo.lower() == titulo_libro), None) # Busca el libro (ignora mayúsculas/minúsculas)
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None) # Busca el usuario

        if libro and usuario:
            if libro in usuario.libros_prestados:
                libro.disponible = True
                usuario.libros_prestados.remove(libro)
                messagebox.showinfo("Éxito", f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                dialog.destroy()
            else:
                messagebox.showerror("Error", "El usuario no tiene este libro prestado.")
        else:
            messagebox.showerror("Error", "Libro o usuario no encontrado.")

    def buscar_libro_dialog(self):  # Método para mostrar el diálogo de buscar libro
        dialog = tk.Toplevel(self.root)
        dialog.title("Buscar Libro")

        tk.Label(dialog, text="Título:").grid(row=0, column=0)
        titulo_entry = tk.Entry(dialog)
        titulo_entry.grid(row=0, column=1)

        tk.Button(dialog, text="Buscar", command=lambda: self.buscar_libro(titulo_entry.get(), dialog)).grid(row=1, column=0, columnspan=2)

    def buscar_libro(self, titulo, dialog):  # Método para buscar un libro
        resultados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]  # Busca libros que coincidan (ignora mayúsculas/minúsculas)
        if resultados:
            mensaje = "\n".join(str(libro) for libro in resultados)
            messagebox.showinfo("Libros Encontrados", mensaje)
        else:
            messagebox.showerror("Error", "Libro no encontrado.")
        dialog.destroy()

    def buscar_usuario_dialog(self):  # Método para mostrar el diálogo de buscar usuario
        dialog = tk.Toplevel(self.root)
        dialog.title("Buscar Usuario")

        tk.Label(dialog, text="Nombre:").grid(row=0, column=0)
        nombre_entry = tk.Entry(dialog)
        nombre_entry.grid(row=0, column=1)

        tk.Button(dialog, text="Buscar", command=lambda: self.buscar_usuario(nombre_entry.get(), dialog)).grid(row=1, column=0, columnspan=2)

    def buscar_usuario(self, nombre, dialog):  # Método para buscar un usuario
        resultados = [usuario for usuario in self.usuarios if nombre.lower() in usuario.nombre.lower()]  # Busca usuarios que coincidan (ignora mayúsculas/minúsculas)
        if resultados:
            mensaje = "\n".join(str(usuario) for usuario in resultados)
            messagebox.showinfo("Usuarios Encontrados", mensaje)
        else:
            messagebox.showerror("Error", "Usuario no encontrado.")
        dialog.destroy()

    def mostrar_libros(self):  # Método para mostrar la lista de libros
        if self.libros:
            libros_str = "\n".join(str(libro) for libro in self.libros)
            messagebox.showinfo("Lista de Libros", libros_str)
        else:
            messagebox.showinfo("Lista de Libros", "No hay libros registrados.")

    def mostrar_usuarios(self):  # Método para mostrar la lista de usuarios
        if self.usuarios:
            usuarios_str = "\n".join(str(usuario) for usuario in self.usuarios)
            messagebox.showinfo("Lista de Usuarios", usuarios_str)
        else:
            messagebox.showinfo("Lista de Usuarios", "No hay usuarios registrados.")

if __name__ == "__main__":  # Punto de entrada del programa
    root = tk.Tk()  # Crea la ventana principal
    app = SistemaGestionBiblioteca(root)  # Crea una instancia de la clase SistemaGestionBiblioteca
    root.mainloop()  # Inicia el bucle principal de la aplicación tkinter
