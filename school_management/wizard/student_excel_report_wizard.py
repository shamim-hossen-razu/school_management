from odoo import api, exceptions, fields, models, _
from . import utility
import xlsxwriter
import io
import base64


class StudentExcelReportWizard(models.TransientModel):
    _name = 'student.excel.report.wizard'
    _description = 'Student Excel Report Wizard'
    _rec_name = 'display_name'

    student_id = fields.Many2one('school_management.student', string='Student')
    preview = fields.Html(string='HTML Content', readonly=True)

    def student_report(self):
        student_results = self.prepare_student_result() or "Nothing to show"
        table = utility.create_styled_table(student_results)
        self.write({
            'preview': table
        })

    def student_report_pdf(self):
        pass

    def student_report_excel(self):
        result = self.prepare_student_result()
        if result:
            """ Generate student report in Excel format """
            row = 0
            # Generate File name format
            filename = 'Student Report' + '.xlsx'

            # Create a workbook and add a worksheet.
            output = io.BytesIO()
            workbook = xlsxwriter.Workbook(output, {'in_memory': True})
            worksheet = workbook.add_worksheet('Student Report')

            # Set column widths
            worksheet.set_column(0, 0, 20)  # Course ID
            worksheet.set_column(1, 1, 10)  # Grade
            worksheet.set_column(2, 2, 10)  # Marks
            worksheet.set_column(3, 3, 20)  # Result Date

            # Write data to the worksheet
            for res in result:
                worksheet.write(row, 0, res['course_id'])
                worksheet.write(row, 1, res['grade'])
                worksheet.write(row, 2, res['marks'])
                worksheet.write(row, 3, res['result_date'])
                row += 1

            workbook.close()
            output.seek(0)
            export_id = self.env['excel.report.out'].create(
                {'excel_file': base64.encodebytes(output.getvalue()), 'file_name': filename})
            output.close()

            return {
                'name': 'Student Report',
                'view_mode': 'form',
                'res_id': export_id.id,
                'res_model': 'excel.report.out',
                'view_type': 'form',
                'type': 'ir.actions.act_window',
                'target': 'new',
            }
        else:
            raise exceptions.ValidationError(_('Date is not selected!'))

    def prepare_student_result(self):
        if self.student_id:
            student = self.student_id
            sql = f"""
            SELECT * FROM school_management_student as student
            INNER JOIN school_management_result as result
            ON student.id = result.student_id 
            WHERE student.id = {student.id}"""

            self.env.cr.execute(sql)
            result = self.env.cr.dictfetchall()
            return result
