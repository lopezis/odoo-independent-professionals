# Datebook - Sistema de Citas en Línea

Datebook es un módulo para Odoo 18 Community que permite a tus clientes reservar citas en línea a través de tu sitio web, de manera similar a Calendly.

## Características

- **Reserva en línea**: Los clientes pueden seleccionar un tipo de cita, fecha y hora disponibles.
- **Generación automática de horarios**: El sistema crea automáticamente los huecos disponibles según las reglas de disponibilidad.
- **Múltiples empleados**: Cada miembro del equipo puede tener sus propios horarios.
- **Zonas horarias**: Soporte completo para zonas horarias del cliente y del empleado.
- **Previene doble reserva**: Un mismo horario no puede ser reservado dos veces.
- **Tiempo debuffer**: Tiempo de preparación entre citas.
- **Aviso mínimo**: Solo permite reservas con cierta anticipación.
- **Cancelación con token**: Los clientes pueden cancelar usando un enlace seguro.
- **Reprogramación con token**: Los clientes pueden cambiar su cita.
- **Notificaciones por correo**: Confirmación, cancelación, recordatorios (24h y 1h antes).
- **Integración con Calendario**: Crea eventos en el calendario de Odoo.
- **Integración con CRM**: Crea automáticamente prospectos en CRM.

## Instalación

1. Ve a **Aplicaciones**.
2. Busca "Datebook" e instálalo.
3. El módulo se encuentra en **Productividad > Datebook**.

## Configuración

### 1. Crear Empleados (Staff)

1. Ve a **Datebook > Configuración > Staff**.
2. Crea un nuevo empleado:
   - **Usuario**: Selecciona el usuario de Odoo.
   - **Zona horaria**: Selecciona la zona horaria del empleado.
   - **Tipos de cita**: Selecciona los tipos de cita que puede atender.
3. Guarda.

### 2. Configurar Disponibilidad

1. En el empleado creado, ve a la pestaña **Disponibilidad**.
2. Agrega reglas para cada día de trabajo:
   - **Día**: Monday, Tuesday, etc.
   - **Hora inicio**: Ejemplo 9.0 para 09:00, 9.5 para 09:30.
   - **Hora fin**: Ejemplo 17.0 para 17:00.
3. Guarda las reglas.

### 3. Crear Tipos de Cita

1. Ve a **Datebook > Configuración > Tipos de Cita**.
2. Crea un nuevo tipo:
   - **Nombre**: Ejemplo "Consulta inicial".
   - **Slug**: Ejemplo "consulta-inicial" (URL amigable).
   - **Descripción**: Descripción que verán los clientes.
   - **Duración**: Duración en minutos (ej. 30).
   - **Buffer antes**: Minutos de preparación antes de la cita.
   - **Buffer después**: Minutos de preparación después de la cita.
   - **Aviso mínimo (horas)**: Mínimo de horas de anticipación para reservar.
   - **Días máximos**: Cuántos días adelante se puede reservar.
   - **Staff asignado**: Selecciona los empleados que ofrecen este tipo de cita.
3. Guarda.

### 4. Generar Horarios

Los horarios se generan automáticamente mediante una tarea programada (cron), pero también puedes generarlos manualmente:

1. Ve a **Datebook > Slots**.
2. Los horarios disponibles aparecerán automáticamente.

## Uso para el Cliente

### Reservar una Cita

1. Visita la URL: `/book/[slug]` donde [slug] es el slug del tipo de cita.
   - Ejemplo: `https://tu-sitio.com/book/consulta-inicial`
2. Selecciona una fecha en el calendario.
3. Elige un horario disponible.
4. Completa el formulario:
   - Nombre
   - Correo electrónico
   - Teléfono (opcional)
   - Notas (opcional)
5. Haz clic en "Confirmar Reserva".
6. Recibirás un correo de confirmación.

### Cancelar una Cita

1. Busca el correo de confirmación que recibiste.
2. Haz clic en el enlace de cancelación proporcionado.
3. Tu cita será cancelada y recibirás confirmación por correo.

### Reprogramar una Cita

1. Busca el correo de confirmación.
2. Haz clic en el enlace de reprogramación.
3. Selecciona una nueva fecha y horario disponible.
4. Tu cita será actualizada.

## Uso en el Backend

### Ver Citas

1. Ve a **Datebook > Citas**.
2. Aquí verás todas las citas con su estado (Pendiente, Confirmada, Cancelada, Completada).
3. Puedes filtrar por estado, empleado, tipo de cita, etc.

### Panel de Control (Dashboard)

1. Ve a **Datebook > Panel de Control**.
2. Verás gráficos y estadísticas de citas:
   - Citas por tipo
   - Citas por empleado
   - Citas de hoy
   - Vista Kanban de citas

### Integración con Calendario

Cada cita confirmada crea un evento en el calendario de Odoo con el empleado asignado como asistente.

### Integración con CRM

Cada cita confirmada crea un prospecto (lead) en CRM con los datos del cliente.

## Tareas Programadas (Cron Jobs)

El módulo incluye automáticamente:

- **Generar horarios**: Crea los horarios disponibles cada día.
- **Recordatorio 24h**: Envía recordatorio 24 horas antes de la cita.
- **Recordatorio 1h**: Envía recordatorio 1 hora antes de la cita.

## Personalización

### Correos Electrónicos

Los correos se pueden modificar en:
- **Configuración > Correo > Plantillas**
- Busca las plantillas que empiezan con "Datebook".

### Estilos

Los estilos CSS están en: `static/src/css/booking.css`
El JavaScript está en: `static/src/js/booking.js`

## Solución de Problemas

### No aparecen horarios disponibles

1. Verifica que el empleado tenga reglas de disponibilidad configuradas.
2. Verifica que el tipo de cita tenga empleados asignados.
3. Ejecuta la tarea de generación de horarios manualmente.

### Error al reservar

1. Verifica que el horario aún esté disponible.
2. Verifica que el tiempo de anticipación sea mayor al aviso mínimo configurado.

### No se envían correos

1. Verifica que el servidor de correo esté configurado en Odoo.
2. Verifica que las plantillas de correo estén activas.

## Licencia

Este módulo está bajo licencia LGPL-3.
