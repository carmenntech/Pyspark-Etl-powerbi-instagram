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

alba_id = cl.user_id_from_username("albisites")

user_media = cl.user_medias(alba_id, 10)




print(len(user_media))

#for media in user_media:


rows = []


for media in user_media:
    commentarios_media_user = media.comment_count
    likes_media_user = media.like_count

    rows.append({
        "comentarios" : commentarios_media_user,
        "likes" : likes_media_user
    })


df = pd.DataFrame(rows)

print(df)
