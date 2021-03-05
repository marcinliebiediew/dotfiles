#!/usr/bin/env python3
from argparse import ArgumentParser
from typing import Dict

from i3ipc.aio import Connection
import asyncio

screen_size = (3840, 2160)
window_size_proportions = (1 / 2, 2 / 3)

window_size = (int(screen_size[0] * window_size_proportions[0]),
               int(screen_size[1] * window_size_proportions[1]))
window_position = (int((screen_size[0] - window_size[0]) / 2),
                   int((screen_size[1] - window_size[1]) / 2))


async def do_the_thing(app: Dict):
    i3 = await Connection().connect()
    root = await i3.get_tree()
    focused = root.find_focused()
    window = root.find_named(
        app['window_name']
    ) if app['window_name'] != None else root.find_classed(app['window_class'])

    # if len(window) > 1:

    if w := window:
        if w[0].workspace().name != focused.workspace().name:
            if root.find_fullscreen():
                await focused.command('fullscreen disable')
            await w[0].command('floating enable')
            await w[0].command('move to workspace current')
            await w[0].command('fullscreen disable')
            await w[0].command('focus')
            await w[0].command('resize set {x} {y}'.format(x=window_size[0],
                                                           y=window_size[1]))
            await w[0].command('move position {x} {y}'.format(
                x=window_position[0], y=window_position[1]))
            print(window_size[0], window_position)
        else:
            await w[0].command('move to workspace {}'.format(
                app['default_workspace']))
            await w[0].command('floating disable')
    else:
        await i3.command(app['command_to_open'])


if __name__ == '__main__':

    parser = ArgumentParser(prog='bring-floating-app-to-current-workspace',
                            description='''
        Get the app
        ''')
    parser.add_argument('--app', dest='app', help='App to launch')
    args = parser.parse_args()

    apps = {
        # 'roam': {
        #     'stich_many_into_one': False,
        #     'default_workspace':
        #     '18:notes',
        #     'window_name':
        #     'roamresearch.com QuteNotes',
        #     'window_class':
        #     None,
        #     'command_to_open':
        #     '''exec "qutebrowser -C ~/.config/qutebrowser/config_notes.py https://roamresearch.com/#/app/disassemblekkiduchemler"''',
        # },
        # 'logseq': {
        #     'stich_many_into_one': False,
        #     'default_workspace':
        #     '18:notes',
        #     'window_name':
        #     'logseq.com QuteNotes',
        #     'window_class':
        #     None,
        #     'command_to_open':
        #     '''exec "qutebrowser -C ~/.config/qutebrowser/config_notes.py https://logseq.com "''',
        # },
        'spotify': {
            'stich_many_into_one': False,
            'default_workspace': '20:music',
            'window_name': None,
            'window_class': 'Spotify',
            'command_to_open': 'exec /usr/bin/spotify',
        },
        'auryo': {
            'stich_many_into_one': False,
            'default_workspace': '20:music',
            'window_name': None,
            'window_class': 'Auryo',
            'command_to_open': 'exec fish -c auryo',
        },
        'productivity_box': {
            'stich_many_into_one': False,
            'default_workspace': '20:music',
            'window_name': None,
            'window_class': 'Auryo',
            'command_to_open': 'exec fish -c auryo',
        },
        # 'notion': {
        #     'stich_many_into_one': False,
        #     'default_workspace':
        #     '18:emacs',
        #     'window_name':
        #     "www.notion.so QuteNotes",
        #     'window_class':
        #     None,
        #     'command_to_open':
        #     '''exec "qutebrowser -C ~/.config/qutebrowser/config_notes.py https://notion.com "''',
        # },
        'fb_ola': {
            'stich_many_into_one': False,
            'default_workspace':
            '17:comm',
            'window_name':
            "www.messenger.com QuteNotes",
            'window_class':
            None,
            'command_to_open':
            '''exec "qutebrowser -C ~/.config/qutebrowser/config_notes.py https://messenger.com/t/100001036064083"''',
        },
        'emacs': {
            'stich_many_into_one': True,
            'default_workspace':
            '11:emacs',
            'window_name':
            None,
            'window_class':
            "Emacs",
            'command_to_open':
            '''exec "emacsclient -nc"; mark emacs; move window to mark emacs; layout tabbed''',
        }
    }

    app_to_have_fun_with = apps[args.app]

    asyncio.run(do_the_thing(app_to_have_fun_with))
