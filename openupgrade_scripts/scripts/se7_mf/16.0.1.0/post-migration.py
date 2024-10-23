from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(
        env.cr,
        [("sale_fleet", "se7_mf"), ("portal_picking_customer_signature", "se7_mf")],
        True
    )
