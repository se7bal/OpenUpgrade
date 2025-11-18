from openupgradelib import openupgrade

_fields_renames = [
    (
        "account.journal",
        "account_journal",
        "diario_tecnicos",
        "applicable_to_technician",
    ),
    (
        "account.payment.term",
        "account_payment_term",
        "cobrar_por_tecnico",
        "employee_can_collect_payment",
    ),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(env, _fields_renames)
