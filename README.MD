# M5 Apps
## Why
Simply because I can. I ordered the [M5 Atom Matrix](https://www.adafruit.com/product/4497), courtesy of Adafruit, and I wanted to learn about MicroPython, so here we are. I have no goals for this repo, aside from compiling all the little garbage apps, that I make for this device, in one convenient place.

This project uses poetry to manage the development tools needed. You can find [the poetry installation guide here](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions).

## Resources
### Documentation
- https://docs.micropython.org/en/latest/esp32/quickref.html
- https://docs.m5stack.com/en/core/atom_matrix
- https://github.com/peterhinch/micropython-async/blob/master/v3/docs/TUTORIAL.md
- https://python-poetry.org/

---

### Pin Map:
| Element | Pin |
| --- | --- |
| RGB Led	| G27 |
| Button	| G39 |
| IR	| G12 |
| SCL	| G21 |
| SDA	| G25 |

### Schematic:
![image](https://static-cdn.m5stack.com/resource/docs/static/assets/img/product_pics/core/minicore/atom/ATOM_MATRIX_SIMPLE_CIRCUT_20200514.webp)

###### Pin map and schematic info provided by: [docs.m5stack.com](https://docs.m5stack.com/en/core/atom_matrix)