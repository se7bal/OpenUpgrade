from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(
        env.cr,
        [("se7_mf_diarios_tecnicos", "se7_stock_picking_app")],
    )
