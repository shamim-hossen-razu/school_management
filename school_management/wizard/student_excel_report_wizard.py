from odoo import api, fields, models, _


class StudentExcelReportWizard(models.TransientModel):
    _name = 'student.excel.report.wizard'
    _description = 'Student Excel Report Wizard'

    student_id = fields.Many2one('school_management.student', string='Student')
    preview = fields.Html(string='HTML Content', readonly=True)

    def student_report(self):
        html = self.prepare_student_report()
        if html:
            self.write({'preview': html})


    def student_report_pdf(self):
        pass

    def student_report_excel(self):
        pass

    def prepare_student_report(self):
        if self.student_id:
            student = self.student_id
            html = f"""
                <table>
                    <tr>
                        <td>Student Name: </td>
                        <td>{student.name or 'No Name'}</td>
                    </tr>
                    <tr>
                        <td>Student Roll: </td>
                        <td>{student.roll_number or 'No roll Number'}</td>
                    </tr>
                    <tr>
                        <td>Student Class: </td>
                        <td>{student.standard or ' No Standard'}</td>
                    </tr>
                    <tr>
                        <td>Student Section: </td>
                        <td>{student.section or 'No section'}</td>
                    </tr>
            </table>
            """
            return html
