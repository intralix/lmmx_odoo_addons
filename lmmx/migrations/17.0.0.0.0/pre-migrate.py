def migrate(cr, version):    

    # TO CORRECT UPGRADE ERROR 1 : Element '<xpath expr="//xxxx">' cannot be located in parent view

    cr.execute("""
        UPDATE ir_module_module 
        set state='to remove'
        WHERE name in ('mass_editing,cnd_l10n_mx_edi_import_cfdi') 
        and state='installed';
    """)
