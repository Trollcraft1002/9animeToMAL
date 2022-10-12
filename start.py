import re
from unittest import result
from mal import Anime
from pathlib import Path
from time import sleep
from tqdm import tqdm
from yattag import Doc, indent



#test = "https://myanimelist.net/anime/31580/ https://myanimelist.net/anime/8630/"
#matches = re.findall(r"(/)(\d+)", f)
try:
    f = Path(__file__).with_name('export.txt')
    with f.open('r',  encoding="utf-8") as f:
        matches = re.findall(r"(/)(\d+)", f.read())
except FileNotFoundError:
    print("Please make sure export.txt exists")
    exit()

animesID = []
for ids in matches:
    animesID.append(ids[1])


f2 = open("./testFile.xml", "w",  encoding="utf-8")
f2.write("")
f2.close()

pbar = tqdm(desc="Progress", total= len(animesID))

failed = []
try:
    for animeID in animesID:
        #print(anime.title)
        #print(anime.episodes)
        try:
            anime = Anime(animeID)
            animeName = anime.title
            animeEp = anime.episodes
            animeType = anime.type
        except ValueError:
                print(" Coudn't find anime " + animeID + " on MAL API :/ gonna continue...")
                failed.append(animeID)
        except Exception:
            print(" Temporary blocked by MAL. Trying in 2 minutes...")
            sleep(2*60)
            print(" Anime " + animeID + " was skipped please add it manually")
            failed.append(animeID)
                
        doc, tag, text = Doc().tagtext()
        try:
            with tag('root'):
                with tag('anime'):
                    with tag('series_animedb_id'):
                        text(animeID)
                    with tag('series_title'):
                        text(animeName)
                    with tag('series_type'):
                        text(animeType)
                    with tag('series_episodes'):
                        text(animeEp)
                    with tag('my_id'):
                        text("0")
                    with tag('my_watched_episodes'):
                        text(animeEp)
                    with tag('my_start_date'):
                        text("0000-00-00")
                    with tag('my_finish_date'):
                        text("0000-00-00")
                    with tag('my_rated'):
                        text("")
                    with tag('my_score'):
                        text(10)
                    with tag('my_dvd'):
                        text("")
                    with tag('my_storage'):
                        text("")
                    with tag('my_status'):
                        text('Completed')
                    with tag('my_comments'):
                        text("")
                    with tag('my_times_watched'):
                        text('0')
                    with tag('my_rewatch_value'):
                        text('Low')
                    with tag('my_tags'):
                        text('')
                    with tag('my_rewatching'):
                        text('0')
                    with tag('my_rewatching_ep'):
                        text('0')
                    with tag('update_on_import'):
                        text('1')
                
                result = indent(
                doc.getvalue(),
                indentation = ' '*4,
                newline = '\n'
                )
                
                f2 = open("./testFile.xml", "a",  encoding="utf-8")
                f2.write('\n')
                f2.write(result)
                f2.write('\n')
                f2.close
        except (Exception, AttributeError,TypeError,ValueError):
                    print(' Something went wrong')
                    failed.append(animeID)

        pbar.update()
    
except KeyboardInterrupt:
    pbar.close()
    print(' Downt\' leawwe me senpai')
    print(' 😣😣😣')
    exit()
    
pbar.close()

if failed:
    print('those failed to import')
    for failedAnimes in failed:
        print(failedAnimes)
    print('please add them mannualy')



"""
<anime>
        <series_animedb_id>6547</series_animedb_id>
        <series_title><![CDATA[Angel Beats!]]></series_title>
        <series_type>TV</series_type>
        <series_episodes>13</series_episodes>
        <my_id>0</my_id>
        <my_watched_episodes>13</my_watched_episodes>
        <my_start_date>0000-00-00</my_start_date>
        <my_finish_date>0000-00-00</my_finish_date>
        <my_rated></my_rated>
        <my_score>9</my_score>
        <my_dvd></my_dvd>
        <my_storage></my_storage>
        <my_status>Completed</my_status>
        <my_comments><![CDATA[]]></my_comments>
        <my_times_watched>0</my_times_watched>
        <my_rewatch_value>Low</my_rewatch_value>
        <my_tags><![CDATA[]]></my_tags>
        <my_rewatching>0</my_rewatching>
        <my_rewatching_ep>0</my_rewatching_ep>
        <update_on_import>0</update_on_import>
    </anime>
"""