# Odoo Freelancer Suite

Colección curada de módulos para **Odoo Community Edition** orientada a **profesionales independientes, freelancers y pequeños negocios unipersonales**.

Este repositorio reúne **módulos personalizados y módulos seleccionados de OCA (Odoo Community Association)** con el objetivo de adaptar Odoo Community a las necesidades reales del trabajo profesional independiente.

La meta es construir un **entorno ligero, modular y práctico** que permita gestionar clientes, citas, servicios, comunicación y presencia profesional desde un solo sistema.

---

# Objetivo del proyecto

Odoo Community es un ERP extremadamente potente, pero muchas de las herramientas que resultan especialmente útiles para **freelancers o profesionales independientes** requieren módulos adicionales o personalizaciones.

Este proyecto busca:

* Adaptar **Odoo Community** al trabajo de profesionales independientes
* Reunir **módulos OCA esenciales**
* Desarrollar **módulos personalizados enfocados en freelancers**
* Proporcionar una **base lista para desplegar**

Casos de uso típicos:

* Consultores
* Desarrolladores
* Diseñadores
* Coaches
* Psicólogos / terapeutas
* Profesionales de marketing
* Profesionales de servicios

---

# Funcionalidades principales

El entorno propuesto busca cubrir las necesidades más comunes de un profesional independiente:

### Gestión de clientes

* CRM simplificado
* Historial de interacciones
* Seguimiento de oportunidades

### Gestión de citas

Sistema de reservas para clientes que permita:

* Reservar citas
* Integración con calendario
* Gestión de disponibilidad

### Hub de enlaces profesional

Un módulo similar a **Linktree** para crear una página con:

* Información de contacto
* Enlaces profesionales
* Enlaces de reserva de citas
* Redes sociales

### Gestión de servicios

* Catálogo de servicios
* Presupuestos
* Facturación

### Automatización básica

* Recordatorios
* Confirmaciones de cita
* Correos automáticos

---

# Módulos personalizados

Los módulos desarrollados específicamente para este repositorio estarán ubicados en:

```
custom_addons/
```

Ejemplos de módulos planeados:

### freelancer_link_hub

Página pública estilo **Linktree** que permite:

* Mostrar información profesional
* Enlaces de contacto
* Enlaces de reserva
* Redes sociales
* Servicios

### datebook

Sistema de citas optimizado para profesionales independientes.

Funcionalidades previstas:

* Calendario de disponibilidad
* Reserva por clientes
* Integración con CRM
* Confirmaciones automáticas

---

# Módulos OCA recomendados para freelancers

Este proyecto también incluye módulos del ecosistema **OCA** considerados especialmente útiles para profesionales independientes.

Repositorio oficial de OCA:

https://github.com/OCA

### CRM

Repositorios OCA recomendados:

* OCA/crm
* OCA/sale-workflow

Utilidad:

* Gestión de clientes
* Seguimiento de oportunidades
* Conversión a ventas

---

### Calendario y citas

Repositorios OCA recomendados:

* OCA/calendar
* OCA/server-tools

Utilidad:

* Mejoras en calendario
* Automatizaciones
* recordatorios

---

### Facturación y contabilidad

Repositorios OCA recomendados:

* OCA/account-financial-tools
* OCA/account-invoicing

Utilidad:

* Facturación profesional
* Automatización contable
* mejoras en reportes

---

### Productividad

Repositorios OCA recomendados:

* OCA/server-tools
* OCA/web

Utilidad:

* mejoras de interfaz
* herramientas administrativas
* optimización de flujo de trabajo

---

### Comunicación

Repositorios OCA recomendados:

* OCA/social
* OCA/mail

Utilidad:

* integraciones de comunicación
* mejoras en correo
* gestión de interacciones

---

# Estructura del repositorio

Este repositorio sigue una estructura inspirada en los proyectos de **OCA** para facilitar mantenimiento y contribuciones.

```
odoo-freelancer-suite/

addons/
│
├── custom_addons/
│   ├── freelancer_link_hub
│   ├── freelancer_appointments
│
├── oca_addons/
│   ├── crm_extensions
│   ├── calendar_extensions
│   ├── productivity_tools
│
docs/
│
scripts/
│
tests/
│
README.md
LICENSE
```

### Descripción de carpetas

**addons/**
Directorio principal de módulos.

**custom_addons/**
Módulos desarrollados específicamente para este proyecto.

**oca_addons/**
Módulos provenientes de repositorios OCA.

**docs/**
Documentación del proyecto.

**scripts/**
Scripts de instalación, setup o utilidades.

**tests/**
Pruebas automáticas para los módulos.

---

# Instalación

Clonar el repositorio:

```
git clone https://github.com/tuusuario/odoo-freelancer-suite.git
```

Agregar los addons al `addons_path` de Odoo:

```
addons_path = /odoo/addons,/ruta/odoo-freelancer-suite/addons
```

Actualizar la lista de aplicaciones desde Odoo y proceder a instalar los módulos necesarios.

---

# Compatibilidad

Este proyecto está diseñado para:

* **Odoo Community Edition**

La compatibilidad exacta dependerá de la rama del repositorio.

Ejemplo:
* `17.0`
* `18.0`

---

# Contribuciones

Las contribuciones son bienvenidas.

Puedes colaborar mediante:

* Nuevos módulos orientados a freelancers
* Mejora de módulos existentes
* Integración de módulos OCA relevantes
* Reporte de bugs
* Propuestas de mejoras

---

# Licencia

Cada módulo mantiene su licencia original.

Generalmente:

* **Módulos personalizados:** LGPL-3
* **Módulos OCA:** licencia definida en su repositorio original

---

# Filosofía del proyecto

Los profesionales independientes necesitan herramientas potentes sin la complejidad de sistemas empresariales.

La combinación de **Odoo Community + OCA + módulos especializados** permite construir un entorno profesional completo para gestionar un negocio independiente desde una sola plataforma.
