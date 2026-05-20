# 📁 Estrutura do Projeto RESENHEDES

## Organização Modular

A partir de agora, o projeto está organizado de forma modular e independente:

```
RESENHEDES/
├── main.py                 # Arquivo principal (menu principal)
├── database.py             # Dados dos jogadores
├── player.py               # Classe Player
├── team.py                 # Classe Team
├── team_select.py          # Seleção de time
├── viewer.py               # Exibição de dados
├── resenha.py              # Função de resenha
├── templates/              # HTML templates
│   ├── index.html
│   ├── player.html
│   └── relacoes.html
└── systems/                # 🎮 Sistemas Modularizados
    ├── __init__.py
    ├── actions/            # 🎯 Ações disponíveis
    │   ├── __init__.py
    │   ├── estudar.py      # Estudar programação
    │   ├── academia.py     # Ir treinar
    │   ├── descansar.py    # Descansar
    │   └── curso_online.py # Comprar curso
    ├── events/             # 🎲 Sistema de eventos aleatórios
    │   ├── __init__.py
    │   ├── event_system.py # Gerenciador de eventos
    │   ├── evento_resenha.py
    │   ├── evento_bug.py
    │   ├── evento_gambiarra.py
    │   ├── evento_fofoca.py
    │   ├── evento_trairagem.py
    │   ├── evento_colapso.py
    │   └── evento_academia.py
    └── hackathon/          # 🏆 Sistema de hackathon
        ├── __init__.py
        └── hackathon_system.py
```

## Benefícios

✅ **Modularidade**: Cada ação/evento é um arquivo independente  
✅ **Facilidade de Manutenção**: Mudanças isoladas não quebram o sistema  
✅ **Escalabilidade**: Fácil adicionar novas ações e eventos  
✅ **Limpeza**: Lógica organizada e sem classes quebradas  
✅ **Flexibilidade**: Funções simples que recebem o `team` como parâmetro  

## Como Importar

### Ações
```python
from systems.actions import estudar_programacao, ir_academia, descansar, curso_online

estudar_programacao(time_player)
ir_academia(time_player)
descansar(time_player)
curso_online(time_player)
```

### Eventos
```python
from systems.events import gerar_evento

gerar_evento(time_player)
```

### Hackathon
```python
from systems.hackathon import iniciar_hackathon, calcular_forca

iniciar_hackathon(time_player)
forca = calcular_forca(time_player)
```

## Adicionando Novas Funcionalidades

### Adicionar uma nova ação:
1. Crie `systems/actions/nova_acao.py`
2. Defina `def nova_acao(team):`
3. Importe em `systems/actions/__init__.py`
4. Use em `main.py`

### Adicionar um novo evento:
1. Crie `systems/events/evento_novo.py`
2. Defina `def evento_novo(team):`
3. Adicione à lista de eventos em `systems/events/event_system.py`
