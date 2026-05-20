#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "DYLAN ALFONSO PLATA MANJARRES"
edad = 14
estatura = 1.80
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("dylanmanjarres_777", "DYLAN_777")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "DANCIN", "artista": "AARON SMITH", "duracion": "4:04"},
{"titulo": "POR AMAR A CIEGAS", "artista": "ARCANGEL", "duracion": "4:36"},
{"titulo": "ME PREFIERES A MI", "artista": "ARCANGEL", "duracion": "3:17"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")
