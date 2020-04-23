class Config:
    def __init__(self, env):
        supported_envs = ['dev', 'qa']
        if env.lower() not in supported_envs:
            raise ValueError(f'{env} is not a supported environment (supported envs: {supported_envs})')
        self.base_url = {
            'dev': 'https://dev.com',
            'qa': 'https://qa.com',
            'stage': 'https://stage.com',
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80,
            'stage': 8081,
        }[env]
