# ✦ Tienda en las Nubes - E-commerce MVP

Este es un proyecto de Portafolio desarrollado con **Django**. Consiste en un MVP (Minimum Viable Product) de un e-commerce que incluye un catálogo dinámico, persistencia de datos y un sistema de carrito de compras basado en sesiones.

## Características Principales
* **Catálogo de Productos:** Visualización de productos renderizados desde la base de datos (ORM).
* **Carrito de Compras:** Lógica de sesiones para agregar productos, sumar cantidades y simular la confirmación de la compra.
* **Panel de Administración:** Acceso seguro para gestionar (CRUD) el inventario de la tienda.
* **Diseño UI:** Maquetación responsiva utilizando Bootstrap 5 y plantillas heredadas (MVT).

## Requisitos Previos
* Python 3.x instalado en el sistema.

## Instrucciones de Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd Portafolio_Ecommerce

   # ✦ Portal Multidimensional Teo - E-Commerce

Plataforma de comercio electrónico orientada a la exhibición y gestión de assets, blueprints y diseño de personajes 3D. Desarrollado con Django, implementa un flujo completo de carrito de compras, gestión de inventario y una arquitectura visual personalizada (Estilo Teo 1.5).

**🔗 Enlace al repositorio público:** https://github.com/stlsisergio-ctrl/Portafolio_Ecommerce_Django

---

## ⚙️ Requisitos e Instalación

Para levantar este entorno en una máquina local, asegúrate de tener instalado **Python 3.x**.

**1. Clonar el repositorio:**
\`\`\`bash
git clone https://github.com/stlsisergio-ctrl/Portafolio_Ecommerce_Django.git
cd Portafolio_Ecommerce_Django
\`\`\`

**2. Crear y activar el entorno virtual:**
* En Windows:
\`\`\`bash
python -m venv venv
venv\Scripts\activate
\`\`\`
* En macOS/Linux:
\`\`\`bash
python3 -m venv venv
source venv/bin/activate
\`\`\`

**3. Instalar las dependencias:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## 🚀 Cómo ejecutar en local

Una vez configurado el entorno virtual y las dependencias, inicializa la base de datos y levanta el servidor:

**1. Aplicar las migraciones (Base de datos):**
\`\`\`bash
python manage.py makemigrations
python manage.py migrate
\`\`\`

**2. Iniciar el servidor de desarrollo:**
\`\`\`bash
python manage.py runserver
\`\`\`
El portal estará disponible en: `http://127.0.0.1:8000/`

---

## 🗺️ Rutas Principales del Sistema

El proyecto está estructurado con las siguientes rutas de navegación clave:

* **Públicas / Cliente:**
  * `/` : Home / Portal interactivo principal.
  * `/catalogo/` : Galería de inventario y assets 3D disponibles.
  * `/carrito/` : Gestión del carrito de compras (agregar, eliminar, totales).
  * `/login/` : Autenticación de usuarios.
  
* **Administración:**
  * `/admin/` : Panel de control nativo de Django para gestión de base de datos (ABM de Productos, Usuarios y Órdenes).

---

## 🔐 Credenciales de Prueba

Para la revisión del flujo completo del MVP, puedes utilizar los siguientes usuarios preconfigurados:

**Administrador (Gestión de catálogo y sistema):**
* **Usuario:** `admin`
* **Contraseña:** `admin`

**Cliente (Prueba de flujo de carrito y compra):**
* **Usuario:** `cliente_test`
* **Contraseña:** `cliente1234`

---
*Desarrollado para la entrega final del Bootcamp.*