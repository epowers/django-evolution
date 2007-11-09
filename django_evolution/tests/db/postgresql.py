add_field = {
    'NullDatabaseColumnModel': 
        'ALTER TABLE "django_evolution_addbasemodel" ADD COLUMN "added_field" integer NULL;',
    'NonDefaultDatabaseColumnModel': 
        'ALTER TABLE "django_evolution_addbasemodel" ADD COLUMN "non-default_column" integer NULL;',
    'AddDatabaseColumnCustomTableModel': 
        'ALTER TABLE "custom_table_name" ADD COLUMN "added_field" integer NULL;',
    'AddIndexedDatabaseColumnModel': 
        '\n'.join([
            'ALTER TABLE "django_evolution_addbasemodel" ADD COLUMN "add_field" integer NULL;',
            'CREATE INDEX "django_evolution_addbasemodel_add_field" ON "django_evolution_addbasemodel" ("add_field");'
        ]),
    'AddUniqueDatabaseColumnModel': 
        'ALTER TABLE "django_evolution_addbasemodel" ADD COLUMN "added_field" integer NULL UNIQUE;',
    'ForeignKeyDatabaseColumnModel': 
        '\n'.join([
            'ALTER TABLE "django_evolution_addbasemodel" ADD COLUMN "added_field_id" integer NULL REFERENCES "django_evolution_addanchor1" ("id")  DEFERRABLE INITIALLY DEFERRED;',
            'CREATE INDEX "django_evolution_addbasemodel_added_field_id" ON "django_evolution_addbasemodel" ("added_field_id");'
        ]),
    'AddManyToManyDatabaseTableModel': 
        '\n'.join([
            'CREATE TABLE "django_evolution_addbasemodel_added_field" (',
            '    "id" serial NOT NULL PRIMARY KEY,',
            '    "testmodel_id" integer NOT NULL REFERENCES "django_evolution_addbasemodel" ("id") DEFERRABLE INITIALLY DEFERRED,',
            '    "addanchor1_id" integer NOT NULL REFERENCES "django_evolution_addanchor1" ("id") DEFERRABLE INITIALLY DEFERRED,',
            '    UNIQUE ("testmodel_id", "addanchor1_id")',
            ')',
            ';'
        ]),
     'AddManyToManyDatabaseTableModel_cleanup': 
        'DROP TABLE "django_evolution_addbasemodel_added_field"',
     'AddManyToManyNonDefaultDatabaseTableModel': 
        '\n'.join([
            'CREATE TABLE "django_evolution_addbasemodel_added_field" (',
            '    "id" serial NOT NULL PRIMARY KEY,',
            '    "testmodel_id" integer NOT NULL REFERENCES "django_evolution_addbasemodel" ("id") DEFERRABLE INITIALLY DEFERRED,',
            '    "addanchor2_id" integer NOT NULL REFERENCES "custom_add_anchor_table" ("id") DEFERRABLE INITIALLY DEFERRED,',
            '    UNIQUE ("testmodel_id", "addanchor2_id")',
            ')',
            ';'
        ]),
     'AddManyToManyNonDefaultDatabaseTableModel_cleanup': 
        'DROP TABLE "django_evolution_addbasemodel_added_field"',
     'ManyToManySelf': 
        '\n'.join([
            'CREATE TABLE "django_evolution_addbasemodel_added_field" (',
            '    "id" serial NOT NULL PRIMARY KEY,',
            '    "from_testmodel_id" integer NOT NULL REFERENCES "django_evolution_addbasemodel" ("id") DEFERRABLE INITIALLY DEFERRED,',
            '    "to_testmodel_id" integer NOT NULL REFERENCES "django_evolution_addbasemodel" ("id") DEFERRABLE INITIALLY DEFERRED,',
            '    UNIQUE ("from_testmodel_id", "to_testmodel_id")',
            ')',
            ';'
        ]),
     'ManyToManySelf_cleanup': 
        'DROP TABLE "django_evolution_addbasemodel_added_field"',
}

delete_field = {
    'DefaultNamedColumnModel': 
        'ALTER TABLE "django_evolution_deletebasemodel" DROP COLUMN "int_field" CASCADE;',
    'NonDefaultNamedColumnModel': 
        'ALTER TABLE "django_evolution_deletebasemodel" DROP COLUMN "non-default_db_column" CASCADE;',
    'ConstrainedColumnModel': 
        'ALTER TABLE "django_evolution_deletebasemodel" DROP COLUMN "int_field3" CASCADE;',
    'DefaultManyToManyModel': 
        'DROP TABLE "django_evolution_deletebasemodel_m2m_field1";',
    'NonDefaultManyToManyModel': 
        'DROP TABLE "non-default_m2m_table";',
    'DeleteForeignKeyModel': 
        'ALTER TABLE "django_evolution_deletebasemodel" DROP COLUMN "fk_field1_id" CASCADE;',
    'DeleteColumnCustomTableModel': 
        'ALTER TABLE "custom_table_name" DROP COLUMN "value" CASCADE;',
}

rename_field = {
    'RenameColumnModel': 
        'ALTER TABLE "django_evolution_renamebasemodel" RENAME COLUMN "int_field" TO "renamed_field";',
    'RenameColumnWithTableNameModel': 
        'ALTER TABLE "django_evolution_renamebasemodel" RENAME COLUMN "int_field" TO "renamed_field";',
    'RenamePrimaryKeyColumnModel': 
        'ALTER TABLE "django_evolution_renamebasemodel" RENAME COLUMN "id" TO "my_pk_id";',
    'RenameForeignKeyColumnModel': 
        'ALTER TABLE "django_evolution_renamebasemodel" RENAME COLUMN "fk_field_id" TO "renamed_field_id";',
    'RenameNonDefaultColumnNameModel': 
        'ALTER TABLE "django_evolution_renamebasemodel" RENAME COLUMN "custom_db_col_name" TO "renamed_field";',
    'RenameNonDefaultColumnNameToNonDefaultNameModel': 
        'ALTER TABLE "django_evolution_renamebasemodel" RENAME COLUMN "custom_db_col_name" TO "non-default_column_name";',
    'RenameNonDefaultColumnNameToNonDefaultNameAndTableModel': 
        'ALTER TABLE "django_evolution_renamebasemodel" RENAME COLUMN "custom_db_col_name" TO "non-default_column_name2";',
    'RenameColumnCustomTableModel': 
        'ALTER TABLE "custom_rename_table_name" RENAME COLUMN "value" TO "renamed_field";',
    'RenameManyToManyTableModel': 
        'ALTER TABLE "django_evolution_renamebasemodel_m2m_field" RENAME TO "django_evolution_renamebasemodel_renamed_field";',
    'RenameManyToManyTableModel_cleanup': 
        'DROP TABLE "django_evolution_renamebasemodel_renamed_field"',
    'RenameManyToManyTableWithColumnNameModel': 
        'ALTER TABLE "django_evolution_renamebasemodel_m2m_field" RENAME TO "django_evolution_renamebasemodel_renamed_field";',
    'RenameManyToManyTableWithColumnNameModel_cleanup': 
        'DROP TABLE "django_evolution_renamebasemodel_renamed_field"',
    'RenameNonDefaultManyToManyTableModel': 
        'ALTER TABLE "non-default_db_table" RENAME TO "django_evolution_renamebasemodel_renamed_field";',
    'RenameNonDefaultManyToManyTableModel_cleanup': 
        'DROP TABLE "django_evolution_renamebasemodel_renamed_field"',
}