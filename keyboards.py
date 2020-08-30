import json

keyboardStart = {
    'inline': True,
    'buttons': [
            [
                {
                    'action': {
                        'type': 'text',
                        'label': '📖 | Инструкция по созданию паспорта',
                        'payload': json.dumps({'command': 'create_passport'})
                    },
                    'color': 'positive'
                }
            ]
        ]
}
keyboardChangeAccess = {
    'inline': True,
    'buttons': [
            [
                {
                    'action': {
                        'type': 'text',
                        'label': '📖 | Показать паспорт',
                        'payload': json.dumps({'command': 'show_passport'})
                    },
                    'color': 'positive'
                }
            ]
        ]
}