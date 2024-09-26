from instagrapi import Client
from credenciales import *
import pandas as pd

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)


huser_id = cl.user_id_from_username(ACCOUNT_USERNAME)
#medias = cl.user_medias(user_id, 20)

#userpablo = cl.user_id_from_username("albisites")
#mediaspablo = cl.user_clips_v1(userpablo, 2)
#print(mediaspablo)

#alba = cl.user_info_by_username('albisites')


post_id = cl.media_pk_from_url("https://www.instagram.com/p/C3QkcQ6sVPW/?img_index=1")

post =  cl.media_info(post_id)

user_id = cl.user_id_from_username("claudianicolasa")

#user_media = cl.user_medias_gql(alba_id, amount=20, sleep=5)

user_media = cl.user_clips_v1(user_id)


print(len(user_media))

#for media in user_media:


rows = []


for media in user_media:
    pk = media.pk
    commentarios_media_user = media.comment_count
    likes_media_user = media.like_count
    taken_at_user = media.taken_at
    media_type_user = media.media_type
    view_count_user = media.view_count
    play_count_user = media.play_count
    caption_text_user = media.caption_text
    #users_tagged_reels = media.usertags
    rows.append({
        "id": pk,
        "comentarios" : commentarios_media_user,
        "likes" : likes_media_user,
        "fecha": taken_at_user,
        "tipo_publicacion" : media_type_user,
        "views" : view_count_user,
        "views_new" : play_count_user,
        "titulo": caption_text_user
        

    })


df = pd.DataFrame(rows)
print(df)
# Guarda datos en CSV:
df.to_csv('data-user-reels-claudianicolasa.csv', header=False, index=False)
