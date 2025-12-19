if __name__ == '__main__': # test procedure
    import helpers
    print(helpers.os.name)
    print(helpers.is_running_windows())
    print(helpers.get_userdata_root())
    print(helpers.get_tidata_root())

    import config
    app_conf = config.Configuration('test', default_config={
        'volume': {
            'master': 1,
            'sfx': 1,
            'music': 1,
        },
        'fullscreen': True,
    })
    print(app_conf.config)
    print(app_conf.read_config())
    app_conf.config['fullscreen'] = not app_conf.config['fullscreen']
    app_conf.write_config()
    print(app_conf.read_config())