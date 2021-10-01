from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/movementmemos"
url2 = "https://feeds.megaphone.fm/climatefrontlines"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/e651e3ce-4467-11ea-a211-ff38e4cd73bf/image/uploads_2F1580502557604-wt9hb1huy6f-77289447a37f40637357673929f67709_2Fmovement-memos-fin-a.jpg?ixlib=rails-2.1.2&max-w=3000&max-h=3000&fit=crop&auto=format,compress"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/c9f01482-1967-11eb-be5a-3b30b6c2b4e1/image/uploads_2F1605285309636-6sirg6em403-93059d842d47b7ebfa8f8221456939ae_2Fclimate-front-lines.jpg?ixlib=rails-2.1.2&max-w=3000&max-h=3000&fit=crop&auto=format,compress"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

if __name__ == '__main__':
    plugin.run()
