class Empleado:
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, supervisor=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Apellidos:", self.apellidos)
        print("DNI:", self.dni)
        print("Dirección:", self.direccion)
        print("Teléfono:", self.telefono)
        print("Salario:", self.salario)
        if self.supervisor:
            print("Supervisor:", self.supervisor.nombre)

    def cambiar_supervisor(self, nuevo_supervisor):
        self.supervisor = nuevo_supervisor

    def incrementar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)


class Secretario(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho, fax):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.despacho = despacho
        self.fax = fax

    def imprimir(self):
        super().imprimir()
        print("Puesto: Secretario")
        print("Despacho:", self.despacho)
        print("Fax:", self.fax)

    def incrementar_salario(self, porcentaje=5):
        super().incrementar_salario(porcentaje)


class Vendedor(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, coche, telefono_movil, area_venta, comision):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.coche = coche
        self.telefono_movil = telefono_movil
        self.area_venta = area_venta
        self.clientes = []
        self.comision = comision

    def imprimir(self):
        super().imprimir()
        print("Puesto: Vendedor")
        print("Coche:", self.coche)
        print("Teléfono Móvil:", self.telefono_movil)
        print("Área de Venta:", self.area_venta)
        print("Comisión:", self.comision)

    def dar_alta_cliente(self, cliente):
        self.clientes.append(cliente)

    def dar_baja_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)
        else:
            print("Cliente no encontrado en la lista.")

    def cambiar_coche(self, coche):
        self.coche = coche

    def incrementar_salario(self, porcentaje=10):
        super().incrementar_salario(porcentaje)


class JefeZona(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho, secretario, coche, vendedores):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.despacho = despacho
        self.secretario = secretario
        self.coche = coche
        self.vendedores = vendedores

    def imprimir(self):
        super().imprimir()
        print("Puesto: Jefe de Zona")
        print("Despacho:", self.despacho)
        print("Secretario:", self.secretario.nombre)
        print("Coche:", self.coche)
        print("Vendedores a cargo:")
        for vendedor in self.vendedores:
            print("- ", vendedor.nombre)

    def cambiar_secretario(self, nuevo_secretario):
        self.secretario = nuevo_secretario

    def cambiar_coche(self, coche):
        self.coche = coche

    def dar_alta_vendedor(self, vendedor):
        self.vendedores.append(vendedor)

    def dar_baja_vendedor(self, vendedor):
        if vendedor in self.vendedores:
            self.vendedores.remove(vendedor)
        else:
            print("Vendedor no encontrado en la lista.")

    def incrementar_salario(self, porcentaje=20):
        super().incrementar_salario(porcentaje)


secretario1 = Secretario("Juan", "González", "12345678A", "Calle Mayor 10", "123456789", 1500, "Despacho 1", "12345")
vendedor1 = Vendedor("Pedro", "López", "87654321B", "Calle Menor 5", "987654321", 2000, "ABC123", "666777888", "Zona Norte", 0.05)
vendedor2 = Vendedor("Maria", "Martinez", "13579246C", "Calle Pequeña 3", "987654322", 2000, "DEF456", "666777999", "Zona Sur", 0.05)
jefe_zona1 = JefeZona("Antonio", "Perez", "98765432D", "Calle Grande 15", "987654320", 3000, "Despacho 2", secretario1, "XYZ789", [vendedor1, vendedor2])

print("--- Empleados ---")
secretario1.imprimir()
print()
vendedor1.imprimir()
print()
vendedor2.imprimir()
print()
jefe_zona1.imprimir()
print()

print("--- Incremento de Salarios ---")
secretario1.incrementar_salario()
vendedor1.incrementar_salario()
vendedor2.incrementar_salario()
jefe_zona1.incrementar_salario()

print("--- Empleados con Salarios Actualizados ---")
secretario1.imprimir()
print()
vendedor1.imprimir()
print()
vendedor2.imprimir()
print()
jefe_zona1.imprimir()
