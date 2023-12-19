# Растворение минеральной фазы при закачке CO2

## Структура Репозитория
- `CMakeLists.txt` - файл для сборки проекта с помощью CMake.
- `data/` - изображения сеток.
- `include/` - заголовочные файлы.
- `scripts/` - Python скрипты и данные + решалка ЛУ.
- `src/` - исходный код на C++.

## Запуск
### Скрипты Python
```bash
python scripts/strokes.py <N> <M> <viscosity>
python scripts/strokes_grid.py <solution_file> <N> <M>
python scripts/solution.py <path/to/A.mtx> <path/to/b.txt>
