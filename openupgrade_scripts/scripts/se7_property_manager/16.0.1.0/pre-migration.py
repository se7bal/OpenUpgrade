from openupgradelib import openupgrade

_fields_renames = [
    (
        "account.move",
        "account_move",
        "administrador_de_fincas",
        "property_manager_id",
    ),
    (
        "res.partner",
        "res_partner",
        "es_administrador_de_fincas",
        "is_property_manager",
    ),
    (
        "res.partner",
        "res_partner",
        "administrador_de_fincas",
        "property_manager_id",
    ),
    (
        "res.partner",
        "res_partner",
        "es_direccion_de_facturacion",
        "is_universal_invoice_address",
    ),
    (
        "sale.order",
        "sale_order",
        "administrador_de_fincas",
        "property_manager_id",
    ),
    (
        "stock.picking",
        "stock_picking",
        "administrador_de_fincas",
        "property_manager_id",
    ),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(env, _fields_renames)
