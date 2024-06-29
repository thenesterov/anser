CONFIG_SCHEMA = '''\
[anser]
url = ''

[anser.migrations]
path = '{path_to_migrations}'
'''

TEMPLATE_SCHEMA = '''\
"""
Current UUID: {current_uuid}
Parent UUID: {parent_uuid}
Created at: {created_at}
Message: {message}

"""

current_uuid: str | None = '{current_uuid}'
parent_uuid: str | None = '{parent_uuid}'

def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
'''
