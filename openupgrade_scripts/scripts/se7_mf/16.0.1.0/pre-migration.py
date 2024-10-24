from openupgradelib import openupgrade

_fields_renames = [
    # (
    #     "account.payment.term",
    #     "account_payment_term",
    #     "diario_por_defecto",
    #     "default_sale_journal_id",
    # ),
    (
        "fleet.vehicle",
        "fleet_vehicle",
        "codigo_vehiculo",
        "code",
    ),
    (
        "product.product",
        "product_product",
        "duracion_teorica_total",
        "estimated_duration",
    ),
    # (
    #     "sale.order",
    #     "sale_order",
    #     "diario_facturacion",
    #     "invoicing_journal_id",
    # ),
    (
        "sale.order",
        "sale_order",
        "num_albaran_antiguo",
        "old_picking_number",
    ),
    (
        "sale.order",
        "sale_order",
        "parte_de_trabajo",
        "work_report",
    ),
    (
        "sale.order",
        "sale_order",
        "vehicle",
        "vehicle_id",
    ),
    (
        "sale.order",
        "sale_order",
        "conductor",
        "driver_id",
    ),
    (
        "sale.order",
        "sale_order",
        "ayudantes",
        "assistant_ids",
    ),
    (
        "sale.order",
        "sale_order",
        "nombre_contacto",
        "contact_person",
    ),
    (
        "sale.order",
        "sale_order",
        "telefono_contacto",
        "contact_phone",
    ),
    (
        "sale.order",
        "sale_order",
        "notas_de_contacto",
        "contact_notes",
    ),
    (
        "sale.order",
        "sale_order",
        "horario_atencion",
        "attention_schedule_id",
    ),
    (
        "sale.order",
        "sale_order",
        "duracion_teorica",
        "estimated_duration",
    ),
    (
        "sale.order",
        "sale_order",
        "duracion_prevista",
        "expected_duration",
    ),
    (
        "sale.order.line",
        "sale_order_line",
        "duracion_teorica",
        "estimated_duration",
    ),
    (
        "stock.picking",
        "stock_picking",
        "garantia",
        "has_warranty",
    ),
    (
        "stock.picking",
        "stock_picking",
        "texto_garantia",
        "warranty_text",
    ),
]
_models_renames = [("saler.order.horarioatencion", "sale.order.attention.schedule")]
_tables_renames = [("saler_order_horarioatencion", "sale_order_attention_schedule")]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(env, _fields_renames)
    openupgrade.rename_models(env.cr, _models_renames)
    openupgrade.rename_tables(env.cr, _tables_renames)
