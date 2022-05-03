# Contexto

Refatorar o arquivo `deprecated/class1`.

# Execução

- Main (comparação via `stdout`): `python3 main.py`
  ```
  Refactored result: {'Mexico': 'Uma', 'Chile': 'Uma', 'Brazil': 'Uma'}
  Old result       : {'Mexico': 'Uma', 'Chile': 'Uma', 'Brazil': 'Uma'}

  Refactored result (SA Countries): {'Chile': 'Uma', 'Brazil': 'Uma'}
  ```
- Testes: `python3 -m unittest test/test_action1_compat.py` 
  ```
  .
  ----------------------------------------------------------------------
  Ran 1 test in 0.017s

  OK
  ```
