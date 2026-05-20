import random
from database import players
from team_select import escolher_time
from systems.hackathon import iniciar_hackathon

# Criar time
print("================== TESTE HACKATHON ==================\n")
time_player = escolher_time(players)
print()

# Rodar hackathon
iniciar_hackathon(time_player)

print("\n===================== FIM DO TESTE =====================")
