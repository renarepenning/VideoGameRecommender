wiki_path = 'https://en.wikipedia.org/wiki/Lists_of_video_games'
#wiki_path = 'https://en.wikipedia.org/wiki/List_of_graphic_adventure_games'

shit = '<table class="wikitable sortable" style="width:100%">'
r = requests.get(wiki_path, headers=headers)
data = r.text.split('href="/wiki/List_of')
data = list(
    map(lambda x: 'https://en.wikipedia.org/wiki/List_of' + x.split('" ')[0], data))
# data


def get_urls(main_url: str = 'https://en.wikipedia.org/wiki/Lists_of_video_games'):

    r = requests.get(wiki_path, headers=headers)
    data = r.text.split('href="/wiki/List_of')
    data = list(
        map(lambda x: 'https://en.wikipedia.org/wiki/List_of' + x.split('" ')[0], data))
    return data


def get_data(urls: list = get_urls()):
    master_path = 'Game Data'
    if not os.path.exists(master_path):
        os.mkdir(master_path)

    for url in urls:
        title = url.split('https://en.wikipedia.org/wiki/List_of')[1][1:]
        out_path = os.path.join(title, title + '.csv')
        if not os.path.exists(title):
            os.mkdir(title)
        try:
            df = pd.read_html(url)
            print(url, 'Finished')

            # Uncomment this line to populate data folders
            # df.to_csv(out_path)

        except:
            print(url, 'Invalid, no Table Muchacho')
            pass


for df in pd.read_html('https://en.wikipedia.org/wiki/List_of_crossovers_in_video_games'):
    if (type(df.columns) == pd.MultiIndex):
        df.columns = list(map(lambda x: x[1], df.columns.tolist()))


get_data()
os.getcwd()
