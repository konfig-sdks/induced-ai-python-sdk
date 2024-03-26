operation_parameter_map = {
    '/autonomous/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/autonomous/{id}/stop-POST': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/extract-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'query'
            },
            {
                'name': 'columns'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/extract/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/autonomous/{id}/feedback-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'feedback'
            },
        ]
    },
    '/autonomous-POST': {
        'parameters': [
            {
                'name': 'task'
            },
        ]
    },
};