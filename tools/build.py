#!/usr/bin/env python3
"""Genera index.html (archivo único) a partir de src/nightfall.html.
Incrusta GLTFLoader (vendor/) y los modelos .glb (assets/) en base64.
Uso: python3 tools/build.py"""
import base64, glob, os, json, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(root, 'src', 'nightfall.html'), encoding='utf8').read()
loader = open(os.path.join(root, 'vendor', 'GLTFLoader.js'), encoding='utf8').read().replace('</script>', '<\\/script>')
data = {}
for f in sorted(glob.glob(os.path.join(root, 'assets', '*.glb'))):
    key = os.path.splitext(os.path.basename(f))[0]
    data[key] = base64.b64encode(open(f, 'rb').read()).decode('ascii')
block = ('<script>/* GLTFLoader (three.js r128, MIT) */\nif (window.THREE) {\n' + loader + '\n}</script>\n'
         '<script>/* Modelos KayKit (CC0) embebidos */\nwindow.NF_GLB = ' + json.dumps(data) + ';</script>')
assert '<!--NF_ASSETS-->' in src, 'falta el marcador <!--NF_ASSETS-->'
out = src.replace('<!--NF_ASSETS-->', block)
open(os.path.join(root, 'index.html'), 'w', encoding='utf8').write(out)
print('index.html', round(len(out) / 1e6, 2), 'MB,', len(data), 'modelos')

# Versión ligera (sin modelos 3D, héroe procedural): python3 tools/build.py --lite
if '--lite' in sys.argv:
    lite = src.replace('<!--NF_ASSETS-->', '')
    open(os.path.join(root, 'index_lite.html'), 'w', encoding='utf8').write(lite)
    print('index_lite.html', round(len(lite) / 1e6, 2), 'MB')
