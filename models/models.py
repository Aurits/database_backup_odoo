from odoo import models, fields, api
import os
import subprocess
import logging

_logger = logging.getLogger(__name__)

class database_backup(models.TransientModel):
    _name = 'database_backup.database_backup'
    _description = 'Database Backup'

    def backup_db(self):
        db_name = self.env.cr.dbname
        backup_path = '/home/aurit/Projects/odoo-17.0/BACKUP'
        filename = f"{db_name}.dump"
        complete_path = os.path.join(backup_path, filename)
        db_user = 'odoo'  # Specify the PostgreSQL user that has access to the database

        # Construct the pg_dump command with user authentication
        command = f"pg_dump -U {db_user} -d {db_name} -F c > {complete_path}"
        
        try:
            # Use the full path to pg_dump if needed, e.g., /usr/bin/pg_dump
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            _logger.error('Failed to execute command: %s', e)