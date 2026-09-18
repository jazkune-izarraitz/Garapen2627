# Ikasle Kudeaketa

Aplicación web completa para gestionar alumnos (Ikasleak) con PHP 8, MySQL y Bootstrap.

## 1. Preparar el entorno XAMPP
1. Descarga XAMPP desde https://www.apachefriends.org e instálalo con los módulos Apache y MySQL.
2. Abre el panel de control de XAMPP y pulsa **Start** en Apache y MySQL. Comprueba que ambos servicios están en verde.

## 2. Crear la base de datos
1. Abre http://localhost/phpmyadmin.
2. Pulsa en la pestaña **SQL** y pega el script completo mostrado abajo. Si lo prefieres, el archivo `ikasleak_db.sql` ya está incluido para importarlo desde *Importar*.

```sql
CREATE DATABASE IF NOT EXISTS ikasleak_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE ikasleak_db;

CREATE TABLE ikasleak (
    id INT AUTO_INCREMENT PRIMARY KEY,
    izena VARCHAR(100) NOT NULL,
    abizena VARCHAR(100) NOT NULL,
    zikloa VARCHAR(100) NOT NULL,
    maila VARCHAR(50) NOT NULL,
    argazkia VARCHAR(255) DEFAULT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## 3. Copiar el proyecto
1. Copia la carpeta completa de este repositorio dentro de `C:\xampp\htdocs\` y renómbrala como `ikasleak`.
2. La ruta final debe quedar `C:\xampp\htdocs\ikasleak`.

## 4. Configurar conexión
- Los valores por defecto (`usuario=root`, sin contraseña) están definidos en `config/db.php`. Modifícalos si tu instancia de MySQL utiliza otras credenciales.

## 5. Acceder a la aplicación
- Si copiaste el contenido directamente dentro de `C:\xampp\htdocs\`, entra a `http://localhost` y serás redirigido automáticamente al panel.
- Si mantienes la carpeta del proyecto (por ejemplo `kontrol_puntua`), accede a `http://localhost/kontrol_puntua` y se abrirá el panel.

## 6. Cambiar el idioma
- En la barra superior hay un selector (EU/EN). Cambia el idioma y la preferencia se guarda en la sesión.

## 7. Módulos disponibles
- **Listado principal:** búsqueda por nombre, ordenación por izena/zikloa/maila, miniaturas de las fotos y paginación de 10 registros por página para listados largos.
- **Alta de alumno:** formulario con validación cliente/servidor, token CSRF y subida segura (MIME real, límite de 2MB) al directorio `public/uploads`.
- **Edición:** precarga los datos y permite reemplazar la foto manteniendo la existente si no se adjunta una nueva.
- **Detalle:** ficha individual del estudiante.
- **Eliminación:** confirmación antes de borrar y limpieza automática de la foto almacenada.
- **Logs:** cada acción relevante (login automático, búsqueda, inserción, actualización, eliminación) genera una línea en `logs/app.log`. Desde la barra superior puedes abrir el visor de logs para verlos en una tabla elegante.

## 8. Seguridad integrada
- Conexión PDO y consultas preparadas (`models/Ikasle.php`).
- Escape de salida con `htmlspecialchars` en todas las vistas.
- Validación en servidor para campos obligatorios + validación rápida en cliente.
- Token CSRF generado en sesión y validado en cada POST.
- Subidas sanitizadas con `finfo`, lista blanca de MIME y renombrado único `time()_nombre.ext`.

Una vez copiado el proyecto y creada la base de datos, la aplicación está lista para usarse en XAMPP sin pasos adicionales. ¡Disfruta gestionando tus alumnos!
