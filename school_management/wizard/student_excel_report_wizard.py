from odoo import api, fields, models, _


class StudentExcelReportWizard(models.TransientModel):
    _name = 'student.excel.report.wizard'
    _description = 'Student Excel Report Wizard'

    student_id = fields.Many2one('school_management.student', string='Student')
    preview = fields.Html(string='HTML Content', readonly=True)

    def student_report(self):
        pass

    def student_report_pdf(self):
        pass

    def student_report_excel(self):
        pass
