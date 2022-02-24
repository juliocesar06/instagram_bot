# importando biblioteca de acesso ao insta
from instapy import InstaPy
from instapy import smart_run

#loguin coloca login e senha
insta_username = ''
insta_password = ''

#perfil que deseja seguir deixa especifico o tipo de seguidores
perfil1 =['wordpress']
perfil2 ='brasil'
print('esse esta rodando')

# sessao para iniciar o instagram com login e senha
session = InstaPy(username=insta_username,
                  password=insta_password,
                  #inicia com navegador oculto
                  headless_browser=False,
                  
                  )
#funçao que segue e deixa de seguir usuarios
with smart_run(session):
        # definir limites de seguidores
        session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    #numero maximo de seguidores
                                    max_followers=5900,
                                    # minimo de seguidores
                                    min_followers=10,
                                    #minimo seguindo
                                    min_following=10)
# activities
        # expecifica o tipo de usuarios que ira seguir,pelo assundo que o usuario segui
        session.follow_user_followers(perfil1, amount=100,)
    
    
        # essa parte deixa de seguir quem nao te segi quem nao te segui em 12horas
        session.unfollow_users(amount=80, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=301)
        # seguindo massivamente todos com perfil selecionado 
        session.follow_user_followers([perfil1], amount=300,
                                  randomize=False, interact=False)

        #deixa de seguir quem nao te segui em 12h
        session.unfollow_users(amount=150, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=301)
        
        # deixa de seguir os usuarios que nao esta segundo depois de  24h
        session.unfollow_users(amount=250, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=301)
