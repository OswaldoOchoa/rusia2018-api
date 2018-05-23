#MVP

## Objetivo de Negocio

Un servicio web diseñado para sortear entre 8 participantes
los 32 equipos del Mundial Rusia 2018 de forma equitativa y justa.

## Como usuario yo quiero...

1. Sortear participantes
2. Sortear un equipo
3. Ver resultados del sorteo


## Arquitectura de datos

- Home - NOT in the MVP
  - Ver resultados del sorteo
  - Ver participantes (antes y despues del sorteo)
  - Inscribirse (facebook login)
  - Sorteo en Vivo (MVP is only this screen)
- Sorteo
- Resultados (pantalla participantes después del sorteo)


## Arquitectura componentes
- Home
  - Contenders
      - Avatar
        - TeamFlags
    - Groups
      - Teams
    - Sort
      - Sort Contenders
      - Sort Teams
    - Results
