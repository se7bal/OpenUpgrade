from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.update_module_names(
        env.cr,
        [("se7_pg_yacht_area", "se7_boat_area")],
    )

    openupgrade.logged_query(
        env.cr,
        """
        update account_move_line
        set boat_area_id = (select yacht_area from account_invoice_line where id = old_invoice_line_id);

        insert into boat_boat_area_rel SELECT yacht_area_yacht_yacht_rel.yacht_area_id, yacht_area_yacht_yacht_rel.yacht_yacht_id FROM public.yacht_area_yacht_yacht_rel;
        """
    )
