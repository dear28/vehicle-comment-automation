COMMENT_TEMPLATES = {
    "1": "Cliente no contesta, se pospone el correo",

    "2": "Cliente solicita ser contactado más tarde",

    "3": "Cliente no brinda disponibilidad",

    "4": "Se regresa solicitud al asesor por falta de información",
    
    "5": (
            "Programación: Contacto: {client} "
            "- Teléfono: {phone} "
            "- Dirección: {address} "
            "- Técnico: {technician} "
            "- Fecha: {date_comment} "
            "- Programador: {programmer}"
    ),

    "6": (
            "No se logra prestar el servicio por: {reason} "
            "- Fallos {total_failed}"
    ),

    "7": (
            "Se programan: {total_vehicles} "
            "vehículos - Se logran ejecutar {total_vehicles_ok} "
            "- Quedan pendientes por reprogramar {total_pending_vehicles} vehículos"
    ),

    "8": (
            "Cliente {client} "
            "- Teléfono {phone}, "
            "con {total_vehicles} vehículos, "
            "indica que va a brindar disponibilidad de {vehicles_per_day} "
            "vehículos por día, iniciando desde el día {date_comment}, "
            "en la dirección {address}, "
            "a la hora {hour_comment}, con el técnico disponible"
    ),

    "9": (
            "Cliente {client} "
            "se atiende por WhatsApp - Pendiente por brindar disponibilidad - "
            "Placas {total_vehicles}"
    ),

    "10": (
            "Cliente COMPANY EXAMPLE coordina sus propias instalaciones. Se envia al técnico {technician} "
            "por 28 días iniciando desde el día {date_comment}"
    ),

    "11": (
            "Se envian {total_units} "
            "unidades al cliente COMPANY EXAMPLE y el cliente coordina sus propias instalaciones con sus propios técnicos"
    )
}


# Create comment from template
def generate_comment(id_comment, data=None):
    data = data or {}

    template = COMMENT_TEMPLATES.get(id_comment)

    if not template:
        return "Invalid comment option"

    return template.format_map(data)