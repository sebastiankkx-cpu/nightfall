# NIGHTFALL

RPG 3D oscuro en un solo HTML (Three.js r128). Abre `index.html` en el navegador.

## Estructura
- `src/nightfall.html`: código fuente del juego (editar aquí).
- `assets/`: modelos .glb (KayKit Adventurers, CC0) con animaciones recortadas.
- `vendor/GLTFLoader.js`: cargador de three.js r128 (MIT).
- `tools/build.py`: genera `index.html` (archivo único) incrustando loader y modelos.

Tras editar `src/nightfall.html`: `python3 tools/build.py`.
