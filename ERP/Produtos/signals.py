from django.core.management import call_command
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def carregar_fixtures_apos_migracao(sender, **kwargs):
    try:
        print("⏳ Carregando dados iniciais de Cor.json...")
        call_command('loaddata', 'Cores')
        print("✅ Dados de Cor carregados com sucesso.")
    except Exception as e:
        print(f"⚠️ Erro ao carregar fixture: {e}")

#    try:
#        print("⏳ Carregando dados iniciais de Tamanho.json...")
#        call_command('loaddata', 'Tamanhos')
#        print("✅ Dados de Tamanho carregados com sucesso.")
#    except Exception as e:
#        print(f"⚠️ Erro ao carregar fixture: {e}")        

    
