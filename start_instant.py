import re
from unittest import result
from pathlib import Path
from tqdm import tqdm
from yattag import Doc, indent

try:
    f = Path(__file__).with_name('export.txt')
    with f.open('r',  encoding="utf-8") as f:
        matches = re.findall(r"(/)(\d+)", f.read())
except FileNotFoundError:
    print("Please make sure export.txt exists")
    exit()

try:
    f = Path(__file__).with_name('export.txt')
    with f.open('r',  encoding="utf-8") as f:
        matches2 = re.findall(r"(# )([A-Za-z:0-9 !?\-\\'\"\\\’,.~\/!@#$%^&*()_\+ä;:\[\]‘é`]+)", f.read())
except FileNotFoundError:
    print("Please make sure export.txt exists")
    exit()


animesID = []
animeName = []
for ids in matches:
    animesID.append(ids[1])
for names in matches2:
    animeName.append(names[1])

f2 = open("./senpaii.xml", "w",  encoding="utf-8")
f2.write("")
f2.close()

pbar = tqdm(desc="Progress", total= len(animesID))

i=0
try:
    
    for animeID in animesID:
                
        doc, tag, text = Doc().tagtext()
        try:
            with tag('root'):
                with tag('anime'):
                    with tag('series_animedb_id'):
                        text(animeID)
                    with tag('series_title'):
                        text(animeName[i])
                    with tag('series_type'):
                        text("")
                    with tag('series_episodes'):
                        text("")
                    with tag('my_id'):
                        text("0")
                    with tag('my_watched_episodes'):
                        text("")
                    with tag('my_start_date'):
                        text("0000-00-00")
                    with tag('my_finish_date'):
                        text("0000-00-00")
                    with tag('my_rated'):
                        text("")
                    with tag('my_score'):
                        text("")
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
                
                f2 = open("./senpaii.xml", "a",  encoding="utf-8")
                f2.write('\n')
                f2.write(result)
                f2.write('\n')
                f2.close
        except (Exception, AttributeError,TypeError,ValueError):
                    print(' Something went wrong')
        i = i + 1
        pbar.update()
         
except KeyboardInterrupt:
    pbar.close()
    print(' Downt\' leawwe me senpai')
    print(' 😣😣😣')
    exit()
    
pbar.close()
#Hiwwo there... You probably are wondering why this is here... right?
#Well... to be honest I am trying to figure why and how does this work... but it does the job done :D