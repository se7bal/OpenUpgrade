from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(
        env.cr,
        [
            (
                "se7_improved_signature_widget",
                "se7_web_widget_signature_extra_fields",
            )
        ],
    )
