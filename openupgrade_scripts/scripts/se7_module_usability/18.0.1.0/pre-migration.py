from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(
        env.cr,
        [
            ("se7_module_log", "se7_module_usability"),
            ("se7_module_to_upgrade", "se7_module_usability"),
        ],
        merge_modules=True,
    )
