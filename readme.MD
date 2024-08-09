- Pegar un webhook de navision en el archivo `webhook.json`
- Ejecutar `filter.py`
- Ejecutar `main.py` y pegar el MD de uno de los archivos generados
- Enjoy

Ejemplo de los dos inputs necesarios:

```
wardrobe_json = {
    0: {"width": 700, "height": 2000},
    1: {"width": 600, "height": 2000},
    2: {"width": 1400, "height": 2000},
    3: {"width": 500, "height": 2000},
    4: {"width": 500, "height": 2000}
}

components_json = {
    0: {"body": 0, "component": "shelf", "height": 800},
    1: {"body": 0, "component": "shelf", "height": 1200},
    2: {"body": 1, "component": "shelf", "height": 1300},
    3: {"body": 2, "component": "shelf", "height": 400},
    4: {"body": 2, "component": "shelf", "height": 600},
    5: {"body": 3, "component": "shelf", "height": 1600},
    6: {"body": 4, "component": "shelf", "height": 1600},
    7: {"body": 4, "component": "shelf", "height": 1400},
    8: {"body": 4, "component": "shelf", "height": 1200},
    9: {"body": 4, "component": "shelf", "height": 1000},
}
````

Model variants:

WARDROBE_SHELF_REGULAR
WARDROBE_SHELF_EXTENDABLE
WARDROBE_SHELF_HANGING_BAR
WARDROBE_SHOE_SHELF_EXTENDABLE
WARDROBE_SHOE_SHELF_INCLINED
WARDROBE_DRAWER_SINGLE
WARDROBE_DRAWER_DOUBLE
WARDROBE_DRAWER_TRIPLE
WARDROBE_DRAWER_QUADRUPLE
WARDROBE_DRAWER_SUSPENDED_SINGLE
WARDROBE_DRAWER_SUSPENDED_DOUBLE
WARDROBE_DRAWER_SUSPENDED_TRIPLE
WARDROBE_DRAWER_DOUBLE_PLUS
WARDROBE_DRAWER_SUSPENDED_DOUBLE_PLUS
WARDROBE_DRAWER_TRIPLE_PLUS