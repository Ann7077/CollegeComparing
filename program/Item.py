# Need modification, certain sections migh have changed names or years

class ItemDef:
    def __init__(this, CNid, description, name): 
        this.CNid = CNid
        this.description = description
        this.name = name

item = []

item.append(ItemDef(-39, ['',''],                                                                                                                       'School_links')) 

item.append(ItemDef(-38, ['Faculty And Graduate Assistants By Primary Function, Fall 2020','Full Time', 'Part Time'],                                   'General_information'))

item.append(ItemDef(-37, ['Estimated Expenses For Academic Year','2018-2019','2019-2020','2020-2021','2021-2022','% Change 2020-2021 To 2021-2022'],    'Tuition_fees_and_estimated_student_expenses_Estimated_expenses_for_academic_year'))

item.append(ItemDef(-35, ['Average Graduate Student Tuition And Fees For Academic Year','2021-2022'],                                                   'Tuition_fees_and_estimated_student_expenses_Average_graduate_student_tuition_and_fees_for_academic_year'))

item.append(ItemDef(-34, ['Type Of Plan','Offered'],                                                                                                    'Tuition_fees_and_estimated_student_expenses_Type_of_plan'))

item.append(ItemDef(-33, ['Type Of Aid','Number Receiving Aid','Percent Receving Aid','Total Amount Of Aid Received','Average Amount Of Aid Received'], 'Financial_aid_Full-time_beginning_undergraduate'))

item.append(ItemDef(-32, ['Type Of Aid','Number Receiving Aid','Total Amount Of Aid Received','Average Amount Of Aid Received'],                        'Financial_aid_All_undergraduates'))

item.append(ItemDef(-31, ['','2018-2019','2019-2020','2020-2021'],                                                                                      'Net_price_Average_net_price'))

item.append(ItemDef(-30, ['Average Net Price By Income','2018-2019','2019-2020','2020-2021'],                                                           'Net_price_Average_net_price_by_income'))

item.append(ItemDef(-29, ['Total Enrollment',''],                                                                                                       'Enrollment_Total_enrollment'))

item.append(ItemDef(-22, ['','Total','Male','Female'],                                                                                                  'Admissions_Applicants'))

item.append(ItemDef(-20, ['Students Submitting Scores','Number','Percent'],                                                                             'Admissions_Students_submitting_scores'))

item.append(ItemDef(-19, ['Test Scores','25th Percentile','75th Percentile'],                                                                           'Admissions_Test_scores'))

item.append(ItemDef(-10, ['Program','Postgraduate Certificate','Bachelor','Master','Doctor'],                                                           'Programs'))

item.append(ItemDef(-6,  ['NCAA Division I Without Football','Men','Women'],                                                                            'Varsity_athletic_team'))

item.append(ItemDef(-5,  ['Accreditor','Status','Next Review Date'],                                                                                    'Accreditation_Institutional_accreditation'))

item.append(ItemDef(-4,  ['Accreditor/Program','Status','Next Review Date'],                                                                            'Accreditation_Program_accreditation'))

item.append(ItemDef(-3,  ['Criminal Offences','2018','2019','2020'],                                                                                    'Campus_security_and_safety_On-campus'))

item.append(ItemDef(-2,  ['Criminal Offences','2018','2019','2020'],                                                                                    'Campus_security_and_safety_On-campus_student_housing_facilities'))

item.append(ItemDef(-1,  ['Fiscal Year','2018','2017','2016'],                                                                                          'Cohort_default_rates'))

item = tuple(item)

