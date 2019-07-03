# Темы
JET_THEMES = [
    {
        'theme': 'default',  # theme folder name
        'color': '#47bac1',  # color of the theme's button in user menu
        'title': 'Default'  # theme title
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]

# Меню
JET_SIDE_MENU_ITEMS = [
    {'label': 'Видео', 'app_label': 'video', 'items': [
        {'name': 'video'},
    ]},
    {'label': 'Галереи и фото', 'app_label': 'photologue', 'items': [
        {'name': 'watermark'},
        {'name': 'gallery'},
        {'name': 'photosize'},
        {'name': 'photo'},
        {'name': 'photoeffect'},
    ]},
    {'label': 'Инфо блок', 'app_label': 'info_block', 'items': [
        {'name': 'infoblock'},
    ]},
    {'label': 'Календарь событий', 'app_label': 'calendar_of_events', 'items': [
        {'name': 'category'},
        {'name': 'calendar'},
        {'name': 'record'},
        {'name': 'strainer'},
    ]},
    {'label': 'Контакты', 'app_label': 'contact', 'items': [
        {'name': 'contact'},
        {'name': 'feedback'},
    ]},
    {'label': 'Меню', 'app_label': 'menu', 'items': [
        {'name': 'menu'},
        {'name': 'menuitem'},
    ]},
    {'label': 'Новости', 'app_label': 'news', 'items': [
        {'name': 'category'},
        {'name': 'post'},
        {'name': 'comments'},
        {'name': 'tags'},
    ]},
    {'label': 'О нас', 'app_label': 'about', 'items': [
        {'name': 'aboutblock'},
    ]},
    {'label': 'Партнеры', 'app_label': 'partners', 'items': [
        {'name': 'partners'},
    ]},
    {'label': 'Страницы', 'app_label': 'pages', 'items': [
        {'name': 'pages'},
    ]},
    {'label': 'Социальные сети', 'app_label': 'social_networks', 'items': [
        {'name': 'socialnetworks'},
    ]},
    {'label': 'Языки', 'app_label': 'languages', 'items': [
        {'name': 'listlang'},
    ]},
    {'label': 'Instagram', 'app_label': 'ms_instagram', 'items': [
        {'name': 'configmsinstagram'},
    ]},
    {'app_label': 'account', 'items': [
        {'name': 'emailaddress'},
    ]},
    {'app_label': 'auth', 'items': [
        {'name': 'group'},
        {'name': 'user'},
    ]},
    {'app_label': 'sites', 'items': [
        {'name': 'site'},
    ]},
    {'app_label': 'socialaccount', 'items': [
        {'name': 'socialaccount'},
        {'name': 'socialapp'},
        {'name': 'socialtoken'},
    ]},
]

# Компактное меню
# JET_SIDE_MENU_COMPACT = True

# JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
# JET_APP_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
