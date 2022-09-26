"""
Created to test simple script as papermill
"""
import papermill as pm

parameters = {
    "db": "db-dev",
}

#  execute_notebook(input_path, output_path, parameters, engine_name, request_save_on_cell_execute, prepare_only, kernel_name, language, progress_bar, log_output, stdout_file, stderr_file, start_timeout, report_mode, cwd, **engine_kwargs)

pm.execute_notebook("notebooks/connection.ipynb",
       'reports/connection_report.ipynb',
        # parameters=parameters,
        parameters={'db':'db-dev'},

        log_output=True,
    )