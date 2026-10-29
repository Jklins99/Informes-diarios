# Informe diario fotográfico

App web (un solo archivo, `index.html`) para armar el reporte diario de actividades:
tabla de avances + fotos, con descarga en **Excel**, **Word** y un **ZIP mensual** con carpetas por fecha.

- No usa servidor ni base de datos: todo se guarda en el navegador del dispositivo (IndexedDB).
- Nada se sube a internet. Cada persona ve solo su propia información.

## Publicarla en GitHub Pages (gratis)

1. Crea una cuenta en https://github.com (si no tienes).
2. Pulsa **New repository**. Nómbralo, por ejemplo, `informe-diario`. Déjalo **Public** y crea el repositorio.
3. Pulsa **Add file → Upload files**, sube `index.html` y pulsa **Commit changes**.
4. Ve a **Settings → Pages**. En *Build and deployment* elige **Deploy from a branch**, rama **main**, carpeta **/ (root)** y pulsa **Save**.
5. Espera 1–2 minutos. Tu app quedará en:
   `https://TU-USUARIO.github.io/informe-diario/`

Comparte ese enlace con tus compañeros. Cada uno debe abrirlo desde su teléfono.

## Instalarla como app en el teléfono

- **iPhone (Safari):** Compartir → *Agregar a pantalla de inicio*.
- **Android (Chrome):** menú ⋮ → *Agregar a la pantalla principal*.

## Importante

- Las fotos quedan en el dispositivo; si se borran los datos del navegador, se pierden. Descarga el ZIP del mes con frecuencia.
- El repositorio público solo muestra el código, nunca las fotos ni los reportes.
- La app carga la librería JSZip desde cdnjs.cloudflare.com, así que necesita internet la primera vez que se abre.
