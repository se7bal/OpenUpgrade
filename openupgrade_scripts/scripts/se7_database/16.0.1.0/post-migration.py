from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(
        env.cr,
        [("se7_databases", "se7_database"), ("se7_databases_token", "se7_database")],
        merge_modules=True,
    )
