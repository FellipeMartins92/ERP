from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def carregar_fixtures_apos_migracao(sender, **kwargs):
    try:
        print("⏳ Carregando dados iniciais de classe_cliente.json...")
        call_command('loaddata', 'Classe_Cliente')
        print("✅ Dados de Classe_Cliente carregados com sucesso.")
    except Exception as e:
        print(f"⚠️ Erro ao carregar fixture: {e}")