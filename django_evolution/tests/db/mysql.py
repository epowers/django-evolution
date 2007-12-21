add_field = {
    'AddNonNullNonCallableDatabaseColumnModel':
        '\n'.join([
            'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `added_field` integer ;',
            'UPDATE `django_evolution_addbasemodel` SET `added_field` = 1 WHERE `added_field` IS NULL;',
            'ALTER TABLE `django_evolution_addbasemodel` MODIFY COLUMN `added_field` integer NOT NULL;',
        ]),
    'AddNonNullCallableDatabaseColumnModel':
        '\n'.join([
            'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `added_field` integer ;',
            'UPDATE `django_evolution_addbasemodel` SET `added_field` = `int_field` WHERE `added_field` IS NULL;',
            'ALTER TABLE `django_evolution_addbasemodel` MODIFY COLUMN `added_field` integer NOT NULL;',
        ]),
    'AddNullColumnWithInitialDatabaseColumnModel':
        '\n'.join([
            'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `added_field` integer ;',
            'UPDATE `django_evolution_addbasemodel` SET `added_field` = 1 WHERE `added_field` IS NULL;',
        ]),
    'AddStringDatabaseColumnModel':
        '\n'.join([
            'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `added_field` varchar(10) ;',
            'UPDATE `django_evolution_addbasemodel` SET `added_field` = \'abc\\\'s xyz\' WHERE `added_field` IS NULL;',
            'ALTER TABLE `django_evolution_addbasemodel` MODIFY COLUMN `added_field` varchar(10) NOT NULL;',
        ]),
    'AddDateDatabaseColumnModel':
        '\n'.join([
            'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `added_field` datetime ;',
            'UPDATE `django_evolution_addbasemodel` SET `added_field` = 2007-12-13 16:42:00 WHERE `added_field` IS NULL;',
            'ALTER TABLE `django_evolution_addbasemodel` MODIFY COLUMN `added_field` datetime NOT NULL;',
        ]),    
    'NullDatabaseColumnModel': 
        'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `added_field` integer NULL ;',
    'NonDefaultDatabaseColumnModel': 
        'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `non-default_column` integer NULL ;',
    'AddDatabaseColumnCustomTableModel':  
        'ALTER TABLE `custom_table_name` ADD COLUMN `added_field` integer NULL ;',
    'AddIndexedDatabaseColumnModel': 
        '\n'.join([
            'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `add_field` integer NULL ;',
            'CREATE INDEX `django_evolution_addbasemodel_add_field` ON `django_evolution_addbasemodel` (`add_field`);'
        ]),
    'AddUniqueDatabaseColumnModel': 
        'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `added_field` integer NULL UNIQUE;',
    'ForeignKeyDatabaseColumnModel': 
        '\n'.join([
            'ALTER TABLE `django_evolution_addbasemodel` ADD COLUMN `added_field_id` integer NULL REFERENCES `django_evolution_addanchor1` (`id`) ;',
            'CREATE INDEX `django_evolution_addbasemodel_added_field_id` ON `django_evolution_addbasemodel` (`added_field_id`);'
        ]),
    'AddManyToManyDatabaseTableModel': 
        '\n'.join([
            'CREATE TABLE `django_evolution_addbasemodel_added_field` (',
            '    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,',
            '    `testmodel_id` integer NOT NULL REFERENCES `django_evolution_addbasemodel` (`id`),',
            '    `addanchor1_id` integer NOT NULL REFERENCES `django_evolution_addanchor1` (`id`),',
            '    UNIQUE (`testmodel_id`, `addanchor1_id`)',
            ')',
            ';'
        ]),
     'AddManyToManyDatabaseTableModel_cleanup': 
        'DROP TABLE `django_evolution_addbasemodel_added_field`',
     'AddManyToManyNonDefaultDatabaseTableModel': 
        '\n'.join([
            'CREATE TABLE `django_evolution_addbasemodel_added_field` (',
            '    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,',
            '    `testmodel_id` integer NOT NULL REFERENCES `django_evolution_addbasemodel` (`id`),',
            '    `addanchor2_id` integer NOT NULL REFERENCES `custom_add_anchor_table` (`id`),',
            '    UNIQUE (`testmodel_id`, `addanchor2_id`)',
            ')',
            ';'
        ]),
     'AddManyToManyNonDefaultDatabaseTableModel_cleanup': 
        'DROP TABLE `django_evolution_addbasemodel_added_field`',
     'ManyToManySelf': 
        '\n'.join([
            'CREATE TABLE `django_evolution_addbasemodel_added_field` (',
            '    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,',
            '    `from_testmodel_id` integer NOT NULL REFERENCES `django_evolution_addbasemodel` (`id`),',
            '    `to_testmodel_id` integer NOT NULL REFERENCES `django_evolution_addbasemodel` (`id`),',
            '    UNIQUE (`from_testmodel_id`, `to_testmodel_id`)',
            ')',
            ';'
        ]),
     'ManyToManySelf_cleanup': 
        'DROP TABLE `django_evolution_addbasemodel_added_field`',
}

delete_field = {
    'DefaultNamedColumnModel': 
        'ALTER TABLE `django_evolution_deletebasemodel` DROP COLUMN `int_field` CASCADE;',
    'NonDefaultNamedColumnModel': 
        'ALTER TABLE `django_evolution_deletebasemodel` DROP COLUMN `non-default_db_column` CASCADE;',
    'ConstrainedColumnModel': 
        'ALTER TABLE `django_evolution_deletebasemodel` DROP COLUMN `int_field3` CASCADE;',
    'DefaultManyToManyModel': 
        'DROP TABLE `django_evolution_deletebasemodel_m2m_field1`;',
    'NonDefaultManyToManyModel': 
        'DROP TABLE `non-default_m2m_table`;',
    'DeleteForeignKeyModel': 
        'ALTER TABLE `django_evolution_deletebasemodel` DROP COLUMN `fk_field1_id` CASCADE;',
    'DeleteColumnCustomTableModel': 
        'ALTER TABLE `custom_table_name` DROP COLUMN `value` CASCADE;',
}

delete_model = {
    'BasicModel': 
        'DROP TABLE `django_evolution_basicmodel`;',
    'BasicWithM2MModel': 
        '\n'.join([
            'DROP TABLE `django_evolution_basicwithm2mmodel_m2m`;',
            'DROP TABLE `django_evolution_basicwithm2mmodel`;'
        ]),
    'CustomTableModel': 
        'DROP TABLE `custom_table_name`;',
    'CustomTableWithM2MModel': 
        '\n'.join([
            'DROP TABLE `another_custom_table_name_m2m`;',
            'DROP TABLE `another_custom_table_name`;'
        ]),
}

delete_application = {
    'DeleteApplication':
        '\n'.join([
            'DROP TABLE `django_evolution_appdeleteanchor1`;',
            'DROP TABLE `django_evolution_appdeletebasemodel_anchor_m2m`;',
            'DROP TABLE `django_evolution_appdeletebasemodel`;',
            'DROP TABLE `app_delete_custom_add_anchor_table`;',
        ]),
}

rename_field = {
    'RenameColumnModel': 
        'ALTER TABLE `django_evolution_renamebasemodel` CHANGE `int_field` `renamed_field` integer NOT NULL;',
    'RenameColumnWithTableNameModel': 
        'ALTER TABLE `django_evolution_renamebasemodel` CHANGE `int_field` `renamed_field` integer NOT NULL;',
    'RenamePrimaryKeyColumnModel': 
        'ALTER TABLE `django_evolution_renamebasemodel` CHANGE `id` `my_pk_id`;',
    'RenameForeignKeyColumnModel': 
        'ALTER TABLE `django_evolution_renamebasemodel` CHANGE `fk_field_id` `renamed_field_id` integer NOT NULL;',
    'RenameNonDefaultColumnNameModel': 
        'ALTER TABLE `django_evolution_renamebasemodel` CHANGE `custom_db_col_name` `renamed_field` integer NOT NULL;',
    'RenameNonDefaultColumnNameToNonDefaultNameModel': 
        'ALTER TABLE `django_evolution_renamebasemodel` CHANGE `custom_db_col_name` `non-default_column_name` integer NOT NULL;',
    'RenameNonDefaultColumnNameToNonDefaultNameAndTableModel': 
        'ALTER TABLE `django_evolution_renamebasemodel` CHANGE `custom_db_col_name` `non-default_column_name2` integer NOT NULL;',
    'RenameColumnCustomTableModel': 
        'ALTER TABLE `custom_rename_table_name` CHANGE `value` `renamed_field` integer NOT NULL;',
    'RenameManyToManyTableModel': 
        'ALTER TABLE `django_evolution_renamebasemodel_m2m_field` RENAME TO `django_evolution_renamebasemodel_renamed_field`;',
    'RenameManyToManyTableModel_cleanup': 
        'DROP TABLE `django_evolution_renamebasemodel_renamed_field`',
    'RenameManyToManyTableWithColumnNameModel': 
        'ALTER TABLE `django_evolution_renamebasemodel_m2m_field` RENAME TO `django_evolution_renamebasemodel_renamed_field`;',
    'RenameManyToManyTableWithColumnNameModel_cleanup': 
        'DROP TABLE `django_evolution_renamebasemodel_renamed_field`',
    'RenameNonDefaultManyToManyTableModel': 
        'ALTER TABLE `non-default_db_table` RENAME TO `django_evolution_renamebasemodel_renamed_field`;',
    'RenameNonDefaultManyToManyTableModel_cleanup': 
        'DROP TABLE `django_evolution_renamebasemodel_renamed_field`',
}


sql_mutation = {
    'SQLMutationSequence': """[
...    SQLMutation('first-two-fields', [
...        'ALTER TABLE `django_evolution_sqlbasemodel` ADD COLUMN `added_field1` integer NULL;',
...        'ALTER TABLE `django_evolution_sqlbasemodel` ADD COLUMN `added_field2` integer NULL;'
...    ], update_first_two),
...    SQLMutation('third-field', [
...        'ALTER TABLE `django_evolution_sqlbasemodel` ADD COLUMN `added_field3` integer NULL;',
...    ], update_third)]
""",
    'SQLMutationOutput': 
        '\n'.join([
            'ALTER TABLE `django_evolution_sqlbasemodel` ADD COLUMN `added_field1` integer NULL;',
            'ALTER TABLE `django_evolution_sqlbasemodel` ADD COLUMN `added_field2` integer NULL;',
            'ALTER TABLE `django_evolution_sqlbasemodel` ADD COLUMN `added_field3` integer NULL;',
        ]),
}
