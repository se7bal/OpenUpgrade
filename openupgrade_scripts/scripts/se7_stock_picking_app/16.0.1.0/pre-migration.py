from openupgradelib import openupgrade

_fields_renames = [
    (
        "account.journal",
        "account_journal",
        "diario_tecnicos",
        "applicable_to_technician",
    ),
    (
        "account.journal",
        "account_journal",
        "tecnico_diario",
        "technician_ids",
    ),
    (
        "account.payment.term",
        "account_payment_term",
        "cobrar_por_tecnico",
        "employee_can_collect_payment",
    ),
    (
        "hr.employee",
        "hr_employee",
        "diario_de_cobro",
        "payment_collection_journal_id",
    ),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_fields(env, _fields_renames)
